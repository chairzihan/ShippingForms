from PyQt5.QtWidgets import QApplication, QDialog
from mainGUI import Ui_mainFrame
import sys

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_mainFrame()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())