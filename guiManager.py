from PyQt5.QtWidgets import QApplication, QDialog
from mainGUI import Ui_mainFrame
from senderGUI import Ui_SenderInformation
from receiverGUI import Ui_senderFrame
from PyQt5.QtCore import QDate
from excelCreate import ExcelCreate
import xlwings as xw
from PyQt5.QtCore import Qt


progress = 0
countryOfOrigin ="THAILAND"

#mdanC defaults
mdanCDescription = "50Ga OLT Optical Transceiver for PON"
mdanCPartNumber = "3TN01273BCAA"
mdanCPrice = "$250.00"

#mdbnB defaults
mdbnBDescription = "50Ga ONU Optical Transceiver for PON"
mdbnBPartNumber = "3TN00704CBAA"
mdbnBPrice = "$250.00"

#mgaoA defaults
mgaoADescription = "50Gs OLT Optical Transceiver for PON"
mgaoAPartNumber = "3FE79858AAAA"
mgaoAPrice = "$1000.00"
#mdanC defaults
mdboDescription = "50Gs ONU Optical Transceiver for PON "
mdboPartNumber = "3FE49859CAAA"
mdboPrice = "$1000.00"


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

        self.setTabOrder(self.ui.postalZipInsert,self.ui.countryInsert)
        self.setTabOrder(self.ui.countryInsert,self.ui.cityInsert)
        self.setTabOrder(self.ui.cityInsert,self.ui.contactPhoneInsert)
        self.setTabOrder(self.ui.contactPhoneInsert,self.ui.addressInsert)
        self.setTabOrder(self.ui.addressInsert,self.ui.companyNameInsert)
        self.setTabOrder(self.ui.companyNameInsert,self.ui.contactInsert)
        self.setTabOrder(self.ui.contactInsert,self.ui.destinationAddressInsert)
        self.setTabOrder(self.ui.destinationAddressInsert,self.ui.finishButton)
        self.setTabOrder(self.ui.finishButton,self.ui.postalZipInsert)

        self.ui.postalZipInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.countryInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.cityInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.contactPhoneInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.addressInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.companyNameInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.contactInsert.setFocusPolicy(Qt.StrongFocus)
        self.ui.destinationAddressInsert.setFocusPolicy(Qt.StrongFocus)


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
        self.setTabOrder(self.ui.dateEdit, self.ui.newSenderButton)
        self.setTabOrder(self.ui.newSenderButton, self.ui.newReceiverButton)
        self.setTabOrder(self.ui.newReceiverButton, self.ui.mdanCQuaInput)
        self.setTabOrder(self.ui.mdanCQuaInput, self.ui.mdbnBInput)
        self.setTabOrder(self.ui.mdbnBInput, self.ui.mgaoAInput)
        self.setTabOrder(self.ui.mgaoAInput, self.ui.mdboAInput)
        self.setTabOrder( self.ui.mdboAInput, self.ui.finishButton)
        
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
        
        if mdanC>0:
             sheet.range((27,9)).value = mdanC
             sheet.range((27,2)).value = mdanCPartNumber
             sheet.range((27,4)).value = mdanCDescription
             sheet.range((27,10)).value = mdanCPrice
             sheet.range((27,11)).value = countryOfOrigin
        if mdbnB>0:
             sheet.range((28,9)).value = mdbnB
             sheet.range((28,2)).value = mdbnBPartNumber
             sheet.range((28,4)).value = mdbnBDescription
             sheet.range((28,10)).value = mdbnBPrice
             sheet.range((28,11)).value = countryOfOrigin
        if mgao>0:
             sheet.range((29,9)).value = mgao
             sheet.range((29,2)).value = mgaoAPartNumber
             sheet.range((29,4)).value = mgaoADescription
             sheet.range((29,10)).value = mgaoAPrice
             sheet.range((29,11)).value = countryOfOrigin
        if mdbo>0:
             sheet.range((30,9)).value = mdbo
             sheet.range((30,2)).value = mdboPartNumber
             sheet.range((30,4)).value = mdboDescription
             sheet.range((30,10)).value = mdboPrice
             sheet.range((30,11)).value = countryOfOrigin
        
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