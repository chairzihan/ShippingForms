from PyQt5.QtWidgets import QApplication, QDialog
from mainGUI import Ui_mainFrame
from senderGUI import Ui_SenderInformation
from receiverGUI import Ui_senderFrame
from PyQt5.QtCore import QDate

progress = 0

class SenderDialog(QDialog):
    def __init__(self, main_dialog):
        super().__init__()
        self.ui = Ui_SenderInformation()
        self.ui.setupUi(self)
        self.ui.finishButton.clicked.connect(self.saveSender)
        self.main_dialog = main_dialog
        
    
    def saveSender(self):
        senderData ={
            "Name": self.ui.nameInput.toPlainText(),
            "Email": self.ui.emailInput.toPlainText(),
            "Phone": self.ui.phoneNumberInput.toPlainText(),
            "Notify": self.ui.notificationCheckBox.isChecked()
        }
        from yamlManager import add_sender
        add_sender(senderData)
        self.main_dialog.updateGUI()

    

class ReceiverDialog(QDialog):
    def __init__(self, main_dialog):
        super().__init__()
        self.ui = Ui_senderFrame()
        self.ui.setupUi(self)
        self.ui.finishButton.clicked.connect(self.saveReceiver)
        self.main_dialog = main_dialog

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
        self.main_dialog.updateGUI()
    
    

    

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainFrame()
        self.ui.setupUi(self)
        self.ui.newSenderButton.clicked.connect(self.open_sender_dialog)
        self.ui.newReceiverButton.clicked.connect(self.openReceiverDialog)
        self.ui.setTodayDateButton.clicked.connect(self.setTodayDate)
        self.updateGUI()

    #open sender screen
    def open_sender_dialog(self):
        dialog = SenderDialog(self)
        dialog.exec_() 

    #open receiver screen
    def openReceiverDialog(self):
        receiverFrame = ReceiverDialog(self)
        receiverFrame.exec_()

    #set Today's date
    def setTodayDate(self):
        today = QDate.currentDate()
        self.ui.dateEdit.setDate(today)
        progress=25
        self.ui.progressBar.setValue(progress)

    def updateGUI(self):
        from yamlManager import get_receivers
        from yamlManager import get_senders
        receivers = get_receivers()
        senders = get_senders()
        # Clear previous items before adding new ones
        self.ui.receiverSelect.clear()
        self.ui.senderSelect.clear()
        names = [r.get("Contact Name", "") for r in receivers]
        self.ui.receiverSelect.addItems(names)
        sNames = [r.get("Name", "") for r in senders]
        self.ui.senderSelect.addItems(sNames)
    
    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    main = MainDialog()
    main.show()
    sys.exit(app.exec_())