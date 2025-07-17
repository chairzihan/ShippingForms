# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYiAOlO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtWidgets import QDialogButtonBox, QPlainTextEdit, QLabel, QCheckBox
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject, Qt


class Ui_SenderInformation(object):
    def setupUi(self, SenderInformation):
        if not SenderInformation.objectName():
            SenderInformation.setObjectName(u"SenderInformation")
        SenderInformation.resize(400, 300)
        self.finishButton = QDialogButtonBox(SenderInformation)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(40, 250, 341, 32))
        self.finishButton.setOrientation(Qt.Horizontal)
        self.finishButton.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.emailInput = QPlainTextEdit(SenderInformation)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(30, 180, 341, 41))
        self.emailLabel = QLabel(SenderInformation)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(30, 150, 251, 21))
        self.phoneNumberLabel = QLabel(SenderInformation)
        self.phoneNumberLabel.setObjectName(u"phoneNumberLabel")
        self.phoneNumberLabel.setGeometry(QRect(30, 50, 311, 21))
        self.phoneNumberInput = QPlainTextEdit(SenderInformation)
        self.phoneNumberInput.setObjectName(u"phoneNumberInput")
        self.phoneNumberInput.setGeometry(QRect(30, 80, 341, 41))
        self.notificationCheckBox = QCheckBox(SenderInformation)
        self.notificationCheckBox.setObjectName(u"notificationCheckBox")
        self.notificationCheckBox.setGeometry(QRect(30, 230, 201, 18))

        self.retranslateUi(SenderInformation)
        self.finishButton.accepted.connect(SenderInformation.accept)
        self.finishButton.rejected.connect(SenderInformation.reject)

        QMetaObject.connectSlotsByName(SenderInformation)
    # setupUi

    def retranslateUi(self, SenderInformation):
        SenderInformation.setWindowTitle(QCoreApplication.translate("SenderInformation", u"Dialog", None))
        self.emailLabel.setText(QCoreApplication.translate("SenderInformation", u"Please input the e-mail associated with this sender:", None))
        self.phoneNumberLabel.setText(QCoreApplication.translate("SenderInformation", u"Please input the phone number associated with this sender:", None))
        self.notificationCheckBox.setText(QCoreApplication.translate("SenderInformation", u"Be notified of shipment WB #?", None))
    # retranslateUi