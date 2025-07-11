import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Shipping Forms")
        self.setGeometry(100, 100, 800,800)

        # Create a label and button
        self.label = QLabel("Hello, PyQt5!", self)
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_click)

        # Layout to arrange widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


