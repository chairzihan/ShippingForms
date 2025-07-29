from PyQt5.QtWidgets import QApplication, QDialog
from mainGUI import Ui_mainFrame
from senderGUI import Ui_SenderInformation
from receiverGUI import Ui_senderFrame
from PyQt5.QtCore import QDate
from excelCreate import ExcelCreate
import xlwings as xw

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
            "Country": self.ui.countryInsert.toPlainText(),
            "Address": self.ui.addressInsert.toPlainText(),
            "Location": self.ui.destinationAddressInsert.toPlainText()
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
        self.ui.finishButton.clicked.connect(self.finishUpdatingSettings)
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
    
    def finishUpdatingSettings(self):
        import yamlManager
        
        destFile = ExcelCreate.copyExcel()
        wb = xw.Book(destFile)
        sheet = wb.sheets["Sheet1"]
        
        receiverName = self.ui.receiverSelect.currentText()
        senderName = self.ui.senderSelect.currentText()
        
        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        mdanC = self.ui.mdanCQuaInput.value()
        mdbnB = self.ui.mdbnBInput.value()
        mgao = self.ui.mgaoAInput.value()
        mdbo = self.ui.mdboAInput.value()
        

        sender = yamlManager.get_sender_by_name(senderName)
        if sender:
            senderEmail = sender.get("Email")
            senderPhone = sender.get("Phone")

        receiver = yamlManager.get_receiver_by_name(receiverName)
        if receiver:
            receiverPhone = receiver.get("Contact Number")
            receiverCity = receiver.get("City")
            receiverPostal = receiver.get("Postal")
            receiverCompany = receiver.get("Company")
            receiverCountry = receiver.get("Country")
            receiverAddress = receiver.get("Address")
            receiverDestination = receiver.get("Location")

        

        sheet.range((5,7)).value = date

        #sender inputs
        sheet.range((8,3)).value = senderName
        sheet.range((9,3)).value = senderPhone
        sheet.range((10,3)).value = senderEmail

        #receiver inputs
        sheet.range((7,7)).value = receiverDestination
        sheet.range((8,9)).value = receiverCompany
        sheet.range((9,9)).value = receiverName
        sheet.range((10,9)).value = receiverPhone
        sheet.range((13,9)).value = receiverCity
        sheet.range((15,9)).value = receiverPostal
        sheet.range((16,9)).value = receiverCountry
        sheet.range((11,9)).value = receiverAddress
        wb.save()
        
        








    




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