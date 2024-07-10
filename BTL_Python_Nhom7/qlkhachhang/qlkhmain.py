import re
import mysql.connector
from PySide6.QtCore import QSortFilterProxyModel, Qt, QModelIndex
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QWidget, \
    QHBoxLayout, QHeaderView, QDialog
from PySide6.QtGui import QIcon
from qlkhachhang.qlkh import Ui_khachhangmain, Ui_ThemKhachHang, Ui_SuaKhachHang

class KhachHangMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_khachhangmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Quản lý Khách Hàng")
        self.ui.btnThemKhachHang.clicked.connect(self.themKhachHang)
        self.ui.btnSearch.clicked.connect(self.timKiemKhachHang)
        self.load_khachhang_data()

    def connect_to_database(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_nhom7_python"
        )
        return connection

    def load_khachhang_data(self, timKiem=""):
        try:
            connection = self.connect_to_database()
            cursor = connection.cursor()

            if timKiem:
                query = (
                    "SELECT STT, kh_sdt_id, kh_ten, kh_gioitinh, kh_ngaysinh, kh_cccd, kh_email, kh_diachi "
                    "FROM khachhang "
                    "WHERE STT LIKE %s OR kh_sdt_id LIKE %s OR kh_ten LIKE %s OR kh_gioitinh LIKE %s OR kh_ngaysinh LIKE %s OR "
                    "kh_cccd LIKE %s OR kh_email LIKE %s OR kh_diachi LIKE %s"
                )
                params = (
                    f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%",
                    f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%"
                )
            else:
                query = (
                    "SELECT STT, kh_sdt_id, kh_ten, kh_gioitinh, kh_ngaysinh, kh_cccd, kh_email, kh_diachi "
                    "FROM khachhang"
                )
                params = ()

            cursor.execute(query, params)
            khachhang_list = cursor.fetchall()
            self.ui.tableKhachHang.setRowCount(0)

            for row_number, row_data in enumerate(khachhang_list):
                self.ui.tableKhachHang.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    if column_number == 0:
                        item.setData(Qt.ItemDataRole.DisplayRole, int(data))
                    self.ui.tableKhachHang.setItem(row_number, column_number, item)

                widget = QWidget()
                layout = QHBoxLayout()
                layout.setContentsMargins(0, 0, 0, 0)

                update_button = QPushButton("Sửa")
                update_button.setIcon(QIcon(":/icons/edit.png"))
                update_button.setToolTip("Update this record")
                update_button.setStyleSheet("background-color: lightblue")
                update_button.setFixedSize(50, 30)
                update_button.clicked.connect(self.create_update_function(row_number))
                layout.addWidget(update_button)

                delete_button = QPushButton("Xóa")
                delete_button.setIcon(QIcon(":/icons/delete.png"))
                delete_button.setToolTip("Delete this record")
                delete_button.setStyleSheet("background-color: lightcoral")
                delete_button.setFixedSize(50, 30)
                delete_button.clicked.connect(self.create_delete_function(row_number))
                layout.addWidget(delete_button)

                widget.setLayout(layout)
                self.ui.tableKhachHang.setCellWidget(row_number, 8, widget)

            headers = ["STT", "SĐT", "Tên Khách Hàng", "Giới Tính", "Ngày Sinh", "CCCD", "Email", "Địa Chỉ",
                       "Hoạt Động"]
            self.ui.tableKhachHang.setHorizontalHeaderLabels(headers)

            header = self.ui.tableKhachHang.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.ui.tableKhachHang.verticalHeader().setVisible(False)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {e}")
        finally:
            cursor.close()
            connection.close()

    def timKiemKhachHang(self):
        timKiem = self.ui.lineEdit.text()
        self.load_khachhang_data(timKiem)

    def themKhachHang(self):
        self.dialog_them = QDialog(self)
        self.dialog_them.setWindowTitle("Thêm Khách Hàng")
        self.ui_them = Ui_ThemKhachHang()
        self.ui_them.setupUi(self.dialog_them)

        self.ui_them.boxGioiTinhKH.setFixedHeight(35)
        self.ui_them.BoxNgaySinhKH.setFixedHeight(35)

        self.ui_them.btnThem.clicked.connect(self.them_khachhang_db)
        self.ui_them.btnCancel.clicked.connect(self.dialog_them.reject)

        self.dialog_them.exec()

    def them_khachhang_db(self):
        sdt_id = self.ui_them.txtSdtKH.text()
        ten = self.ui_them.txtTenKH.text()
        gioi_tinh = self.ui_them.boxGioiTinhKH.currentText()
        ngaysinh = self.ui_them.BoxNgaySinhKH.date().toString("yyyy-MM-dd")
        cccd = self.ui_them.txtCCCD.text()
        email = self.ui_them.txtEmail.text()
        diachi = self.ui_them.txtDiaChi.text()

        if not sdt_id or not ten or not email or not diachi or not cccd:
            QMessageBox.warning(self, "Cảnh Báo", "Vui lòng nhập đầy đủ thông tin khách hàng!")
            return

        if not self.check_email(email):
            QMessageBox.warning(self, "Cảnh Báo", "Email phải có đuôi @gmail.com!")
            return

        if not self.check_phone_number(sdt_id):
            QMessageBox.warning(self, "Cảnh Báo", "Số điện thoại phải đủ 10 số và bắt đầu bằng số 0!")
            return

        if not self.check_cccd(cccd):
            QMessageBox.warning(self, "Cảnh Báo", "CCCD phải có 12 số!")
            return

        connection = self.connect_to_database()
        cursor = connection.cursor()
        try:
            query_khachhang = (
                "INSERT INTO khachhang (kh_sdt_id, kh_ten, kh_gioitinh, kh_ngaysinh, kh_cccd, kh_email, kh_diachi) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )
            cursor.execute(query_khachhang, (sdt_id, ten, gioi_tinh, ngaysinh, cccd, email, diachi))
            connection.commit()

            self.load_khachhang_data()
            QMessageBox.information(self, "Thành Công", "Thêm khách hàng thành công!")
            self.dialog_them.accept()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi thêm khách hàng: {e}")
        finally:
            cursor.close()
            connection.close()

    def suaKhachHang(self, row_number):
        khachhang_data = []
        for column in range(self.ui.tableKhachHang.columnCount() - 1):
            khachhang_data.append(self.ui.tableKhachHang.item(row_number, column).text())

        self.dialog_sua = QDialog(self)
        self.dialog_sua.setWindowTitle("Sửa Thông Tin Khách Hàng")
        self.ui_sua = Ui_SuaKhachHang()
        self.ui_sua.setupUi(self.dialog_sua)

        self.ui_sua.boxcnGioiTinhKH.setFixedHeight(35)
        self.ui_sua.BoxcnNgaySinhKH.setFixedHeight(35)

        self.ui_sua.txtcnSdtKH.setText(khachhang_data[1])
        self.ui_sua.txtcnTenKH.setText(khachhang_data[2])
        self.ui_sua.boxcnGioiTinhKH.setCurrentText(khachhang_data[3])
        self.ui_sua.BoxcnNgaySinhKH.setDate(QDate.fromString(khachhang_data[4], "yyyy-MM-dd"))
        self.ui_sua.txtcnCCCD.setText(khachhang_data[5])
        self.ui_sua.txtcnEmail.setText(khachhang_data[6])
        self.ui_sua.txtcnDiaChi.setText(khachhang_data[7])

        self.ui_sua.btnSua.clicked.connect(lambda: self.sua_khachhang_db(khachhang_data[0]))
        self.ui_sua.btnCancel.clicked.connect(self.dialog_sua.reject)

        self.dialog_sua.exec()

    def sua_khachhang_db(self, kh_stt):
        sdt_id = self.ui_sua.txtcnSdtKH.text()
        ten = self.ui_sua.txtcnTenKH.text()
        gioi_tinh = self.ui_sua.boxcnGioiTinhKH.currentText()
        ngaysinh = self.ui_sua.BoxcnNgaySinhKH.date().toString("yyyy-MM-dd")
        cccd = self.ui_sua.txtcnCCCD.text()
        email = self.ui_sua.txtcnEmail.text()
        diachi = self.ui_sua.txtcnDiaChi.text()

        if not sdt_id or not ten or not email or not diachi or not cccd:
            QMessageBox.warning(self, "Cảnh Báo", "Vui lòng nhập đầy đủ thông tin khách hàng!")
            return

        if not self.check_email(email):
            QMessageBox.warning(self, "Cảnh Báo", "Email phải có đuôi @gmail.com!")
            return

        if not self.check_phone_number(sdt_id):
            QMessageBox.warning(self, "Cảnh Báo", "Số điện thoại phải đủ 10 số và bắt đầu bằng số 0!")
            return

        if not self.check_cccd(cccd):
            QMessageBox.warning(self, "Cảnh Báo", "CCCD phải có 12 số!")
            return

        connection = self.connect_to_database()
        cursor = connection.cursor()
        try:
            query_update = (
                "UPDATE khachhang SET kh_sdt_id=%s, kh_ten=%s, kh_gioitinh=%s, kh_ngaysinh=%s, kh_cccd=%s, kh_email=%s, kh_diachi=%s "
                "WHERE STT=%s"
            )
            cursor.execute(query_update, (sdt_id, ten, gioi_tinh, ngaysinh, cccd, email, diachi, kh_stt))
            connection.commit()

            self.load_khachhang_data()
            QMessageBox.information(self, "Thành Công", "Cập nhật khách hàng thành công!")
            self.dialog_sua.accept()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi cập nhật khách hàng: {e}")
        finally:
            cursor.close()
            connection.close()

    def create_update_function(self, row_number):
        def update():
            self.suaKhachHang(row_number)
        return update

    def create_delete_function(self, row_number):
        def delete():
            sdt_id = self.ui.tableKhachHang.item(row_number, 1).text()
            response = QMessageBox.question(self, "Xác Nhận Xóa", f"Bạn có chắc chắn muốn xóa khách hàng với SĐT {sdt_id}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if response == QMessageBox.Yes:
                connection = self.connect_to_database()
                cursor = connection.cursor()
                try:
                    query_delete = "DELETE FROM khachhang WHERE kh_sdt_id=%s"
                    cursor.execute(query_delete, (sdt_id,))
                    connection.commit()
                    self.load_khachhang_data()
                    QMessageBox.information(self, "Thành Công", "Xóa khách hàng thành công!")
                except mysql.connector.Error as e:
                    QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi xóa khách hàng: {e}")
                finally:
                    cursor.close()
                    connection.close()
        return delete

    def check_email(self, email):
        return re.match(r'^[\w\.-]+@gmail\.com$', email) is not None

    def check_phone_number(self, phone_number):
        return re.match(r'^0\d{9}$', phone_number) is not None

    def check_cccd(self, cccd):
        return re.match(r'^\d{12}$', cccd) is not None

if __name__ == "__main__":
    app = QApplication([])
    window = KhachHangMain()
    window.show()
    app.exec()
