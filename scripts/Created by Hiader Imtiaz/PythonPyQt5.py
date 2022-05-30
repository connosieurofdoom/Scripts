# Python PyQt5
# pip install pyqt5
import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
app = QApplication([])
w = QWidget()
# Resize Window
w.resize(300, 300)
# Set Title
w.setWindowTitle('PyQt5 from Medium')
# Text Labels
label = QLabel('Name')
label.move(20, 20)
# Buttons
btn1 = QPushButton('Press', w)
btn1.move(20, 60)
# Set Button Action
btn1.clicked.connect(app.quit)
# Input Box
entry1 = QLineEdit(w)
entry1.move(20, 100)
# Message Boxes
msgBox = QMessageBox()
msgBox.setText('Hello World')
# Check Box
checkBox = QCheckBox('Check Me', w)
checkBox.move(20, 140)
# Radio Buttons
radioBtn1 = QRadioButton('Radio 1', w)
radioBtn1.move(20, 180)
w.show()
sys.exit(app.exec_())