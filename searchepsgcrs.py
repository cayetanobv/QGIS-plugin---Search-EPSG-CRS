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
from searchepsgcrsdialog import SearchEpsgCrsDialog
# Other imports
import os.path
import httplib2
import re


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
        self.dlg = SearchEpsgCrsDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/searchepsgcrs/icon.png"),
            u"Search EPSG CRS...", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Search EPSG CRS Plugin", self.action)

        # connecting buttons and functions
        QObject.connect(self.dlg.pushButton, SIGNAL("clicked()"), self.getCRSResult)
        QObject.connect(self.dlg.pushButton_2, SIGNAL("clicked()"), self.setActLayerCRS)
        QObject.connect(self.dlg.pushButton_3, SIGNAL("clicked()"), self.about)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Search EPSG CRS Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        # show the dialog
        self.dlg.show()

        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            pass

    def getCRSResult(self):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser(self.searchCRS())

    def setActLayerCRS(self):
        # get active layer Coordinate Reference System
        layer = iface.activeLayer()
        if layer:
            crs = layer.crs().authid()
            # extract from result EPSG number code (remove from string "EPSG:")
            self.dlg.setTextCRS(crs[5:])
        else:
            # if no active layer in TOC...
            QMessageBox.information(self.iface.mainWindow(),"Get active layer CRS", "No active layer in the Table of Contents.")

    def searchCRS(self):
        # this function do the CRS search using EPSG.io website
        try:
            EPSG = self.dlg.getTextCRS()
            CRS_format = self.dlg.getComboCRS()
            url = "http://epsg.io/"+ EPSG + CRS_format
    
            resp, content = httplib2.Http().request(url)
    
            if re.search("Sorry, that page cannot be found", content):
                return "---Error: Wrong EPSG code.---\n"
            elif re.search("Something went wrong", content):
                return "---Error: Wrong EPSG code.---\n"
            elif re.search("Direct IP access not allowed ", content):
                return "---Error: Wrong EPSG code.---\n"
            elif not content:
                return "---No content for this format---"
            
            return "\t--CRS in " + CRS_format + "--\n\n" + content + "\n"

        except:
            # You must have an Internet connection
            return "---Error: something didn't work---\nDo you have an Internet connection?"

    def about(self):
        QMessageBox.about(self.iface.mainWindow(),"About", 
            """
            Developed by Cayetano Benavent 2014.
            
            This plugin uses EPSG.io website.
            The EPSG.io website is built around 
            the official EPSG database maintained 
            by OGP Geomatics Committee.
            """)
