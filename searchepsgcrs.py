# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Search EPSG CRS
                                 A QGIS plugin
 Search for a valid CRS on the basis of an EPSG code.
 This plugin uses epsg.io
                              -------------------
        begin                : 2014-05-05
        copyright            : (C) 2014 by Cayetano Benavent
        email                : cayetanobv@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from searchepsgcrsdialog import SearchEpsgCrsDock
# Other imports
import os.path
import urllib2
import socket
import re
import json


class SearchEpsgCrs:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'searchepsgcrs_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dock = SearchEpsgCrsDock()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/searchepsgcrs/icon.png"),
            u"Search and format EPSG CRS...", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Search and format EPSG CRS Plugin", self.action)

        # Add dock dialog to the right
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # connecting buttons and functions
        QObject.connect(self.dock.FormattedCRSButton, SIGNAL("clicked()"), self.getCRSResult)
        QObject.connect(self.dock.getEPSGActiveLayerButton, SIGNAL("clicked()"), self.setActLayerCRS)
        QObject.connect(self.dock.transfCRSButton, SIGNAL("clicked()"), self.getCRSResult2)
        QObject.connect(self.dock.aboutButton, SIGNAL("clicked()"), self.about)
        QObject.connect(self.dock.helpButton, SIGNAL("clicked()"), self.getHelp)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Search and format EPSG CRS Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        # show the dialog
        self.dock.show()

    def getCRSResult(self):
        self.dock.clearTextBrowser()
        self.dock.setTextBrowser(self.searchCRS())

    def getCRSResult2(self):
        self.dock.clearTextBrowser2()
        self.dock.setTextBrowser2(self.searchCRSTransform())

    def setActLayerCRS(self):
        # get active layer Coordinate Reference System
        layer = iface.activeLayer()
        if layer:
            crs = layer.crs().authid()
            # extracting from result EPSG number code (remove from string "EPSG:")
            self.dock.setTextCRS(crs[5:])
        else:
            # if no active layer in TOC...
            QMessageBox.information(self.iface.mainWindow(),"Get active layer CRS",
                "No active layer in the Table of Contents.")

    @staticmethod
    def __getContent(url, timeout=2):
        # timeout (seconds)
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Custom User-Agent')
        url_open = urllib2.urlopen(req, timeout=timeout)
        return url_open.read()

    def searchCRS(self):
        # this function does the CRS search using EPSG.io website
        try:
            EPSG = self.dock.getTextCRS()
            CRS_format = self.dock.getComboCRS()
            url = "http://epsg.io/{0}{1}".format(EPSG, CRS_format)

            content = self.__getContent(url)

            if re.search("Sorry, that page cannot be found", content):
                return "---Error: Wrong EPSG code.---\n"
            elif re.search("Something went wrong", content):
                return "---Error: Wrong EPSG code.---\n"
            elif re.search("Direct IP access not allowed ", content):
                return "---Error: Wrong EPSG code.---\n"
            elif not content:
                return "---No content for this format---"

            return "\t--CRS in %s--\n\n%s\n" % (CRS_format, content)

        except socket.timeout as e:
            return "---Sorry, but something didn't work.\nError: %r\ntimeout is %i s" % (e, timeout)
        except:
            return "---Sorry, but something didn't work.\n---Maybe a wrong EPSG code."


    def searchCRSTransform(self):
        # this function does the CRS transform search using EPSG.io API
        try:
            EPSG = self.dock.getTextCRS()
            url = "http://epsg.io/?q={0}&format=json&trans=1".format(EPSG)

            content = self.__getContent(url)

            json_results = json.loads(content)

            if json_results:
                n_rslts = json_results.get('number_result', 0)
                jsn_rslts = json_results.get('results')
                rslts_epsg = jsn_rslts[0].get('code')
                if n_rslts == 0 or rslts_epsg != EPSG:
                    return "---No Results.---\nError: Wrong EPSG code.---\n"

                else:
                    crs_transf = jsn_rslts[0].get('trans')
                    default_trans = jsn_rslts[0].get('default_trans')
                    crs_name = jsn_rslts[0].get('name')
                    crs_kind = jsn_rslts[0].get('kind')
                    crs_area = jsn_rslts[0].get('area')
                    txtTransf_str = 'CRS name: %s\n\nCRS kind: %s\n\nCRS area: %s\n\n No. of CRS transformations: %i\n'
                    txtTransf = txtTransf_str % (crs_name, crs_kind, crs_area, len(crs_transf))

                    if len(crs_transf) > 0:
                        txtTransf += '\nCRS Transformations list:\n'
                        for tr in crs_transf:
                            nm = tr.get('name')
                            cd = tr.get('code_trans')
                            ac = str(tr.get('accuracy'))
                            ar = tr.get('area')

                            str_transf = '- %s (EPSG Trans: %s)/ (Accuracy: %s) Area: %s' % (nm, cd, ac, ar)
                            if default_trans == tr.get('code_trans'):
                                str_transf += ' / DEFAULT'
                            txtTransf += str_transf + '\n\n'

                    return txtTransf

        except socket.timeout as e:
            return "---Sorry, but something didn't work.\nError: %r\ntimeout is %i s" % (e, timeout)
        except:
            return "---Sorry, but something didn't work.\n---Maybe a wrong EPSG code."

    def about(self):
        QMessageBox.about(self.iface.mainWindow(),"About",
            """
            Developed by Cayetano Benavent 2014.

            This plugin uses EPSG.io API website.
            The EPSG.io website is built around
            the official EPSG database maintained
            by OGP Geomatics Committee.
            """)

    def getHelp(self):
        QMessageBox.information(self.iface.mainWindow(),"Help",
            """
            1) Type EPSG code or push button "Get active
            layer EPSG CRS code".

            2) Push button "Get Formatted CRS" in "Formatted
            CRS" tab or push button "Get CRS transformations"
            in "Transformations info" tab.

            """)
