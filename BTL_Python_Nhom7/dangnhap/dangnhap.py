from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from dangnhap.DangNhap_ui import Ui_MainWindow
import mysql.connector


class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý cửa hàng truyện")
        self.btnDangNhap.clicked.connect(self.kiemTraDangNhap)
        self.btnThoat.clicked.connect(self.close)

        self.db_connection = None
        self.ketNoiCSDL()

    def ketNoiCSDL(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="",  
                database="db_nhom7_python"  
            )
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi kết nối", f"Không thể kết nối đến cơ sở dữ liệu:\n{err}")

    def kiemTraDangNhap(self):
        taiKhoan = self.txtTaiKhoan.toPlainText()
        matKhau = self.txtMatKhau.toPlainText()

        if self.db_connection is None or not self.db_connection.is_connected():
            QMessageBox.critical(self, "Lỗi kết nối", "Không thể kết nối đến cơ sở dữ liệu")
            return

        cursor = self.db_connection.cursor()
        query = "SELECT * FROM taikhoan WHERE tk_username=%s AND tk_password=%s"
        cursor.execute(query, (taiKhoan, matKhau))
        result = cursor.fetchone()

        if result:
            self.dangNhapThanhCong(result)
        else:
            QMessageBox.warning(self, "Đăng nhập thất bại", "Sai tài khoản hoặc mật khẩu!")

    def dangNhapThanhCong(self, user_info):
        from index import MySidebar
        self.mainWindow = MySidebar(user_info)
        self.mainWindow.show()
        self.close()