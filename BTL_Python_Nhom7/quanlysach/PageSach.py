from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *  
from quanlysach.qlsach_ui import Ui_qlsach
from quanlysach.qlsach_themsach_ui import Ui_qlsach_themsach
from quanlysach.qlsach_suasach_ui import Ui_qlsach_suasach
import mysql.connector

class QLSach(QMainWindow, Ui_qlsach):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý sách")
        self.create_connection() 
        self.btnThemSach.clicked.connect(self.them_sach_form)
        self.btnLamMoi.clicked.connect(self.refreshAll)
        self.btnTimKiemSach.clicked.connect(self.tim_kiem)
        self.setupTable()
        self.them_du_lieu_vao_table()
        self.cbbTimKiemTheLoaiSach.currentIndexChanged.connect(self.tim_kiem_theo_loai)
        self.cbbTimKiemNXB.currentIndexChanged.connect(self.tim_kiem_theo_nxb)
    
    def create_connection(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',       
            password='',   
            database='db_nhom7_python'
        )
        self.cursor = self.mydb.cursor()

    def them_sach_form(self):  
        dialog = QLSach_themsach(self.cursor)
        dialog.sach_moi_da_them.connect(self.them_du_lieu_vao_table)
        dialog.exec()

    def edit_item(self, row):
        row_data = [
            self.tableSach.item(row, 0).text(),
            self.tableSach.item(row, 1).text(),
            self.tableSach.item(row, 2).text(),
            self.tableSach.item(row, 3).text(),
            self.tableSach.item(row, 4).text()
        ]
        self.sua_sach_form(row_data)

    def sua_sach_form(self, row_data):
        dialog = QLSach_suasach(self.cursor, row_data)
        dialog.sach_moi_da_them.connect(self.them_du_lieu_vao_table)
        dialog.exec()
    

    def setupTable(self):
        self.tableSach.setColumnCount(8)
        self.tableSach.setHorizontalHeaderLabels(["Mã sách", "Tên sách",
                                                "Thể loại sách", "Nhà xuất bản", "Giá bán lẻ", "Số lượng tồn kho", "Trạng thái", "Hành động"])

        self.tableSach.setRowHeight(0, 40)
        self.tableSach.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableSach.verticalHeader().setVisible(False)
        self.tableSach.setColumnWidth(0, 100)
        self.tableSach.setColumnWidth(1, 200)
        self.tableSach.setColumnWidth(2, 180)
        self.tableSach.setColumnWidth(3, 182)
        self.tableSach.setColumnWidth(4, 107)
        self.tableSach.setColumnWidth(5, 110)
        self.tableSach.setColumnWidth(6, 100)
        self.tableSach.setColumnWidth(7, 115)
    
    def tim_kiem(self):
        text = self.txtTimKiemSach.text().strip()
        if text == "":
            self.them_du_lieu_vao_table()
        else:
            query = "SELECT * FROM sach WHERE s_id LIKE %s OR s_tensach LIKE %s OR s_theloaisach LIKE %s OR s_nhaxuatban LIKE %s "
            self.cursor.execute(query, ('%' + text + '%', '%' + text + '%', '%' + text + '%', '%' + text + '%'))
            du_lieu = self.cursor.fetchall()
            self.cap_nhat_table(du_lieu)

    def tim_kiem_theo_loai(self):
        theLoaiSach = self.cbbTimKiemTheLoaiSach.currentText()
        query = "SELECT * FROM sach"
        
        if theLoaiSach != "Thể loại sách":
            query += f" WHERE s_theloaisach = '{theLoaiSach}'"
            self.cursor.execute(query)
            du_lieu = self.cursor.fetchall()
            self.cap_nhat_table(du_lieu)
        else:
            self.them_du_lieu_vao_table()  

    def tim_kiem_theo_nxb(self):
        nxb = self.cbbTimKiemNXB.currentText()
        query = "SELECT * FROM sach"
        
        if nxb != "Nhà xuất bản":
            query += f" WHERE s_nhaxuatban = '{nxb}'"
            self.cursor.execute(query)
            du_lieu = self.cursor.fetchall()
            self.cap_nhat_table(du_lieu)
        else:
            self.them_du_lieu_vao_table()  
 
    def cap_nhat_table(self, data):
        self.tableSach.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                if col == 5:
                    item.setTextAlignment(Qt.AlignCenter)
                elif col == 6:
                    if value == 1:
                        item.setText("Còn hàng")
                    else:
                        item.setText("Tạm hết hàng")
                self.tableSach.setItem(row, col, item)
            
            self.tableSach.setRowHeight(row, 40)
            btn_edit = QToolButton()
            btn_edit.setIcon(QIcon("icons/editLS.png"))
            btn_edit.setIconSize(QSize(25, 25))
            btn_edit.setFixedSize(25, 25)
            btn_edit.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
            btn_edit.clicked.connect(lambda _, row=row: self.edit_item(row))

            btn_delete = QToolButton()
            btn_delete.setIcon(QIcon("icons/deleteLS.png"))
            btn_delete.setIconSize(QSize(25, 25))
            btn_delete.setFixedSize(25, 25)
            btn_delete.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
            btn_delete.clicked.connect(lambda _, row=row: self.delete_item(row))

            action_layout = QHBoxLayout()
            action_layout.addWidget(btn_edit)
            action_layout.addWidget(btn_delete)
            action_widget = QWidget()
            action_widget.setLayout(action_layout)
            self.tableSach.setCellWidget(row, 7, action_widget)

            action_widget.setFixedWidth(115)
            action_widget.setFixedHeight(40)

    def them_du_lieu_vao_table(self):
        try:
            query = "SELECT * FROM sach"
            self.cursor.execute(query)
            du_lieu = self.cursor.fetchall()
            self.tableSach.setRowCount(len(du_lieu))
            for row, data in enumerate(du_lieu):
                for col, value in enumerate(data):
                    item = QTableWidgetItem(str(value))
                    if col == 5:
                        item.setTextAlignment(Qt.AlignCenter)
                    elif col == 6:
                        if value == 1:
                            item.setText("Còn hàng")
                        else:
                            item.setText("Tạm hết hàng")
                    self.tableSach.setItem(row, col, item)
                
                btn_edit = QToolButton()
                btn_edit.setIcon(QIcon("icons/editLS.png"))
                btn_edit.setIconSize(QSize(25, 25))
                btn_edit.setFixedSize(25, 25)
                btn_edit.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
                btn_edit.clicked.connect(lambda _, row=row: self.edit_item(row))

                btn_delete = QToolButton()
                btn_delete.setIcon(QIcon("icons/deleteLS.png"))
                btn_delete.setIconSize(QSize(25, 25))
                btn_delete.setFixedSize(25, 25)
                btn_delete.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
                btn_delete.clicked.connect(lambda _, row=row: self.delete_item(row))

                action_layout = QHBoxLayout()
                action_layout.addWidget(btn_edit)
                action_layout.addWidget(btn_delete)
                action_widget = QWidget()
                action_widget.setLayout(action_layout)
                self.tableSach.setCellWidget(row, 7, action_widget)
                self.tableSach.setRowHeight(row, 40)
                action_widget.setFixedWidth(115)
                action_widget.setFixedHeight(40)

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi truy vấn dữ liệu: {err}")

    def delete_item(self, row):
        maSach = self.tableSach.item(row, 0).text()
        soLuong = int(self.tableSach.item(row, 5).text())
        lay_trang_thai_HDCT ="""SELECT Count(hdct.hdct_trangthai)
                                FROM hoadonchothue hdct  
                                INNER JOIN phieuchothue pct ON pct.pct_hdct_id = hdct.hdct_id 
                                LEFT JOIN sach s ON s.s_id = pct.pct_s_id 
                                WHERE s.s_id = %s AND (hdct.hdct_trangthai = 1 OR hdct.hdct_trangthai = 2);"""

        self.cursor.execute(lay_trang_thai_HDCT, (maSach,))
        trang_thai_HDCT = self.cursor.fetchone()
        if soLuong > 0:
            QMessageBox.warning(self, "Lỗi", "Sách này đang còn tồn kho, không thể xóa")
            return
        if trang_thai_HDCT[0] > 0:
            QMessageBox.warning(self, "Lỗi", "Sách này đang được thuê, không thể xóa")
            return
        else: 
            try:
                confirm_box = QMessageBox()
                confirm_box.setIcon(QMessageBox.Question)
                confirm_box.setWindowTitle("Xác nhận xóa")
                confirm_box.setText("Bạn có chắc chắn muốn xóa sách này?")
                confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                confirm_box.setDefaultButton(QMessageBox.No)
                response = confirm_box.exec() 
                if response == QMessageBox.Yes:
                    query_xoa_sach = "DELETE FROM sach WHERE s_id = %s"
                    self.cursor.execute(query_xoa_sach, (maSach,))
                    self.cursor._connection.commit()
                    self.them_du_lieu_vao_table()
                    QMessageBox.information(self, "Thành công", "Xóa sách thành công")
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa lô sách: {err}")




    def refreshAll(self):
        self.them_du_lieu_vao_table()
        self.cbbTimKiemTheLoaiSach.setCurrentIndex(0)
        self.cbbTimKiemNXB.setCurrentIndex(0)
        self.txtTimKiemSach.clear() 
        

class QLSach_themsach(QDialog, Ui_qlsach_themsach):
    sach_moi_da_them = Signal()
    
    def __init__(self, cursor):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Thêm sách")
        self.cursor = cursor
        self.btnThemSach.clicked.connect(self.them_sach)
        self.btnThoat.clicked.connect(self.close)

    def them_sach(self):
        tensach = self.txtTenSach.text()
        theloai = self.cbbTheLoaiSach.currentText()
        nhaxuatban = self.cbbNhaXuatBan.currentText()
        giabanle = self.txtGiaBanLe.text()
        soluongtonkho = 0
        trangthai = 0
        query_check_ten_sach = "SELECT * FROM sach WHERE s_tensach = %s"
        self.cursor.execute(query_check_ten_sach, (tensach,))
        sach = self.cursor.fetchone()
        if sach:
            QMessageBox.warning(self, "Lỗi", "Tên sách đã tồn tại trong hệ thống. Kiểm tra lại.")
            return
        theloai1 = self.cbbTheLoaiSach.itemText(0)
        theloai2 = self.cbbTheLoaiSach.itemText(1)
        nhaxuatban1 = self.cbbNhaXuatBan.itemText(0)
        nhaxuatban2 = self.cbbNhaXuatBan.itemText(1)
        if tensach == "" or giabanle == "" or theloai == theloai1 or theloai == theloai2 or nhaxuatban == nhaxuatban1 or nhaxuatban == nhaxuatban2:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
        try:
            query = "INSERT INTO sach (s_tensach, s_theloaisach, s_nhaxuatban, s_gia, s_soluong, s_trangthai) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (tensach, theloai, nhaxuatban, giabanle, soluongtonkho, trangthai))
            self.cursor._connection.commit()
            QMessageBox.information(self, "Thành công", "Thêm sách mới thành công")
            self.clearFormThem()
            self.sach_moi_da_them.emit()
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm sách: {err}")

    def clearFormThem(self):
        self.txtTenSach.clear()
        self.txtGiaBanLe.clear()
        self.cbbTheLoaiSach.setCurrentIndex(0)
        self.cbbNhaXuatBan.setCurrentIndex(0)


class QLSach_suasach(QDialog, Ui_qlsach_suasach):
    sach_moi_da_them = Signal()
    def __init__(self, cursor, row_data):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sửa thông tin sách")
        self.cursor = cursor
        self.row_data = row_data
        self.btnSuaSach.clicked.connect(self.suaSach)
        self.btnThoat.clicked.connect(self.close)
        self.load_row_data()
        self.txtMaSach.setReadOnly(True)
        self.txtTenSach.setReadOnly(True)
        self.txtNhaXuatBan.setReadOnly(True)
        self.txtTheLoaiSach.setReadOnly(True)

    def load_row_data(self):
        self.txtMaSach.setText(self.row_data[0])
        self.txtTenSach.setText(self.row_data[1])  
        self.txtTheLoaiSach.setText(self.row_data[2])  
        self.txtNhaXuatBan.setText(self.row_data[3])   
        self.txtGiaBanLe.setText(self.row_data[4])

    def suaSach(self):
        masach = self.txtMaSach.text()
        giabanle = self.txtGiaBanLe.text()
        if giabanle == "":
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
        try:
            query = "UPDATE sach SET s_gia = %s WHERE s_id = %s"
            self.cursor.execute(query, (giabanle, masach))
            self.cursor._connection.commit()
            QMessageBox.information(self, "Thành công", "Sửa giá bán của sách thành công")
            self.sach_moi_da_them.emit()
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi sửa thông tin sách: {err}")  




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QLSach()
    window.show()
    sys.exit(app.exec())

