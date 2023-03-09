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
        About_window.resize(490, 213)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(About_window.sizePolicy().hasHeightForWidth())
        About_window.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(About_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(About_window)
        self.buttonBox.accepted.connect(About_window.accept)
        QtCore.QMetaObject.connectSlotsByName(About_window)

    def retranslateUi(self, About_window):
        _translate = QtCore.QCoreApplication.translate
        About_window.setWindowTitle(_translate("About_window", "About Coverage Builder"))
        self.label_2.setText(_translate("About_window", "<html><head/><body><p align=\"center\"><img src=\":/plugins/coveragebuilder/icon.png\"/></p><p align=\"center\">Coverage Builder Version 0.5.0</p></body></html>"))
        self.label.setText(_translate("About_window", "<html><head/><body><p align=\"center\">This is an updated version of the &quot;Grids for Atlas&quot; plugin, previously published by:<br/>Experts SIG / <a href=\"https://www.biotope.fr/\"><span style=\" text-decoration: underline; color:#0000ff;\">Biotope</span></a><br/>Bertrand Chaussat<br/>Dmitry Kiselev</p><p align=\"center\">homepage = <a href=\"https://github.com/alisterh/coveragebuilder\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/alisterh/coveragebuilder<br/></span></a>tracker = <a href=\"https://github.com/alisterh/coveragebuilder/issues\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/alisterh/coveragebuilder/issues</span></a></p></body></html>"))

from . import resources
