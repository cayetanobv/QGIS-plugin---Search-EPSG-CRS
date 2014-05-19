# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Search EPSG CRS Dialog
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

from PyQt4 import QtCore, QtGui
from ui_searchepsgcrs import Ui_SearchEpsgCrs
# create the dialog


class SearchEpsgCrsDialog(QtGui.QDialog, Ui_SearchEpsgCrs):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def setTextBrowser(self, output):
        self.txtFeedback.setText(output)

    def clearTextBrowser(self):
        self.txtFeedback.clear()

    def setTextCRS(self, output):
        self.txtCRS.setText(output)
    
    def getTextCRS(self):
        return self.txtCRS.text()

    def getComboCRS(self):
        return self.comboCRS.currentText()
