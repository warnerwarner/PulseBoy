# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoiseValveWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 76)
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
        self.lengthEdit = QtWidgets.QLineEdit(Form)
        self.lengthEdit.setEnabled(False)
        self.lengthEdit.setObjectName("lengthEdit")
        self.gridLayout.addWidget(self.lengthEdit, 1, 9, 1, 1)
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
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 9)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 6, 1, 1)
        self.seedEdit = QtWidgets.QLineEdit(Form)
        self.seedEdit.setObjectName("seedEdit")
        self.gridLayout.addWidget(self.seedEdit, 1, 4, 1, 1)
        self.ampMaxEdit = QtWidgets.QLineEdit(Form)
        self.ampMaxEdit.setObjectName("ampMaxEdit")
        self.gridLayout.addWidget(self.ampMaxEdit, 1, 7, 1, 1)
        self.repeatsEdit = QtWidgets.QLineEdit(Form)
        self.repeatsEdit.setObjectName("repeatsEdit")
        self.gridLayout.addWidget(self.repeatsEdit, 0, 9, 1, 1)
        self.frequencyEdit = QtWidgets.QLineEdit(Form)
        self.frequencyEdit.setObjectName("frequencyEdit")
        self.gridLayout.addWidget(self.frequencyEdit, 1, 3, 1, 1)
        self.repeatsRadio = QtWidgets.QRadioButton(Form)
        self.repeatsRadio.setChecked(True)
        self.repeatsRadio.setAutoExclusive(False)
        self.repeatsRadio.setObjectName("repeatsRadio")
        self.gridLayout.addWidget(self.repeatsRadio, 0, 8, 1, 1)
        self.ampMinEdit = QtWidgets.QLineEdit(Form)
        self.ampMinEdit.setObjectName("ampMinEdit")
        self.gridLayout.addWidget(self.ampMinEdit, 1, 6, 1, 1)
        self.lengthRadio = QtWidgets.QRadioButton(Form)
        self.lengthRadio.setAutoExclusive(False)
        self.lengthRadio.setObjectName("lengthRadio")
        self.gridLayout.addWidget(self.lengthRadio, 1, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.shatterHzEdit = QtWidgets.QLineEdit(Form)
        self.shatterHzEdit.setObjectName("shatterHzEdit")
        self.gridLayout.addWidget(self.shatterHzEdit, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.removeButton = QtWidgets.QToolButton(Form)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 1, 0, 1, 1)
        self.position = QtWidgets.QLabel(Form)
        self.position.setObjectName("position")
        self.gridLayout.addWidget(self.position, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.repeatsRadio.clicked.connect(self.lengthRadio.toggle)
        self.lengthRadio.clicked.connect(self.repeatsRadio.toggle)
        self.repeatsRadio.toggled['bool'].connect(self.repeatsEdit.setEnabled)
        self.lengthRadio.toggled['bool'].connect(self.lengthEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lengthEdit.setText(_translate("Form", "1"))
        self.onsetEdit.setText(_translate("Form", "0.1"))
        self.label_2.setText(_translate("Form", "Offset"))
        self.label.setText(_translate("Form", "Onset"))
        self.offsetEdit.setText(_translate("Form", "0.1"))
        self.label_7.setText(_translate("Form", "Amp Max (/1)"))
        self.label_6.setText(_translate("Form", "Amp Min (/1)"))
        self.seedEdit.setText(_translate("Form", "1"))
        self.ampMaxEdit.setText(_translate("Form", "0.9"))
        self.repeatsEdit.setText(_translate("Form", "5"))
        self.frequencyEdit.setText(_translate("Form", "20"))
        self.repeatsRadio.setText(_translate("Form", "Repeats"))
        self.ampMinEdit.setText(_translate("Form", "0.1"))
        self.lengthRadio.setText(_translate("Form", "Length (s)"))
        self.label_8.setText(_translate("Form", "Shatter (Hz)"))
        self.label_4.setText(_translate("Form", "Frequncy (Hz)"))
        self.shatterHzEdit.setText(_translate("Form", "500"))
        self.label_5.setText(_translate("Form", "Seed"))
        self.removeButton.setText(_translate("Form", "-"))
        self.position.setText(_translate("Form", "1"))

