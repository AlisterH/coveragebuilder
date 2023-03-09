# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_coveragebuilder.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CoverageBuilder(object):
    def setupUi(self, CoverageBuilder):
        CoverageBuilder.setObjectName("CoverageBuilder")
        CoverageBuilder.setWindowModality(QtCore.Qt.NonModal)
        CoverageBuilder.resize(507, 460)
        CoverageBuilder.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox = QtWidgets.QDialogButtonBox(CoverageBuilder)
        self.buttonBox.setGeometry(QtCore.QRect(0, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblGrille = QtWidgets.QLabel(CoverageBuilder)
        self.lblGrille.setGeometry(QtCore.QRect(90, 70, 41, 51))
        self.lblGrille.setFrameShape(QtWidgets.QFrame.Box)
        self.lblGrille.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblGrille.setLineWidth(1)
        self.lblGrille.setMidLineWidth(0)
        self.lblGrille.setText("")
        self.lblGrille.setPixmap(QtGui.QPixmap(":/plugins/coveragebuilder/grille.png"))
        self.lblGrille.setScaledContents(True)
        self.lblGrille.setObjectName("lblGrille")
        self.gridLayoutWidget = QtWidgets.QWidget(CoverageBuilder)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 200, 444, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.cbbComp = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbbComp.setObjectName("cbbComp")
        self.gridLayout.addWidget(self.cbbComp, 1, 2, 1, 1)
        self.lblComp = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblComp.setObjectName("lblComp")
        self.gridLayout.addWidget(self.lblComp, 1, 0, 1, 1)
        self.lieOutDir = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lieOutDir.setText("")
        self.lieOutDir.setObjectName("lieOutDir")
        self.gridLayout.addWidget(self.lieOutDir, 4, 2, 1, 1)
        self.lblOutDir = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblOutDir.setObjectName("lblOutDir")
        self.gridLayout.addWidget(self.lblOutDir, 4, 0, 1, 1)
        self.overlapInp = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.overlapInp.setMaximum(50)
        self.overlapInp.setSingleStep(5)
        self.overlapInp.setProperty("value", 0)
        self.overlapInp.setObjectName("overlapInp")
        self.gridLayout.addWidget(self.overlapInp, 5, 2, 1, 1)
        self.lblOverlap = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblOverlap.setObjectName("lblOverlap")
        self.gridLayout.addWidget(self.lblOverlap, 5, 0, 1, 1)
        self.btnUpdate = QtWidgets.QToolButton(self.gridLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/coveragebuilder/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon)
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout.addWidget(self.btnUpdate, 1, 3, 1, 1)
        self.btnShow = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnShow.setObjectName("btnShow")
        self.gridLayout.addWidget(self.btnShow, 1, 4, 1, 1)
        self.btnBrowse = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 4, 4, 1, 1)
        self.lblInLayer = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblInLayer.setObjectName("lblInLayer")
        self.gridLayout.addWidget(self.lblInLayer, 0, 0, 1, 1)
        self.cbbInLayer = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbbInLayer.setObjectName("cbbInLayer")
        self.gridLayout.addWidget(self.cbbInLayer, 0, 2, 1, 1)
        self.btnCreerSyno = QtWidgets.QPushButton(CoverageBuilder)
        self.btnCreerSyno.setGeometry(QtCore.QRect(150, 370, 201, 27))
        self.btnCreerSyno.setObjectName("btnCreerSyno")
        self.chkGrille = QtWidgets.QCheckBox(CoverageBuilder)
        self.chkGrille.setGeometry(QtCore.QRect(140, 80, 211, 22))
        self.chkGrille.setObjectName("chkGrille")
        self.chkDyn = QtWidgets.QCheckBox(CoverageBuilder)
        self.chkDyn.setGeometry(QtCore.QRect(140, 140, 251, 22))
        self.chkDyn.setObjectName("chkDyn")
        self.lblDyn = QtWidgets.QLabel(CoverageBuilder)
        self.lblDyn.setGeometry(QtCore.QRect(90, 130, 41, 51))
        self.lblDyn.setFrameShape(QtWidgets.QFrame.Box)
        self.lblDyn.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblDyn.setLineWidth(1)
        self.lblDyn.setMidLineWidth(0)
        self.lblDyn.setText("")
        self.lblDyn.setPixmap(QtGui.QPixmap(":/plugins/coveragebuilder/grille_dyn.png"))
        self.lblDyn.setScaledContents(True)
        self.lblDyn.setObjectName("lblDyn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(CoverageBuilder)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 371, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aboutButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.aboutButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        self.aboutButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.aboutButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/coveragebuilder/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutButton.setIcon(icon1)
        self.aboutButton.setIconSize(QtCore.QSize(30, 30))
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout.addWidget(self.aboutButton)
        self.lblEntete = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblEntete.setFont(font)
        self.lblEntete.setTextFormat(QtCore.Qt.AutoText)
        self.lblEntete.setObjectName("lblEntete")
        self.horizontalLayout.addWidget(self.lblEntete)
        self.helpButton = QtWidgets.QToolButton(CoverageBuilder)
        self.helpButton.setEnabled(True)
        self.helpButton.setGeometry(QtCore.QRect(460, 10, 36, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        self.helpButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.helpButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/coveragebuilder/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon2)
        self.helpButton.setIconSize(QtCore.QSize(30, 30))
        self.helpButton.setObjectName("helpButton")

        self.retranslateUi(CoverageBuilder)
        self.buttonBox.accepted.connect(CoverageBuilder.accept)
        self.buttonBox.rejected.connect(CoverageBuilder.reject)
        QtCore.QMetaObject.connectSlotsByName(CoverageBuilder)

    def retranslateUi(self, CoverageBuilder):
        _translate = QtCore.QCoreApplication.translate
        CoverageBuilder.setWindowTitle(_translate("CoverageBuilder", "Coverage Builder"))
        self.lblComp.setText(_translate("CoverageBuilder", "Print layout :"))
        self.lblOutDir.setText(_translate("CoverageBuilder", "Outfiles directory :"))
        self.lblOverlap.setText(_translate("CoverageBuilder", "Overlap % :"))
        self.btnUpdate.setText(_translate("CoverageBuilder", "..."))
        self.btnShow.setText(_translate("CoverageBuilder", "Show"))
        self.btnBrowse.setText(_translate("CoverageBuilder", "Browse"))
        self.lblInLayer.setText(_translate("CoverageBuilder", "Extent layer :"))
        self.btnCreerSyno.setText(_translate("CoverageBuilder", "Create coverage layer(s)"))
        self.chkGrille.setText(_translate("CoverageBuilder", "Generate regular coverage layer"))
        self.chkDyn.setText(_translate("CoverageBuilder", "Generate irregular coverage layer"))
        self.aboutButton.setText(_translate("CoverageBuilder", "..."))
        self.lblEntete.setText(_translate("CoverageBuilder", "Coverage Builder"))
        self.helpButton.setText(_translate("CoverageBuilder", "..."))

