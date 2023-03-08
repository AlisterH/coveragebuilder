# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_help_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help_window(object):
    def setupUi(self, help_window):
        help_window.setObjectName("help_window")
        help_window.resize(758, 511)
        self.frame = QtWidgets.QFrame(help_window)
        self.frame.setGeometry(QtCore.QRect(9, 9, 741, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.webView = QtWebKitWidgets.QWebView(self.frame)
        self.webView.setGeometry(QtCore.QRect(0, 0, 741, 491))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")

        self.retranslateUi(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

    def retranslateUi(self, help_window):
        _translate = QtCore.QCoreApplication.translate
        help_window.setWindowTitle(_translate("help_window", "Coverage Builder Help"))

from PyQt5 import QtWebKitWidgets
