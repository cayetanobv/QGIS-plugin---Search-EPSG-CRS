# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchepsgcrs.ui'
#
# Created: Mon Oct 13 03:05:24 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SearchEPSGCRS_dock(object):
    def setupUi(self, SearchEPSGCRS_dock):
        SearchEPSGCRS_dock.setObjectName(_fromUtf8("SearchEPSGCRS_dock"))
        SearchEPSGCRS_dock.resize(303, 575)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchEPSGCRS_dock.sizePolicy().hasHeightForWidth())
        SearchEPSGCRS_dock.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.dockWidgetContents.setFont(font)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtFeedback = QtGui.QTextBrowser(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFeedback.sizePolicy().hasHeightForWidth())
        self.txtFeedback.setSizePolicy(sizePolicy)
        self.txtFeedback.setMinimumSize(QtCore.QSize(270, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txtFeedback.setFont(font)
        self.txtFeedback.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtFeedback.setFrameShape(QtGui.QFrame.StyledPanel)
        self.txtFeedback.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtFeedback.setLineWidth(1)
        self.txtFeedback.setAcceptRichText(True)
        self.txtFeedback.setObjectName(_fromUtf8("txtFeedback"))
        self.gridLayout.addWidget(self.txtFeedback, 3, 0, 1, 2)
        self.comboCRS = QtGui.QComboBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboCRS.sizePolicy().hasHeightForWidth())
        self.comboCRS.setSizePolicy(sizePolicy)
        self.comboCRS.setMinimumSize(QtCore.QSize(120, 30))
        self.comboCRS.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboCRS.setObjectName(_fromUtf8("comboCRS"))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.comboCRS.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboCRS, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(270, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setMinimumSize(QtCore.QSize(270, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(285, 85))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(15, 28, 140, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.txtCRS = QtGui.QLineEdit(self.dockWidgetContents)
        self.txtCRS.setGeometry(QtCore.QRect(165, 15, 126, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCRS.sizePolicy().hasHeightForWidth())
        self.txtCRS.setSizePolicy(sizePolicy)
        self.txtCRS.setMinimumSize(QtCore.QSize(120, 30))
        self.txtCRS.setMaxLength(10)
        self.txtCRS.setObjectName(_fromUtf8("txtCRS"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 51, 270, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(270, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        SearchEPSGCRS_dock.setWidget(self.dockWidgetContents)

        self.retranslateUi(SearchEPSGCRS_dock)
        QtCore.QMetaObject.connectSlotsByName(SearchEPSGCRS_dock)

    def retranslateUi(self, SearchEPSGCRS_dock):
        SearchEPSGCRS_dock.setWindowTitle(QtGui.QApplication.translate("SearchEPSGCRS_dock", "Get formatted CRS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SearchEPSGCRS_dock", "Select output format:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtFeedback.setHtml(QtGui.QApplication.translate("SearchEPSGCRS_dock", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(0, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".prettywkt", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(1, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".wkt", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(2, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".esriwkt", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(3, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".gml", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(4, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".xml", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(5, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".proj4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(6, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".js", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(7, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".geoserver", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(8, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".mapfile", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(9, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".mapnik", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(10, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".mapnikpython", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCRS.setItemText(11, QtGui.QApplication.translate("SearchEPSGCRS_dock", ".sql", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SearchEPSGCRS_dock", "GET FORMATTED CRS", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("SearchEPSGCRS_dock", "About this plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SearchEPSGCRS_dock", "Type EPSG CRS code:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtCRS.setText(QtGui.QApplication.translate("SearchEPSGCRS_dock", "25830", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("SearchEPSGCRS_dock", "Get active layer EPSG CRS code", None, QtGui.QApplication.UnicodeUTF8))

