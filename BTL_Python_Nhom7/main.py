from PySide6.QtWidgets import QApplication
from dangnhap.dangnhap import Login
import sys
app = QApplication(sys.argv)
loginWindow = Login()
loginWindow.show()
app.exec()