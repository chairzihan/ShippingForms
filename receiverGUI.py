# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designersbsSSg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import QDialogButtonBox, QPlainTextEdit, QLabel
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject, Qt


class Ui_senderFrame(object):
    def setupUi(self, senderFrame):
        if not senderFrame.objectName():
            senderFrame.setObjectName(u"senderFrame")
        senderFrame.resize(700, 650)
        self.finishButton = QDialogButtonBox(senderFrame)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(70, 530, 560, 50))
        self.finishButton.setOrientation(Qt.Horizontal)
        self.finishButton.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.companyNameInsert = QPlainTextEdit(senderFrame)
        self.companyNameInsert.setObjectName(u"companyNameInsert")
        self.companyNameInsert.setGeometry(QRect(20, 350, 320, 50))
        self.companyName = QLabel(senderFrame)
        self.companyName.setObjectName(u"companyName")
        self.companyName.setGeometry(QRect(20, 320, 180, 30))
        self.contactName = QLabel(senderFrame)
        self.contactName.setObjectName(u"contactName")
        self.contactName.setGeometry(QRect(370, 320, 180, 30))
        self.contactInsert = QPlainTextEdit(senderFrame)
        self.contactInsert.setObjectName(u"contactInsert")
        self.contactInsert.setGeometry(QRect(370, 350, 320, 50))
        self.contactPhone = QLabel(senderFrame)
        self.contactPhone.setObjectName(u"contactPhone")
        self.contactPhone.setGeometry(QRect(20, 200, 180, 30))
        self.contactPhoneInsert = QPlainTextEdit(senderFrame)
        self.contactPhoneInsert.setObjectName(u"contactPhoneInsert")
        self.contactPhoneInsert.setGeometry(QRect(20, 230, 320, 50))
        self.address = QLabel(senderFrame)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(370, 200, 180, 30))
        self.addressInsert = QPlainTextEdit(senderFrame)
        self.addressInsert.setObjectName(u"addressInsert")
        self.addressInsert.setGeometry(QRect(370, 230, 320, 50))
        self.destinationLabel = QLabel(senderFrame)
        self.destinationLabel.setObjectName(u"destinationLabel")
        self.destinationLabel.setGeometry(QRect(20, 420, 180, 30))
        self.destinationAddressInsert = QPlainTextEdit(senderFrame)
        self.destinationAddressInsert.setObjectName(u"destinationAddressInsert")
        self.destinationAddressInsert.setGeometry(QRect(20, 450, 670, 60))
        self.postalZip = QLabel(senderFrame)
        self.postalZip.setObjectName(u"postalZip")
        self.postalZip.setGeometry(QRect(20, 80, 180, 30))
        self.postalZipInsert = QPlainTextEdit(senderFrame)
        self.postalZipInsert.setObjectName(u"postalZipInsert")
        self.postalZipInsert.setGeometry(QRect(20, 110, 320, 50))
        self.countryInsert = QPlainTextEdit(senderFrame)
        self.countryInsert.setObjectName(u"countryInsert")
        self.countryInsert.setGeometry(QRect(370, 140, 140, 30))
        self.countryLabel = QLabel(senderFrame)
        self.countryLabel.setObjectName(u"countryLabel")
        self.countryLabel.setGeometry(QRect(370, 110, 140, 30))
        self.cityLabel = QLabel(senderFrame)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setGeometry(QRect(540, 110, 140, 30))
        self.cityInsert = QPlainTextEdit(senderFrame)
        self.cityInsert.setObjectName(u"cityInsert")
        self.cityInsert.setGeometry(QRect(540, 140, 140, 30))
        self.dialogLabel = QLabel(senderFrame)
        self.dialogLabel.setObjectName(u"dialogLabel")
        self.dialogLabel.setGeometry(QRect(20, 20, 660, 30))

        self.retranslateUi(senderFrame)
        self.finishButton.accepted.connect(senderFrame.accept)
        self.finishButton.rejected.connect(senderFrame.reject)

        QMetaObject.connectSlotsByName(senderFrame)
    # setupUi

    def retranslateUi(self, senderFrame):
        senderFrame.setWindowTitle(QCoreApplication.translate("senderFrame", u"Dialog", None))
        self.companyName.setText(QCoreApplication.translate("senderFrame", u"Company Name", None))
        self.contactName.setText(QCoreApplication.translate("senderFrame", u"Contact Name", None))
        self.contactPhone.setText(QCoreApplication.translate("senderFrame", u"Contact Phone #", None))
        self.address.setText(QCoreApplication.translate("senderFrame", u"Address", None))
        self.postalZip.setText(QCoreApplication.translate("senderFrame", u"Postal Zip", None))
        self.countryLabel.setText(QCoreApplication.translate("senderFrame", u"Country", None))
        self.cityLabel.setText(QCoreApplication.translate("senderFrame", u"City", None))
        self.dialogLabel.setText(QCoreApplication.translate("senderFrame", u"Sender Profile", None))
        self.destinationLabel.setText(QCoreApplication.translate("senderFrame", u"Destination Address", None))
    # retranslateUi

