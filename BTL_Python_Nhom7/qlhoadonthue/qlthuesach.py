from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QDate
from PySide6.QtCore import Qt
import sys
from datetime import datetime
import mysql.connector

from qlhoadonthue.ql_hoadonthue_ui import Ui_MainWindow
from qlhoadonthue.chitiettrasach_ui import Ui_chitiet

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, nv_id=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_to_db()
        self.load_data()
        self.nv_id = nv_id

        self.ui.btn_search.clicked.connect(lambda: self.search())

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
            query = "SELECT * FROM hoadonchothue"
            cursor.execute(query)
            rows = cursor.fetchall()
            thue_table = self.ui.thue_table.horizontalHeader()
            thue_table.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
            thue_table.setStretchLastSection(True)
            self.ui.thue_table.setRowCount(len(rows))
            self.ui.thue_table.setColumnCount(len(rows[0]) + 1)
            self.ui.thue_table.setEditTriggers(QTableWidget.NoEditTriggers)
            for row_num, row_data in enumerate(rows):
                for col_num, data in enumerate(row_data):
                    if col_num == 6:
                        if data == 0:
                            display_text = "Đã trả sách"
                        elif data == 1:
                            display_text = "Đang cho thuê"
                        elif data == 2:
                            display_text = "Đã quá hạn trả sách"
                        else:
                            display_text = str(data)
                        self.ui.thue_table.setItem(row_num, col_num, QTableWidgetItem(display_text))
                    else:
                        self.ui.thue_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
                self.add_button(row_num, self.ui.thue_table.item(row_num, 0).text())
                self.style_table(row_num)

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        date_str = datetime.now().strftime("%d-%m-%Y")
        day, month, year = map(int, date_str.split('-'))
        date_qt = QDate(year, month, day)
        self.ui.ngaythue.setDate(date_qt)
        self.ui.ngayhh.setDate(date_qt)
        self.ui.ngaythue.setDisplayFormat("dd-MM-yyyy")
        self.ui.ngayhh.setDisplayFormat("dd-MM-yyyy")

    def add_button(self, row_num, id):
        detail_btn = QPushButton("Chi tiết", self)
        detail_btn.setStyleSheet(
            "Background-color: #00CCCC; color: white; font-weight: bold; font-size: 14px;")
        detail_btn.setFixedSize(75, 31)
        detail_btn.clicked.connect(lambda: self.btn_chitiet(id))

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(detail_btn)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.thue_table.setCellWidget(row_num, self.ui.thue_table.columnCount() - 1, widget)

    def search(self):
        cursor = self.conn.cursor()

        query = "SELECT * FROM hoadonchothue WHERE"

        hdct_id = self.ui.masach.text()
        ngaythue = self.ui.ngaythue.date().toString("yyyy-MM-dd")
        ngayhh = self.ui.ngayhh.date().toString("yyyy-MM-dd")
        trangthai = self.ui.trangthai.currentText()

        conditions = []

        if hdct_id != '':
            conditions.append(f" hdct_id LIKE '%{hdct_id}%'")
        if ngaythue != '':
            conditions.append(f" hdct_ngaythue LIKE '%{ngaythue}%'")
        if ngayhh != '':
            conditions.append(f" hdct_ngayhethan LIKE '%{ngayhh}%'")
        if trangthai != 'Trạng thái':
            trangthai_ = 0
            if trangthai == "Đang cho thuê":
                trangthai_ = 1
            if trangthai == "Đã quá hạn cho thuê":
                trangthai_ = 2

            conditions.append(f" hdct_trangthai LIKE '%{trangthai_}%'")

        if conditions:
            query += ' AND '.join(conditions)

        if query != "SELECT * FROM hoadonchothue WHERE":
            self.ui.thue_table.clearContents()
            self.ui.thue_table.setRowCount(0)
            cursor.execute(query)
            rows = cursor.fetchall()

            self.ui.thue_table.setRowCount(len(rows))

            for row_num, row_data in enumerate(rows):
                for col_num, data in enumerate(row_data):
                    if col_num == 6:
                        if data == 0:
                            display_text = "Đã trả sách"
                        elif data == 1:
                            display_text = "Đang cho thuê"
                        elif data == 2:
                            display_text = "Đã quá hạn trả sách"
                        else:
                            display_text = str(data)
                        self.ui.thue_table.setItem(row_num, col_num, QTableWidgetItem(display_text))
                    else:
                        self.ui.thue_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
                self.add_button(row_num, row_data[0])  # Use the actual ID value here
                self.style_table(row_num)

            cursor.close()
        else:
            self.load_data()

    def btn_chitiet(self, id):
        trasach_dialog = chitiet(id, self)
        result = trasach_dialog.exec()

        if result == QDialog.Rejected:
            self.connect_to_db()
            self.load_data()

    def style_table(self, row_num):
        self.ui.thue_table.setRowHeight(row_num, 35)
        self.ui.thue_table.setColumnWidth(0, 120)
        self.ui.thue_table.setColumnWidth(1, 120)
        self.ui.thue_table.setColumnWidth(2, 120)
        self.ui.thue_table.setColumnWidth(3, 150)
        self.ui.thue_table.setColumnWidth(4, 150)
        self.ui.thue_table.setColumnWidth(5, 150)
        self.ui.thue_table.setColumnWidth(6, 150)

class chitiet(QDialog, Ui_chitiet):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.ui = Ui_chitiet()
        self.ui.setupUi(self)
        self.setWindowTitle("Chi tiết hóa đơn")
        self.data = data
        self.connect_to_db()
        self.load_data()

        self.ui.btn_thue.clicked.connect(lambda : self.close())

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
        id = self.data
        cursor = self.conn.cursor()
        data_tra = []
        cursor.execute(
            "SELECT hdct_kh_sdt_id, hdct_nv_id, hdct_tongtien, hdct_trangthai FROM hoadonchothue WHERE hdct_id = %s",
            (id,))
        rl = cursor.fetchall()

        if rl:
            self.ui.mak.setText(f"Mã khách hàng: {rl[0][0]}")
            self.ui.manv.setText(f"Mã nhân viên: {rl[0][1]}")
            self.ui.tongtien.setText(f"Tổng tiền: {rl[0][2]} VND")

            trangthai = rl[0][3]
            if trangthai == 0:
                self.ui.trangthai.setText("Trang thái: Đã thanh toán")
            elif trangthai == 1:
                self.ui.trangthai.setText("Trang thái: Đang thuê sách")
            elif trangthai == 2:
                self.ui.trangthai.setText("Trang thái: Đã quá thời hạn thuê sách")

        cursor.execute(
            "SELECT pct_s_id, sach.s_tensach,  pct_dongia, pct_soluong, pct_thanhtien FROM phieuchothue INNER JOIN sach ON phieuchothue.pct_s_id = sach.s_id  WHERE pct_hdct_id = %s",
            (id,))
        rl = cursor.fetchall()

        self.ui.table.setRowCount(len(rl))
        self.ui.table.verticalHeader().setVisible(False)
        table = self.ui.table.horizontalHeader()
        table.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        table.setStretchLastSection(True)
        self.ui.table.setEditTriggers(QTableWidget.NoEditTriggers)
        for row_num, row_data in enumerate(rl):
            for col_num, data in enumerate(row_data):
                if col_num == 0:
                    self.ui.table.setItem(row_num, col_num, QTableWidgetItem(id))
                self.ui.table.setItem(row_num, col_num + 1, QTableWidgetItem(str(data)))
            data_tra.append(self.ui.table.item(row_num, 1).text())
            data_tra.append(self.ui.table.item(row_num, 4).text())
            self.style_table(row_num)
        data_tra.append(self.ui.table.item(0, 0).text())
        cursor.execute("SELECT hdct_trangthai FROM hoadonchothue WHERE hdct_id = %s", (id,))
        re = cursor.fetchall()
        if re[0][0] != 0:
            self.ui.btn_thue_2.show()
            self.ui.btn_thue_2.clicked.connect(lambda: self.trasach(data_tra))
        else:
            self.ui.btn_thue_2.hide()

    def trasach(self, data_tra):
        if self.show_message_box():
            cursor = self.conn.cursor()

            for i in range(0, len(data_tra) - 1, 2):
                s_id = data_tra[i]
                soluong_tra = data_tra[i + 1]

                cursor.execute("SELECT s_soluong FROM sach WHERE s_id = %s", (s_id,))
                rl = cursor.fetchall()
                soluong_hientai = int(rl[0][0])
                soluong_moi = soluong_hientai + int(soluong_tra)

                cursor.execute("UPDATE sach SET s_soluong = %s WHERE s_id = %s", (soluong_moi, s_id))

            hdct_id = data_tra[-1]
            cursor.execute("UPDATE hoadonchothue SET hdct_trangthai = 0 WHERE hdct_id = %s", (hdct_id,))
            self.conn.commit()
            self.close()

    def style_table(self, row_num):
        self.ui.table.setRowHeight(row_num, 35)
        self.ui.table.setColumnWidth(0, 90)
        self.ui.table.setColumnWidth(1, 90)
        self.ui.table.setColumnWidth(2, 300)
        self.ui.table.setColumnWidth(3, 90)
        self.ui.table.setColumnWidth(4, 90)
        self.ui.table.setColumnWidth(5, 90)

    def show_message_box(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("Bạn chắc chứ?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

        result = msg_box.exec()

        if result != QMessageBox.StandardButton.Ok:
            return False
        else:
            return True


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())