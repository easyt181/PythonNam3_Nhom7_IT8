from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QDate
from PySide6.QtCore import Qt
import sys
import re
from datetime import datetime
import mysql.connector

from qlbansach.qlbanhang_ui import Ui_MainWindow
from qlbansach.hoadonmua_ui import Ui_hoadonmua_dialog
from qlbansach.hoadonthue_ui import Ui_Dialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, nv_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_to_db()
        self.nv_id = nv_id
        self.load_data()
        self.setup_table()
        self.cart_data = []
        self.ui.btn_search.clicked.connect(lambda: self.search())
        self.set_com()  

        self.ui.btn_mua.clicked.connect(lambda: self.btn_mua())
        self.ui.btn_thue.clicked.connect(lambda: self.btn_thue())


    def setup_table(self):
        self.ui.gio_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header_gio = self.ui.gio_table.horizontalHeader()
        header_gio.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        header_gio.setStretchLastSection(True)
        self.ui.sach_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header_sach = self.ui.sach_table.horizontalHeader()
        header_sach.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        header_sach.setStretchLastSection(True)
        for row in range(self.ui.gio_table.rowCount()):
            item = QTableWidgetItem(self.ui.gio_table.item(row, 2))
            item.setFlags(item.flags() | Qt.ItemIsEditable)

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_nhom7_python"
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn = None

    def load_data(self):
        if not self.conn:
            return

        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM sach"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.ui.sach_table.setRowCount(len(rows))
            self.ui.sach_table.setColumnCount(len(rows[0]) + 1)
            self.ui.gio_table.verticalHeader().setVisible(False)
            self.ui.sach_table.verticalHeader().setVisible(False)
            rows_to_remove = []

            for row_num, row_data in enumerate(rows):
                if row_data[6] == 0:
                    rows_to_remove.append(row_num)
                else:
                    for col_num, data in enumerate(row_data):
                        self.ui.sach_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
                        self.ui.sach_table.setItem(row_num, 6, QTableWidgetItem("Còn hàng"))
                    self.add_button(row_num)
                    self.style_table(row_num)
            for row_num in reversed(rows_to_remove):
                self.ui.sach_table.removeRow(row_num)

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def set_com(self):
        cursor = self.conn.cursor()
        query_ = "SELECT s_theloaisach FROM sach"
        cursor.execute(query_)
        rows_ = cursor.fetchall()
        added_items = set()
        self.ui.loaisach.addItem("Thể loại sách")
        for row in rows_:
            value = row[0]
            if value not in added_items:
                self.ui.loaisach.addItem(value)
                added_items.add(value)

    def add_button(self, row_num):
        self.edit_btn = QPushButton("Thêm", self)
        self.edit_btn.setStyleSheet("Background-color: green; color: white; font-weight: bold; font-size: 14px;")
        self.edit_btn.setFixedSize(61, 31)
        icon = QIcon(":/icon/add-to-cart(1).png")
        self.edit_btn.setIcon(icon)

        self.edit_btn.clicked.connect(lambda: self.btn_add_cart(row_num))

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(self.edit_btn)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.sach_table.setCellWidget(row_num, self.ui.sach_table.columnCount() - 1, widget)

    def btn_add_cart(self, row_num):
        id = self.ui.sach_table.item(row_num, 0)
        ten = self.ui.sach_table.item(row_num, 1)
        gia = self.ui.sach_table.item(row_num, 4)
        self.add_cart(id.text(),ten.text(), gia.text())

    def add_cart(self, id, ten, gia):
        exists = False
        for item in self.cart_data:
            if item['ten'] == ten:
                exists = True
                item['qty'] += 1
                break

        if not exists:
            self.cart_data.append({'id': id, 'ten': ten, 'gia': gia, 'qty': 1})

        self.refresh_table()

    def btn_del(self, num):
        self.edit_btn = QPushButton("Xóa", self)
        self.edit_btn.setStyleSheet("Background-color: red; color: white; font-weight: bold; font-size: 14px;")
        self.edit_btn.setFixedSize(61, 31)
        self.edit_btn.clicked.connect(lambda: self.delete_row(num))
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(self.edit_btn)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self.ui.gio_table.setCellWidget(num, self.ui.gio_table.columnCount() - 1, widget)

    def delete_row(self, num):
        if num >= 0 and num < len(self.cart_data):
            del self.cart_data[num]
            self.refresh_table()

    def search(self):
        cursor = self.conn.cursor()

        query = "SELECT * FROM sach WHERE"

        id = self.ui.Masach.text()
        ten = self.ui.tensach.text()
        loai = self.ui.loaisach.currentText()
        gia = self.ui.gia.text()

        conditions = []

        if id != '':
            conditions.append(f" s_id LIKE '%{id}%'")
        if ten != '':
            conditions.append(f" s_tensach LIKE '%{ten}%'")
        if loai != 'Thể loại sách':
            conditions.append(f" s_theloaisach LIKE '%{loai}%'")
        if gia != '':
            conditions.append(f" s_gia LIKE '%{gia}%'")

        if conditions:
            query += ' AND '.join(conditions)

        if query != "SELECT * FROM sach WHERE":
            self.ui.sach_table.clearContents()
            self.ui.sach_table.setRowCount(0)
            cursor.execute(query)
            rows = cursor.fetchall()

            self.ui.sach_table.setRowCount(len(rows))
            rows_to_remove = []

            for row_num, row_data in enumerate(rows):
                if row_data[6] == 0:
                    rows_to_remove.append(row_num)
                else:
                    for col_num, data in enumerate(row_data):
                        self.ui.sach_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
                        self.ui.sach_table.setItem(row_num, 6, QTableWidgetItem("Còn hàng"))
                    self.add_button(row_num)
                    self.style_table(row_num)
            for row_num in reversed(rows_to_remove):
                self.ui.sach_table.removeRow(row_num)

            cursor.close()
        else:
            self.load_data()

    def style_table(self, row_num):
        self.ui.sach_table.setRowHeight(row_num, 35)
        self.ui.sach_table.setColumnWidth(0, 60)
        self.ui.sach_table.setColumnWidth(1, 200)
        self.ui.sach_table.setColumnWidth(2, 100)
        self.ui.sach_table.setColumnWidth(3, 150)
        self.ui.sach_table.setColumnWidth(4, 70)
        self.ui.sach_table.setColumnWidth(5, 60)
        self.ui.sach_table.setColumnWidth(6, 80)
        self.ui.sach_table.setColumnWidth(7, 50)

        self.ui.gio_table.setColumnWidth(0, 130)
        self.ui.gio_table.setColumnWidth(1, 60)
        self.ui.gio_table.setColumnWidth(2, 30)
        self.ui.gio_table.setColumnWidth(3, 50)

    def refresh_table(self):
        self.ui.gio_table.clearContents()
        self.ui.gio_table.setRowCount(len(self.cart_data))
        for row, item in enumerate(self.cart_data):
            self.ui.gio_table.setItem(row, 0, QTableWidgetItem(item['ten']))
            self.ui.gio_table.setItem(row, 1, QTableWidgetItem(item['gia']))
            self.ui.gio_table.setItem(row, 2, QTableWidgetItem(str(item['qty'])))
            self.btn_del(row)

        for row in range(self.ui.gio_table.rowCount()):
            self.ui.gio_table.setVerticalHeaderItem(row, QTableWidgetItem(str(row + 1)))
        self.ui.gio_table.setRowCount(self.ui.gio_table.rowCount())

    def btn_mua(self):
        hoadon_dialog = hoadonmua(self.cart_data, self, self.nv_id)
        result = hoadon_dialog.exec()
        if result == QDialog.Rejected:
            self.connect_to_db()
            self.load_data()
            self.ui.gio_table.clearContents()
            self.ui.gio_table.setRowCount(0)
            self.cart_data.clear()
    def btn_thue(self):
        hoathue_dialog = hoadonthue(self.cart_data, self , self.nv_id)
        result = hoathue_dialog.exec()
        if result == QDialog.Rejected:
            self.connect_to_db()
            self.load_data()
            self.ui.gio_table.clearContents()
            self.ui.gio_table.setRowCount(0)
            self.cart_data.clear()


class hoadonmua(QDialog, Ui_hoadonmua_dialog):
    def __init__(self, cart_data, parent=None, nv_id=None):
        super().__init__(parent)
        self.ui = Ui_hoadonmua_dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Hóa đơn mua")
        self.cart_data = cart_data
        self.connect_to_db()
        self.load_hdm()
        self.sum()
        self.kh_id = True
        self.nv_id = nv_id

        self.ui.huy.clicked.connect(lambda: self.close())
        self.ui.thanhtoan.clicked.connect(lambda: self.btn_thanhtoan())
        self.ui.sdt.textChanged.connect(self.check_phone)
    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_nhom7_python"
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn = None
    def load_hdm(self):
        self.ui.hdm_table.setRowCount(len(self.cart_data))
        self.ui.hdm_table.setColumnCount(3)
        self.style_table()
        for row_num, item in enumerate(self.cart_data):
            self.ui.hdm_table.setItem(row_num, 0, QTableWidgetItem(item['ten']))
            self.ui.hdm_table.setItem(row_num, 1, QTableWidgetItem(item['gia']))
            self.ui.hdm_table.setItem(row_num, 2, QTableWidgetItem(str(item['qty'])))
    def style_table(self):
        self.ui.hdm_table.setColumnWidth(0, 500)
        self.ui.hdm_table.setColumnWidth(1, 250)
        self.ui.hdm_table.setColumnWidth(2, 30)

    def btn_thanhtoan(self):
        cursor = self.conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        tongtien = self.ui.tongtien.text()
        matches = re.findall(r'\d+\.\d+', tongtien)

        if matches:
            num = matches[0]
        else:
            num = 0
        id_kh = self.ui.sdt.text()
        if id_kh == "":
            self.kh_id = False
        if self.check_phone() and self.kh_id:
            cursor.execute("INSERT INTO hoadonban(hdb_nv_id, hdb_kh_sdt_id, hdb_ngayxuat, hdb_tongtien, hdb_trangthai) VALUES (%s, %s, %s, %s, %s)",
                           (self.nv_id, id_kh, date, num, 1))
        else:
            cursor.execute("INSERT INTO hoadonban(hdb_nv_id, hdb_ngayxuat, hdb_tongtien, hdb_trangthai) VALUES (%s, %s, %s, %s)",
                       (self.nv_id, date, num, 1))
        self.conn.commit()
        cursor.execute("SELECT hdb_id FROM hoadonban ORDER BY hdb_id DESC LIMIT 1")
        id = cursor.fetchone()
        hdb_id = id[0]
        row_table = self.ui.hdm_table.rowCount()

        id_list = [item['id'] for item in self.cart_data]

        for i in range(row_table):
            s_id = id_list[i]
            dongia = self.ui.hdm_table.item(i, 1).text()
            soluong = self.ui.hdm_table.item(i, 2).text()
            thanhtien = float(dongia) * int(soluong)

            cursor.execute(
                "INSERT INTO chitiethoadon(cthd_hdb_id, cthd_s_id, cthd_dongia, cthd_soluong, cthd_thanhtien) VALUES(%s, %s, %s, %s, %s)",
                (hdb_id, s_id, dongia, soluong, thanhtien))
            cursor.execute("SELECT s_soluong FROM sach WHERE s_id = %s", (s_id,))
            rl = cursor.fetchone()
            soluong_ = int(rl[0])

            soluong_ -= int(soluong)
            cursor.execute("UPDATE sach SET s_soluong = %s WHERE s_id = %s", (soluong_, s_id))

        self.conn.commit()
        self.show_info_message()
    def sum(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT kh_sdt_id  FROM khachhang""")
        sdt_ = cursor.fetchall()
        sdt = self.ui.sdt.text()
        row_table = self.ui.hdm_table.rowCount()
        tongtien = float(0)
        for i in range(row_table):
            tien = self.ui.hdm_table.item(i, 1).text()
            sl = self.ui.hdm_table.item(i, 2).text()
            tongtien += (float(tien)*float(sl))
        self.ui.tongtien.setText(f"Tổng tiền: {tongtien} VND")
        for i in sdt_:
            if sdt == i[0]:
                self.kh_id = True
                tongtien = tongtien - (tongtien * 0.05)
                self.ui.tongtien.setText(f"Tổng tiền(-5% hội viên): {tongtien} VND")
                break
            else:
                self.kh_id = False
    def check_phone(self):
        sdt = self.ui.sdt.text()
        if self.is_valid_phone(sdt):
            self.sum()
        return True
    def is_valid_phone(self, sdt):
        pattern = re.compile(
            r'^\+?(\d{1,3})?[-.\s]?(\d{1,4})?[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})$'
        )
        return bool(pattern.match(sdt))


    def show_info_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Thanh toán thành công.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
        self.close()



class hoadonthue(QDialog, Ui_Dialog):
    def __init__(self, cart_data, parent=None, nv_id=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Hóa đơn thuê")
        self.cart_data = cart_data
        self.connect_to_db()
        self.load_hdt()
        self.sum()
        self.kh_id = True
        self.nv_id = nv_id

        self.ui.btn_huy.clicked.connect(lambda: self.close())
        self.ui.btn_thanhtoan.clicked.connect(lambda: self.btn_thanhtoan())
        self.ui.sdt.textChanged.connect(self.check_phone)

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_nhom7_python"
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn = None
    def load_hdt(self):
        self.ui.hdt_table.setRowCount(len(self.cart_data))
        self.ui.hdt_table.setColumnCount(3)
        self.style_table()
        for row_num, item in enumerate(self.cart_data):
            self.ui.hdt_table.setItem(row_num, 0, QTableWidgetItem(item['ten']))
            self.ui.hdt_table.setItem(row_num, 1, QTableWidgetItem("5000.00"))
            self.ui.hdt_table.setItem(row_num, 2, QTableWidgetItem(str(item['qty'])))

    def btn_thanhtoan(self):
        cursor = self.conn.cursor()
        sdt = self.ui.sdt.text()
        ten = self.ui.ten.text()
        email = self.ui.email.text()
        diachi = self.ui.diachi.text()
        ngaythue = self.ui.ngaythue.date().toString("yyyy-MM-dd")
        ngayhh = self.ui.ngayhh.date().toString("yyyy-MM-dd")

        if not sdt or not ten or not email or not diachi:
            QMessageBox.critical(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        tongtien = self.ui.tongtien.text()
        matches = re.findall(r'\d+\.\d+', tongtien)

        if matches:
            num = matches[0]
        else:
            num = 0
        
        self.check_phone()
        if not self.kh_id :
            cursor.execute("INSERT INTO khachhang(kh_sdt_id, kh_ten, kh_email, kh_diachi) VALUES (%s, %s, %s, %s)",
                           (sdt, ten, email, diachi))
            self.conn.commit()

        cursor.execute(
            "INSERT INTO hoadonchothue(hdct_kh_sdt_id, hdct_nv_id, hdct_ngaythue, hdct_ngayhethan, hdct_tongtien, hdct_trangthai) VALUES (%s, %s, %s, %s, %s, '1')",
            (sdt, self.nv_id, ngaythue, ngayhh, num))
        self.conn.commit()

        cursor.execute("SELECT hdct_id FROM hoadonchothue ORDER BY hdct_id DESC LIMIT 1")
        id = cursor.fetchone()
        hdct_id = id[0]
        row_table = self.ui.hdt_table.rowCount()

        id_list = [item['id'] for item in self.cart_data]

        for i in range(row_table):
            s_id = id_list[i]
            dongia = self.ui.hdt_table.item(i, 1).text()
            soluong = self.ui.hdt_table.item(i, 2).text()
            thanhtien = float(dongia) * int(soluong)
            cursor.execute(
                "INSERT INTO phieuchothue(pct_hdct_id, pct_s_id, pct_dongia, pct_soluong, pct_thanhtien) VALUES(%s, %s, %s, %s, %s)",
                (hdct_id, s_id, dongia, soluong, thanhtien))

            cursor.execute("SELECT s_soluong FROM sach WHERE s_id = %s", (s_id,))
            rl = cursor.fetchone()
            soluong_ = int(rl[0])

            soluong_ -= int(soluong)
            cursor.execute("UPDATE sach SET s_soluong = %s WHERE s_id = %s", (soluong_, s_id))

        self.conn.commit()
        self.show_info_message()

    def sum(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT kh_sdt_id  FROM khachhang""")
        sdt_ = cursor.fetchall()
        sdt = self.ui.sdt.text()

        date_str = datetime.now().strftime("%d-%m-%Y")
        day, month, year = map(int, date_str.split('-'))
        date_qt = QDate(year, month, day)
        self.ui.ngaythue.setDate(date_qt)
        self.ui.ngayhh.setDate(date_qt)
        self.ui.ngaythue.setDisplayFormat("dd-MM-yyyy")
        self.ui.ngayhh.setDisplayFormat("dd-MM-yyyy")

        row_table = self.ui.hdt_table.rowCount()
        tongtien = float(0)
        for i in range(row_table):
            tien = self.ui.hdt_table.item(i, 1).text()
            sl = self.ui.hdt_table.item(i, 2).text()
            tongtien += (float(tien)*float(sl))
        self.ui.tongtien.setText(f"Tổng tiền: {tongtien} VND")
        for i in sdt_:
            if sdt == i[0]:
                self.kh_id = True
                tongtien = tongtien - (tongtien*0.05)
                self.ui.tongtien.setText(f"Tổng tiền(-5% hội viên): {tongtien} VND")
                cursor.execute("SELECT kh_ten, kh_email, kh_diachi FROM khachhang WHERE kh_sdt_id = %s", (sdt,))
                rl = cursor.fetchall()
                self.ui.ten.setText(rl[0][0])
                self.ui.email.setText(rl[0][1])
                self.ui.diachi.setText(rl[0][2])
                break
            else:
                self.kh_id = False
    def check_phone(self):
        sdt = self.ui.sdt.text()
        if self.is_valid_phone(sdt):
            self.sum()
        return True
    def is_valid_phone(self, sdt):
        pattern = re.compile(
            r'^\+?(\d{1,3})?[-.\s]?(\d{1,4})?[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})$'
        )
        return bool(pattern.match(sdt))

    def style_table(self):
        self.ui.hdt_table.setColumnWidth(0, 500)
        self.ui.hdt_table.setColumnWidth(1, 250)
        self.ui.hdt_table.setColumnWidth(2, 30)

    def show_info_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Thanh toán thành công.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
        self.close()
class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
