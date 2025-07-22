from PyQt5.QtWidgets import QApplication, QDialog
from mainGUI import Ui_mainFrame
from senderGUI import Ui_SenderInformation
from receiverGUI import Ui_senderFrame
import datetime
from PyQt5.QtCore import QDate

progress = 0

class SenderDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SenderInformation()
        self.ui.setupUi(self)
    
    def saveSender(self):
        senderData ={
            "name": self.ui.nameInput.toPlainText(),
            "email": self.ui.emailInput.toPlainText(),
            "phone": self.ui.phoneNumberInput.toPlainText(),
            "notify": self.ui.notificationCheckBox.isChecked()
        }
        from yamlManager import add_sender
        add_sender(senderData)

class ReceiverDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_senderFrame()
        self.ui.setupUi(self)
    
    def saveReceiver(self):
        receiverData = {
            "Contact Name": self.ui.contactInsert.toPlainText(),
            "Contact Number": self.ui.contactPhoneInsert.toPlainText(),
            "City": self.ui.cityInsert.toPlainText(),
            "Company": self.ui.companyNameInsert.toPlainText(),                
            "Postal": self.ui.postalZipInsert.toPlainText(),
            "Country": self.ui.countryInsert.toPlainText()
            }
        from yamlManager import add_receiver
        add_receiver(receiverData)
    

    

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainFrame()
        self.ui.setupUi(self)
        self.ui.newSenderButton.clicked.connect(self.open_sender_dialog)
        self.ui.newReceiverButton.clicked.connect(self.openReceiverDialog)
        self.ui.setTodayDateButton.clicked.connect(self.setTodayDate)

    #open sender screen
    def open_sender_dialog(self):
        dialog = SenderDialog()
        dialog.exec_() 

    #open receiver screen
    def openReceiverDialog(self):
        receiverFrame = ReceiverDialog()
        receiverFrame.exec_()

    #set Today's date
    def setTodayDate(self):
        today = QDate.currentDate()
        self.ui.dateEdit.setDate(today)
        progress=25
        self.ui.progressBar.setValue(progress)

    
    
    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    main = MainDialog()
    main.show()
    sys.exit(app.exec_())