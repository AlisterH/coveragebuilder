# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About_window(object):
    def setupUi(self, About_window):
        About_window.setObjectName("About_window")
        About_window.resize(400, 300)
        self.label = QtWidgets.QLabel(About_window)
        self.label.setGeometry(QtCore.QRect(70, 150, 291, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About_window)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 181, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(About_window)
        QtCore.QMetaObject.connectSlotsByName(About_window)

    def retranslateUi(self, About_window):
        _translate = QtCore.QCoreApplication.translate
        About_window.setWindowTitle(_translate("About_window", "About Coverage Builder"))
        self.label.setText(_translate("About_window", "Developer : Bertrand Chaussat"))
        self.label_2.setText(_translate("About_window", "Coverage Builder Version 0.5.0"))

