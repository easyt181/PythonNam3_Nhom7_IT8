# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QHeaderView, QHBoxLayout, QWidget, QDialog
from PySide6.QtGui import QIcon
import mysql.connector
from qlnhanvien.qlnv import Ui_nhanvienmain, Ui_them, Ui_SuaNhanVien
import re


class QLNV(QMainWindow, Ui_nhanvienmain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý Nhân Viên")

        # Kết nối nút "Thêm Nhân Viên" với hàm xử lý sự kiện
        self.btnThemNhanVien.clicked.connect(self.themNhanVien)
        # Kết nối nút "Tìm kiếm" với hàm xử lý sự kiện
        self.btnSearch.clicked.connect(self.timKiemNhanVien)

        # Tải dữ liệu vào tableWidget
        self.load_nhanvien_data()

    def connect_to_database(self):
        # Kết nối đến cơ sở dữ liệu
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_nhom7_python'
        )
        return connection

    def themNhanVien(self):
        # Tạo đối tượng QDialog cho Ui_them
        self.dialog_them = QDialog(self)
        self.dialog_them.setWindowTitle("Thêm Nhân Viên")  # Đặt tiêu đề của dialog thành "Thêm Nhân Viên"
        self.ui_them = Ui_them()
        self.ui_them.setupUi(self.dialog_them)

        # Kết nối nút "Thêm" và "Cancel" với các hàm xử lý sự kiện
        self.ui_them.btnThem.clicked.connect(self.add_nhanvien)
        self.ui_them.btnCancel.clicked.connect(self.dialog_them.reject)

        # Kết nối sự kiện khi nhập vào txtEmail để tự động cập nhật txtTaiKhoan
        self.ui_them.txtEmail.textChanged.connect(self.update_tai_khoan_and_password)

        # Hiển thị dialog để thêm nhân viên
        self.dialog_them.exec()

    def update_tai_khoan_and_password(self):
        email = self.ui_them.txtEmail.text()
        # Cập nhật txtTaiKhoan với giá trị bằng email và txtMatKhau với "1234"
        self.ui_them.txtTaiKhoan.setText(email)
        self.ui_them.txtMatKhau.setText("1234")

    def validate_email(self, email):
        # Check if email ends with @gmail.com
        if not re.match(r"[^@]+@gmail\.com$", email):
            QMessageBox.warning(self, "Cảnh Báo", "Email phải có đuôi @gmail.com")
            return False
        return True

    def validate_phone(self, phone):
        # Check if phone number is 10 digits and starts with 0
        if not re.match(r"^0\d{9}$", phone):
            QMessageBox.warning(self, "Cảnh Báo", "Số điện thoại phải đủ 10 số và bắt đầu bằng số 0")
            return False
        return True

    def validate_input_fields(self, ten_nv, sdt, email, dia_chi, luong, tai_khoan, mat_khau):
        if not ten_nv:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập tên nhân viên.")
            return False
        if not sdt:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập số điện thoại.")
            return False
        if not dia_chi:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập địa chỉ.")
            return False
        if not luong:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập lương.")
            return False
        if not tai_khoan:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập tài khoản.")
            return False
        if not mat_khau:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập mật khẩu.")
            return False
        return True

    def add_nhanvien(self):
        ten_nv = self.ui_them.txtTenNv.text()
        gioi_tinh = self.ui_them.boxGioiTinh.currentText()
        ngay_sinh = self.ui_them.BoxNgaySinh.date().toString("yyyy-MM-dd")
        sdt = self.ui_them.txtSdt.text()
        email = self.ui_them.txtEmail.text()
        dia_chi = self.ui_them.txtDiaChi.text()
        luong = self.ui_them.txtLuong.text()
        tai_khoan = self.ui_them.txtTaiKhoan.text()
        mat_khau = self.ui_them.txtMatKhau.text()

        if not self.validate_input_fields(ten_nv, sdt, email, dia_chi, luong, tai_khoan, mat_khau):
            return

        if not self.validate_email(email) or not self.validate_phone(sdt):
            return

        connection = self.connect_to_database()
        cursor = connection.cursor()
        try:
            # Thực hiện thêm tài khoản vào cơ sở dữ liệu
            query_taikhoan = (
                "INSERT INTO taikhoan (tk_username, tk_password, tk_role) "
                "VALUES (%s, %s, 'nhanvien')"
            )
            cursor.execute(query_taikhoan, (tai_khoan, mat_khau))
            tk_id = cursor.lastrowid  # Lấy ID của tài khoản vừa thêm

            # Thực hiện thêm nhân viên vào cơ sở dữ liệu
            query_nhanvien = (
                "INSERT INTO nhanvien (nv_tk_id, nv_ten, nv_gioitinh, nv_ngaysinh, nv_sdt, nv_email, nv_diachi, nv_luong) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            cursor.execute(query_nhanvien, (tk_id, ten_nv, gioi_tinh, ngay_sinh, sdt, email, dia_chi, luong))

            # Lưu thay đổi vào cơ sở dữ liệu
            connection.commit()
            QMessageBox.information(self, "Thành Công", "Nhân viên đã được thêm thành công!")
            self.dialog_them.accept()
            self.load_nhanvien_data()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def timKiemNhanVien(self):
        # Hàm xử lý tìm kiếm nhân viên
        timKiem = self.lineEdit.text()  # Đổi từ txtSearch thành lineEdit để phù hợp với tên trong Ui_nhanvienmain
        self.load_nhanvien_data(timKiem)  # Cập nhật dữ liệu bảng dựa trên từ khóa tìm kiếm

    def load_nhanvien_data(self, timKiem=""):
        connection = self.connect_to_database()
        cursor = connection.cursor()

        # Nếu có từ khóa tìm kiếm, thêm điều kiện vào câu lệnh SQL
        if timKiem:
            query = (
                "SELECT nv_id, nv_tk_id, nv_ten, nv_gioitinh, nv_ngaysinh, nv_sdt, nv_email, nv_diachi, nv_luong "
                "FROM nhanvien "
                "WHERE nv_id LIKE %s OR nv_tk_id LIKE %s OR nv_ten LIKE %s OR nv_gioitinh LIKE %s OR nv_ngaysinh LIKE %s OR "
                "nv_sdt LIKE %s OR nv_email LIKE %s OR nv_diachi LIKE %s OR nv_luong LIKE %s"
            )
            params = (
                f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%",
                f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%", f"%{timKiem}%"
            )
        else:
            query = (
                "SELECT nv_id, nv_tk_id, nv_ten, nv_gioitinh, nv_ngaysinh, nv_sdt, nv_email, nv_diachi, nv_luong "
                "FROM nhanvien"
            )
            params = ()

        try:
            cursor.execute(query, params)
            nhanviens = cursor.fetchall()
            if not nhanviens:  # Nếu không có kết quả tìm kiếm, tải lại tất cả dữ liệu
                cursor.execute(
                    "SELECT nv_id, nv_tk_id, nv_ten, nv_gioitinh, nv_ngaysinh, nv_sdt, nv_email, nv_diachi, nv_luong "
                    "FROM nhanvien"
                )
                nhanviens = cursor.fetchall()

            self.tableWidget.setRowCount(0)  # Xóa tất cả các hàng hiện tại trong tableWidget
            self.tableWidget.setColumnCount(10)  # Số cột là 10, bao gồm cả nv_tk_id

            # Thêm các hàng vào tableWidget
            for row_number, row_data in enumerate(nhanviens):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa dữ liệu trong ô
                    self.tableWidget.setItem(row_number, column_number, item)

                # Thêm nút Sửa và Xóa vào cột thứ 9 (cột hành động)
                edit_button = QPushButton("Sửa")
                delete_button = QPushButton("Xóa")

                # Kết nối nút Sửa và Xóa với các hàm xử lý sự kiện tương ứng
                edit_button.clicked.connect(lambda _, row=row_number: self.sua_nhanvien(row))
                delete_button.clicked.connect(lambda _, row=row_number: self.xoa_nhanvien(row))

                button_widget = QWidget()
                button_layout = QHBoxLayout(button_widget)
                button_layout.addWidget(edit_button)
                button_layout.addWidget(delete_button)
                button_layout.setContentsMargins(5, 2, 5, 2)
                self.tableWidget.setCellWidget(row_number, 9, button_widget)

            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "Tài Khoản", "Tên Nhân Viên", "Giới Tính", "Ngày Sinh", "SĐT", "Email", "Địa Chỉ", "Lương", "Hành Động"])

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")
        finally:
            cursor.close()
            connection.close()

    def sua_nhanvien(self, row):
        nv_id_item = self.tableWidget.item(row, 0)
        if nv_id_item:
            nv_id = nv_id_item.text()

            connection = self.connect_to_database()
            cursor = connection.cursor()

            query = (
                "SELECT nv_id, nv_tk_id, nv_ten, nv_gioitinh, nv_ngaysinh, nv_sdt, nv_email, nv_diachi, nv_luong, tk_username, tk_password, tk_role "
                "FROM nhanvien "
                "JOIN taikhoan ON nhanvien.nv_tk_id = taikhoan.tk_id "
                "WHERE nv_id = %s"
            )
            cursor.execute(query, (nv_id,))
            nhanvien = cursor.fetchone()

            if nhanvien:
                self.dialog_sua = QDialog(self)
                self.dialog_sua.setWindowTitle("Cập Nhật Nhân Viên")
                self.ui_sua = Ui_SuaNhanVien()
                self.ui_sua.setupUi(self.dialog_sua)

                # Điền thông tin nhân viên vào form sửa và đặt chế độ chỉ đọc cho các trường không được phép sửa
                self.ui_sua.txtIdnv.setText(str(nhanvien[0]))
                self.ui_sua.txtIdnv.setReadOnly(True)  # Đặt chế độ chỉ đọc cho nv_id
                self.ui_sua.txtidtknv.setText(str(nhanvien[1]))
                self.ui_sua.txtidtknv.setReadOnly(True)  # Đặt chế độ chỉ đọc cho nv_tk_id
                self.ui_sua.txtcnTenNv.setText(str(nhanvien[2]))
                self.ui_sua.boxcnGioiTinh.setCurrentText(str(nhanvien[3]))
                self.ui_sua.BoxcnNgaySinh.setDate(QDate.fromString(str(nhanvien[4]), "yyyy-MM-dd"))
                self.ui_sua.txtcnSdt.setText(str(nhanvien[5]))
                self.ui_sua.txtcnEmail.setText(str(nhanvien[6]))
                self.ui_sua.txtcnDiaChi.setText(str(nhanvien[7]))
                self.ui_sua.txtcnLuong.setText(str(nhanvien[8]))
                self.ui_sua.txtcnTaiKhoan.setText(str(nhanvien[9]))
                self.ui_sua.txtcnMatKhau.setText(str(nhanvien[10]))
                self.ui_sua.txtrole.setText(str(nhanvien[11]))
                self.ui_sua.txtrole.setReadOnly(True)  # Đặt chế độ chỉ đọc cho tk_role

                # Kết nối sự kiện click của nút Sửa với hàm update_nhanvien
                self.ui_sua.btnSua.clicked.connect(lambda: self.update_nhanvien(nv_id))

                # Kết nối sự kiện click của nút Cancel để đóng dialog
                self.ui_sua.btnCancel.clicked.connect(self.dialog_sua.reject)

                self.dialog_sua.exec()

            cursor.close()
            connection.close()

    def update_nhanvien(self, nv_id):
        ten_nv = self.ui_sua.txtcnTenNv.text()
        gioi_tinh = self.ui_sua.boxcnGioiTinh.currentText()
        ngay_sinh = self.ui_sua.BoxcnNgaySinh.date().toString("yyyy-MM-dd")
        sdt = self.ui_sua.txtcnSdt.text()
        dia_chi = self.ui_sua.txtcnDiaChi.text()
        luong = self.ui_sua.txtcnLuong.text()
        tai_khoan = self.ui_sua.txtcnTaiKhoan.text()
        mat_khau = self.ui_sua.txtcnMatKhau.text()

        if not self.validate_input_fields(ten_nv, sdt, "", dia_chi, luong, tai_khoan, mat_khau):
            return

        if not self.validate_phone(sdt):
            return

        connection = self.connect_to_database()
        cursor = connection.cursor()

        try:
            query_nhanvien = (
                "UPDATE nhanvien SET nv_ten = %s, nv_gioitinh = %s, nv_ngaysinh = %s, nv_sdt = %s, nv_diachi = %s, nv_luong = %s "
                "WHERE nv_id = %s"
            )
            query_taikhoan = (
                "UPDATE taikhoan SET tk_username = %s, tk_password = %s "
                "WHERE tk_id = (SELECT nv_tk_id FROM nhanvien WHERE nv_id = %s)"
            )
            cursor.execute(query_nhanvien, (ten_nv, gioi_tinh, ngay_sinh, sdt, dia_chi, luong, nv_id))
            cursor.execute(query_taikhoan, (tai_khoan, mat_khau, nv_id))

            connection.commit()
            QMessageBox.information(self, "Thành Công", "Nhân viên đã được cập nhật thành công!")
            self.dialog_sua.accept()
            self.load_nhanvien_data()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def xoa_nhanvien(self, row):
        nv_id_item = self.tableWidget.item(row, 0)
        tk_id_item = self.tableWidget.item(row, 1)
        if nv_id_item and tk_id_item:
            nv_id = nv_id_item.text()
            tk_id = tk_id_item.text()

            confirm = QMessageBox.question(self, "Xác Nhận", "Bạn có chắc chắn muốn xóa nhân viên này?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                connection = self.connect_to_database()
                cursor = connection.cursor()
                try:
                    query_nhanvien = "DELETE FROM nhanvien WHERE nv_id = %s"
                    query_taikhoan = "DELETE FROM taikhoan WHERE tk_id = %s"

                    cursor.execute(query_nhanvien, (nv_id,))
                    cursor.execute(query_taikhoan, (tk_id,))

                    connection.commit()
                    QMessageBox.information(self, "Thành Công", "Nhân viên đã được xóa thành công!")
                    self.load_nhanvien_data()
                except mysql.connector.Error as err:
                    QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")
                    connection.rollback()
                finally:
                    cursor.close()
                    connection.close()


if __name__ == "__main__":
    app = QApplication([])
    window = QLNV()
    window.show()
    app.exec()