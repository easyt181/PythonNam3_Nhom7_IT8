import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from main_ui import Ui_MainWindow
import mysql.connector
from datetime import datetime, date
from baocaothongke.bieudothongke import BieuDo
from baocaothongke.hoadonban import HoaDonBan
from baocaothongke.hoadonnhap import HoaDonNhap
from baocaothongke.hoadontrahang import HoaDonTraHang
from baocaothongke.hoadonthuetruyen import HoaDonChoThue
from baocaothongke.baocaothongke import BaoCaoThongKe
from quanlynhapsach.PageNhapSach import QLNhapSach
from quanlysach.PageSach import QLSach

class MySidebar(QMainWindow, Ui_MainWindow):
    def __init__(self, user_info):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý cửa hàng truyện")
        self.icon_only_menu.setHidden(True)
        self.frame.setHidden(True)
        self.user_info = user_info
        self.lbNametk.setText(user_info[1])
        self.phanquyen = user_info[3] 
        self.setupDatabaseConnection()  
        self.btnLogOut.clicked.connect(self.logout)
        # Các nút sidebar
        if self.phanquyen == "admin":
            self.showThongke()
            self.btnQLNhapSach.clicked.connect(self.showQLNhapSach)
            self.btnQLSach.clicked.connect(self.showQLSach)
            self.btnHoaDonBanHang.clicked.connect(self.showHoaDonBan)
            self.btnThongKe.clicked.connect(self.showThongke)
            self.btnHoaDonNhapHang.clicked.connect(self.showhodonnhap)
            self.btnHoaDonTraHang.clicked.connect(self.showhodontrahang)
            self.btnHoaDonThueTruyen.clicked.connect(self.showhoadonthuetruyen)
            self.btnNhanVien.clicked.connect(self.showNhanVien)
            self.btnBanHang.clicked.connect(self.showBanHang)
            self.btnQuanLyThue.clicked.connect(self.showQuanLyThueTruyen)
            self.btnKhachHang.clicked.connect(self.showKhachHang)

        else:
            self.showBanHang()
            self.btnQLNhapSach.clicked.connect(self.showQLNhapSach)
            self.btnQLSach.clicked.connect(self.showQLSach)
            self.btnHoaDonBanHang.clicked.connect(self.showHoaDonBan)
            self.btnHoaDonNhapHang.clicked.connect(self.showhodonnhap)
            self.btnHoaDonTraHang.clicked.connect(self.showhodontrahang)
            self.btnHoaDonThueTruyen.clicked.connect(self.showhoadonthuetruyen)
            self.btnThongKe.setHidden(True)
            self.btnNhanVien.setHidden(True)
            self.btnBanHang.clicked.connect(self.showBanHang)
            self.btnQuanLyThue.clicked.connect(self.showQuanLyThueTruyen)
            self.btnKhachHang.clicked.connect(self.showKhachHang)

    def showKhachHang(self):   
        from qlkhachhang.qlkhmain import KhachHangMain
        self.deleteDataold()
        self.QLKhachHang = KhachHangMain()
        self.verticalLayout_11.addWidget(self.QLKhachHang)

    def showQuanLyThueTruyen(self):
        from qlhoadonthue.qlthuesach import MainWindow 
        self.deleteDataold()
        nv_id = self.getNhanVien() 
        self.QLThueTruyen = MainWindow(nv_id)
        self.verticalLayout_11.addWidget(self.QLThueTruyen) 

    def showBanHang(self):  
        from qlbansach.qlbanhang import MainWindow
        self.deleteDataold()
        nv_id = self.getNhanVien()
        self.QLBanSach = MainWindow(nv_id)
        self.verticalLayout_11.addWidget(self.QLBanSach)

    def showNhanVien(self):
        from qlnhanvien.qlnvmain import QLNV
        self.deleteDataold()
        self.QLNhanVien = QLNV()
        self.verticalLayout_11.addWidget(self.QLNhanVien)   
    
    def getNhanVien(self):
        query = "SELECT nv_id FROM nhanvien INNER JOIN taikhoan ON nhanvien.nv_tk_id = taikhoan.tk_id WHERE taikhoan.tk_id = %s"
        self.db_cursor.execute(query, (self.user_info[0],))
        nv_id = self.db_cursor.fetchone()
        return nv_id[0]


    def setupDatabaseConnection(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_nhom7_python"
            )
            self.db_cursor = self.db_connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def deleteDataold(self):
        for i in reversed(range(self.verticalLayout_11.count())):
            widget = self.verticalLayout_11.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def showQLNhapSach(self): 
        self.deleteDataold()
        self.QLNhapSachWidget = QLNhapSach()
        self.verticalLayout_11.addWidget(self.QLNhapSachWidget)

    def showQLSach(self):
        self.deleteDataold()
        self.QLSachWidget = QLSach()
        self.verticalLayout_11.addWidget(self.QLSachWidget) 

    def showHoaDonBan(self):
        self.deleteDataold()
        nv_id = self.getNhanVien()
        self.hoaDonBanWidget = HoaDonBan(nv_id)
        self.verticalLayout_11.addWidget(self.hoaDonBanWidget)

    def showThongke(self):
        self.deleteDataold()
        self.baoCaoThongKeWidget = BaoCaoThongKe()
        self.verticalLayout_11.addWidget(self.baoCaoThongKeWidget)

    def showhodonnhap(self):
        self.deleteDataold()
        self.hoadonnhapWidget = HoaDonNhap()
        self.verticalLayout_11.addWidget(self.hoadonnhapWidget)

    def showhoadonthuetruyen(self):
        self.deleteDataold()
        self.hoadonchothueWidget = HoaDonChoThue()
        self.verticalLayout_11.addWidget(self.hoadonchothueWidget)

    def showhodontrahang(self):
        self.deleteDataold()  
        self.hoadontrahangWidget = HoaDonTraHang()
        self.verticalLayout_11.addWidget(self.hoadontrahangWidget)
    
    def logout(self):
        self.close()
        from dangnhap.dangnhap import Login
        self.login = Login()
        self.login.show()