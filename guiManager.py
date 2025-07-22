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

class ReceiverDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_senderFrame()
        self.ui.setupUi(self)

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