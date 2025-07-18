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
        senderFrame.resize(400, 300)
        self.finishButton = QDialogButtonBox(senderFrame)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(40, 250, 341, 32))
        self.finishButton.setOrientation(Qt.Horizontal)
        self.finishButton.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.companyNameInsert = QPlainTextEdit(senderFrame)
        self.companyNameInsert.setObjectName(u"companyNameInsert")
        self.companyNameInsert.setGeometry(QRect(10, 200, 181, 31))
        self.companyName = QLabel(senderFrame)
        self.companyName.setObjectName(u"companyName")
        self.companyName.setGeometry(QRect(10, 180, 91, 16))
        self.contactName = QLabel(senderFrame)
        self.contactName.setObjectName(u"contactName")
        self.contactName.setGeometry(QRect(210, 180, 91, 16))
        self.contactInsert = QPlainTextEdit(senderFrame)
        self.contactInsert.setObjectName(u"contactInsert")
        self.contactInsert.setGeometry(QRect(210, 200, 181, 31))
        self.contactPhone = QLabel(senderFrame)
        self.contactPhone.setObjectName(u"contactPhone")
        self.contactPhone.setGeometry(QRect(10, 110, 91, 16))
        self.contactPhoneInsert = QPlainTextEdit(senderFrame)
        self.contactPhoneInsert.setObjectName(u"contactPhoneInsert")
        self.contactPhoneInsert.setGeometry(QRect(10, 130, 181, 31))
        self.address = QLabel(senderFrame)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(210, 110, 91, 16))
        self.addressInsert = QPlainTextEdit(senderFrame)
        self.addressInsert.setObjectName(u"addressInsert")
        self.addressInsert.setGeometry(QRect(210, 130, 181, 31))
        self.postalZip = QLabel(senderFrame)
        self.postalZip.setObjectName(u"postalZip")
        self.postalZip.setGeometry(QRect(10, 50, 91, 16))
        self.postalZipInsert = QPlainTextEdit(senderFrame)
        self.postalZipInsert.setObjectName(u"postalZipInsert")
        self.postalZipInsert.setGeometry(QRect(10, 70, 181, 31))
        self.countryInsert = QPlainTextEdit(senderFrame)
        self.countryInsert.setObjectName(u"countryInsert")
        self.countryInsert.setGeometry(QRect(210, 80, 81, 20))
        self.countryLabel = QLabel(senderFrame)
        self.countryLabel.setObjectName(u"countryLabel")
        self.countryLabel.setGeometry(QRect(210, 60, 91, 16))
        self.cityLabel = QLabel(senderFrame)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setGeometry(QRect(310, 60, 91, 16))
        self.cityInsert = QPlainTextEdit(senderFrame)
        self.cityInsert.setObjectName(u"cityInsert")
        self.cityInsert.setGeometry(QRect(310, 80, 81, 20))
        self.dialogLabel = QLabel(senderFrame)
        self.dialogLabel.setObjectName(u"dialogLabel")
        self.dialogLabel.setGeometry(QRect(10, 20, 351, 16))

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
    # retranslateUi

