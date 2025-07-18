# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShippingFormUIvRojOq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import QDialogButtonBox, QComboBox, QProgressBar, QDateEdit, QPushButton, QLabel, QLineEdit, QSpinBox
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject

from senderGUI import Ui_SenderInformation

import sys


# Main UI class for the Shipping Form
class Ui_mainFrame(object):
    def setupUi(self, mainFrame):
        # Set up the main frame
        if not mainFrame.objectName():
            mainFrame.setObjectName(u"mainFrame")
        mainFrame.resize(700, 600)

        # Sender selection
        self.senderSelect = QComboBox(mainFrame)
        self.senderSelect.setObjectName(u"senderSelect")
        self.senderSelect.setGeometry(QRect(270, 70, 150, 32))

        # Progress bar
        self.progressBar = QProgressBar(mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 520, 631, 41))
        self.progressBar.setValue(0)

        # Date edit and related controls
        self.dateEdit = QDateEdit(mainFrame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(40, 70, 150, 32))

        self.setTodayDateButton = QPushButton(mainFrame)
        self.setTodayDateButton.setObjectName(u"setTodayDateButton")
        self.setTodayDateButton.setGeometry(QRect(40, 110, 151, 32))

        self.dateButtonBox = QDialogButtonBox(mainFrame)
        self.dateButtonBox.setObjectName(u"dateButtonBox")
        self.dateButtonBox.setGeometry(QRect(40, 150, 151, 32))
        self.dateButtonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.dateLabel = QLabel(mainFrame)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(40, 40, 121, 31))

        # Sender controls
        self.senderLabel = QLabel(mainFrame)
        self.senderLabel.setObjectName(u"senderLabel")
        self.senderLabel.setGeometry(QRect(270, 40, 91, 31))

        self.newSenderButton = QPushButton(mainFrame)
        self.newSenderButton.setObjectName(u"newSenderButton")
        self.newSenderButton.setGeometry(QRect(270, 150, 151, 32))

    

        

        # Receiver controls
        self.receiverSelect = QComboBox(mainFrame)
        self.receiverSelect.setObjectName(u"receiverSelect")
        self.receiverSelect.setGeometry(QRect(470, 70, 150, 32))

        self.receiverLabel = QLabel(mainFrame)
        self.receiverLabel.setObjectName(u"receiverLabel")
        self.receiverLabel.setGeometry(QRect(470, 40, 91, 31))

        self.newReceiverButton = QPushButton(mainFrame)
        self.newReceiverButton.setObjectName(u"newReceiverButton")
        self.newReceiverButton.setGeometry(QRect(470, 150, 151, 32))

        self.lineEdit = QLineEdit(mainFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 110, 151, 28))

        self.receiverInput = QLineEdit(mainFrame)
        self.receiverInput.setObjectName(u"receiverInput")
        self.receiverInput.setGeometry(QRect(470, 110, 151, 28))

        # Module selection label
        self.moduleSeleLabel = QLabel(mainFrame)
        self.moduleSeleLabel.setObjectName(u"moduleSeleLabel")
        self.moduleSeleLabel.setGeometry(QRect(40, 200, 300, 41))

        # MDAN-C controls
        self.mdanCQuaInput = QSpinBox(mainFrame)
        self.mdanCQuaInput.setObjectName(u"mdanCQuaInput")
        self.mdanCQuaInput.setGeometry(QRect(40, 300, 91, 32))

        self.mdanCLabel = QLabel(mainFrame)
        self.mdanCLabel.setObjectName(u"mdanCLabel")
        self.mdanCLabel.setGeometry(QRect(40, 250, 81, 31))

        self.mdanCQuaLabel = QLabel(mainFrame)
        self.mdanCQuaLabel.setObjectName(u"mdanCQuaLabel")
        self.mdanCQuaLabel.setGeometry(QRect(40, 270, 81, 31))

        # MDBN-B controls
        self.mdbnBQuaLabel = QLabel(mainFrame)
        self.mdbnBQuaLabel.setObjectName(u"mdbnBQuaLabel")
        self.mdbnBQuaLabel.setGeometry(QRect(170, 270, 81, 31))

        self.mdbnBInput = QSpinBox(mainFrame)
        self.mdbnBInput.setObjectName(u"mdbnBInput")
        self.mdbnBInput.setGeometry(QRect(170, 300, 91, 32))

        self.mdbnBLabel = QLabel(mainFrame)
        self.mdbnBLabel.setObjectName(u"mdbnBLabel")
        self.mdbnBLabel.setGeometry(QRect(170, 250, 81, 31))

        # MGAO-A controls
        self.mgaoAQuaLabel = QLabel(mainFrame)
        self.mgaoAQuaLabel.setObjectName(u"mgaoAQuaLabel")
        self.mgaoAQuaLabel.setGeometry(QRect(300, 270, 81, 31))

        self.mgaoAInput = QSpinBox(mainFrame)
        self.mgaoAInput.setObjectName(u"mgaoAInput")
        self.mgaoAInput.setGeometry(QRect(300, 300, 91, 32))

        self.mgaoA = QLabel(mainFrame)
        self.mgaoA.setObjectName(u"mgaoA")
        self.mgaoA.setGeometry(QRect(300, 250, 81, 31))

        # MDBO-A controls
        self.mdboAQuaLabel = QLabel(mainFrame)
        self.mdboAQuaLabel.setObjectName(u"mdboAQuaLabel")
        self.mdboAQuaLabel.setGeometry(QRect(430, 270, 81, 31))

        self.mdboAInput = QSpinBox(mainFrame)
        self.mdboAInput.setObjectName(u"mdboAInput")
        self.mdboAInput.setGeometry(QRect(430, 300, 91, 32))

        self.mdboA = QLabel(mainFrame)
        self.mdboA.setObjectName(u"mdboA")
        self.mdboA.setGeometry(QRect(430, 250, 81, 31))

        # Finish button
        self.finishButton = QPushButton(mainFrame)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(200, 400, 300, 41))

        # Retranslate UI (set text)
        self.retranslateUi(mainFrame)

        # Connect slots by name
        QMetaObject.connectSlotsByName(mainFrame)
    # setupUi

    def retranslateUi(self, mainFrame):
        # Set all UI text (for translation/localization)
        mainFrame.setWindowTitle(QCoreApplication.translate("mainFrame", u"Shipping Form Manager", None))
        self.setTodayDateButton.setText(QCoreApplication.translate("mainFrame", u"Use Today's Date", None))
        self.dateLabel.setText(QCoreApplication.translate("mainFrame", u"Date", None))
        self.senderLabel.setText(QCoreApplication.translate("mainFrame", u"Sender", None))
        self.newSenderButton.setText(QCoreApplication.translate("mainFrame", u" New Sender", None))
        self.receiverLabel.setText(QCoreApplication.translate("mainFrame", u"Receiver", None))
        self.newReceiverButton.setText(QCoreApplication.translate("mainFrame", u"New Receiver", None))
        self.moduleSeleLabel.setText(QCoreApplication.translate("mainFrame", u"Module Selection", None))
        self.mdanCLabel.setText(QCoreApplication.translate("mainFrame", u"MDAN-C", None))
        self.mdanCQuaLabel.setText(QCoreApplication.translate("mainFrame", u"Quantity:", None))
        self.mdbnBQuaLabel.setText(QCoreApplication.translate("mainFrame", u"Quantity:", None))
        self.mdbnBLabel.setText(QCoreApplication.translate("mainFrame", u"MDBN-B", None))
        self.mgaoAQuaLabel.setText(QCoreApplication.translate("mainFrame", u"Quantity:", None))
        self.mgaoA.setText(QCoreApplication.translate("mainFrame", u"MGAO-A", None))
        self.mdboAQuaLabel.setText(QCoreApplication.translate("mainFrame", u"Quantity:", None))
        self.mdboA.setText(QCoreApplication.translate("mainFrame", u"MDBO-A", None))
        self.finishButton.setText(QCoreApplication.translate("mainFrame", u"Finish", None))
    # retranslateUi

