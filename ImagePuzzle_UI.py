# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\zhusun\asunlab\GameTools\ImagePuzzle\ImagePuzzle.ui'
#
# Created: Wed Mar 18 16:46:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ImagePuzzle(object):
    def setupUi(self, ImagePuzzle):
        ImagePuzzle.setObjectName("ImagePuzzle")
        ImagePuzzle.resize(794, 601)
        self.groupBox = QtGui.QGroupBox(ImagePuzzle)
        self.groupBox.setGeometry(QtCore.QRect(400, 470, 381, 121))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.resY = QtGui.QSpinBox(self.gridLayoutWidget)
        self.resY.setMinimum(16)
        self.resY.setMaximum(40000)
        self.resY.setProperty("value", 2048)
        self.resY.setObjectName("resY")
        self.gridLayout.addWidget(self.resY, 0, 2, 1, 1)
        self.resX = QtGui.QSpinBox(self.gridLayoutWidget)
        self.resX.setMinimum(16)
        self.resX.setMaximum(40000)
        self.resX.setProperty("value", 2048)
        self.resX.setObjectName("resX")
        self.gridLayout.addWidget(self.resX, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.tileY = QtGui.QSpinBox(self.gridLayoutWidget)
        self.tileY.setMinimum(1)
        self.tileY.setMaximum(100)
        self.tileY.setProperty("value", 4)
        self.tileY.setObjectName("tileY")
        self.gridLayout.addWidget(self.tileY, 1, 2, 1, 1)
        self.tileX = QtGui.QSpinBox(self.gridLayoutWidget)
        self.tileX.setMinimum(1)
        self.tileX.setMaximum(100)
        self.tileX.setProperty("value", 8)
        self.tileX.setObjectName("tileX")
        self.gridLayout.addWidget(self.tileX, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.outputPath = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.outputPath.setObjectName("outputPath")
        self.horizontalLayout_3.addWidget(self.outputPath)
        self.groupBox_2 = QtGui.QGroupBox(ImagePuzzle)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 10, 381, 461))
        self.groupBox_2.setObjectName("groupBox_2")
        self.labelPreview = QtGui.QLabel(self.groupBox_2)
        self.labelPreview.setGeometry(QtCore.QRect(10, 20, 361, 421))
        self.labelPreview.setText("")
        self.labelPreview.setObjectName("labelPreview")
        self.groupBox_3 = QtGui.QGroupBox(ImagePuzzle)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 381, 581))
        self.groupBox_3.setObjectName("groupBox_3")
        # self.listWidget = QtGui.QListWidget(self.groupBox_3)
        # self.listWidget.setGeometry(QtCore.QRect(10, 20, 361, 511))
        # self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 540, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnDel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnDel.setObjectName("btnDel")
        self.horizontalLayout.addWidget(self.btnDel)
        self.btnClear = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.sortBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.sortBtn.setObjectName("sortBtn")
        self.horizontalLayout.addWidget(self.sortBtn)
        self.previewBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.previewBtn.setObjectName("previewBtn")
        self.horizontalLayout.addWidget(self.previewBtn)
        self.btnOutput = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnOutput.setObjectName("btnOutput")
        self.horizontalLayout.addWidget(self.btnOutput)

        self.retranslateUi(ImagePuzzle)
        QtCore.QMetaObject.connectSlotsByName(ImagePuzzle)

    def retranslateUi(self, ImagePuzzle):
        ImagePuzzle.setWindowTitle(QtGui.QApplication.translate("ImagePuzzle", "ImagePuzzle", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ImagePuzzle", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.resY.setSuffix(QtGui.QApplication.translate("ImagePuzzle", " pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.resX.setSuffix(QtGui.QApplication.translate("ImagePuzzle", " pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ImagePuzzle", "Tile", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImagePuzzle", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ImagePuzzle", "output path", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ImagePuzzle", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ImagePuzzle", "Image Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("ImagePuzzle", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("ImagePuzzle", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.sortBtn.setText(QtGui.QApplication.translate("ImagePuzzle", "Sort", None, QtGui.QApplication.UnicodeUTF8))
        self.previewBtn.setText(QtGui.QApplication.translate("ImagePuzzle", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOutput.setText(QtGui.QApplication.translate("ImagePuzzle", "Output", None, QtGui.QApplication.UnicodeUTF8))

