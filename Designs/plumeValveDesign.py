# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/PlumeValveWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(848, 76)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.dataSamplingRateEdit = QtWidgets.QLineEdit(Form)
        self.dataSamplingRateEdit.setObjectName("dataSamplingRateEdit")
        self.gridLayout.addWidget(self.dataSamplingRateEdit, 1, 5, 1, 1)
        self.onsetEdit = QtWidgets.QLineEdit(Form)
        self.onsetEdit.setObjectName("onsetEdit")
        self.gridLayout.addWidget(self.onsetEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(Form)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.shatterHzEdit = QtWidgets.QLineEdit(Form)
        self.shatterHzEdit.setObjectName("shatterHzEdit")
        self.gridLayout.addWidget(self.shatterHzEdit, 1, 3, 1, 1)
        self.removeButton = QtWidgets.QToolButton(Form)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 1, 0, 1, 1)
        self.openPlumeDataButton = QtWidgets.QPushButton(Form)
        self.openPlumeDataButton.setObjectName("openPlumeDataButton")
        self.gridLayout.addWidget(self.openPlumeDataButton, 0, 4, 1, 1)
        self.plumeDataLabel = QtWidgets.QLabel(Form)
        self.plumeDataLabel.setObjectName("plumeDataLabel")
        self.gridLayout.addWidget(self.plumeDataLabel, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.targetMaxEdit = QtWidgets.QLineEdit(Form)
        self.targetMaxEdit.setObjectName("targetMaxEdit")
        self.gridLayout.addWidget(self.targetMaxEdit, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dataSamplingRateEdit.setText(_translate("Form", "10000"))
        self.onsetEdit.setText(_translate("Form", "0.1"))
        self.label_2.setText(_translate("Form", "Offset"))
        self.label.setText(_translate("Form", "Onset"))
        self.offsetEdit.setText(_translate("Form", "0.1"))
        self.label_8.setText(_translate("Form", "Shatter (Hz)"))
        self.shatterHzEdit.setText(_translate("Form", "500"))
        self.removeButton.setText(_translate("Form", "-"))
        self.openPlumeDataButton.setText(_translate("Form", "Open Plume Data"))
        self.plumeDataLabel.setText(_translate("Form", "-"))
        self.label_5.setText(_translate("Form", "Data Sampling Rate"))
        self.targetMaxEdit.setText(_translate("Form", "1.0"))
        self.label_3.setText(_translate("Form", "Target Max."))

