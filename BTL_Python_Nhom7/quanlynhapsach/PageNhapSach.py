from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *  
from quanlynhapsach.qlnhapsach_ui import Ui_qlnhapsach
from quanlynhapsach.qlnhapsach_themlosach_ui import Ui_qlnhapsach_ThemLoSach
from quanlynhapsach.qlnhapsach_sualosach_ui import Ui_qlnhapsach_SuaLoSach
import mysql.connector

class QLNhapSach(QMainWindow, Ui_qlnhapsach):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý nhập sách")
        self.create_connection() 
        self.btnThemLoSach.clicked.connect(self.them_lo_sach_form)
        self.btnLamMoi.clicked.connect(self.refreshAll)
        self.btnTimKiemLoSach.clicked.connect(self.tim_kiem)
        self.setupTable()
        self.them_du_lieu_vao_table()
        
        self.cbbTimKiemTheLoaiSach.currentIndexChanged.connect(self.tim_kiem_theo_loai)
        self.cbbTimKiemNXB.currentIndexChanged.connect(self.tim_kiem_theo_nxb)

    def setupTable(self):
        self.tableLoSach.setColumnCount(12)
        self.tableLoSach.setHorizontalHeaderLabels(["Mã lô sách", "Mã sách", "Mã NCC", "Tên sách",
                                                    "Thể loại sách", "Nhà xuất bản", "Ngày nhập", "Đơn giá",
                                                    "Số lượng", "Thành tiền", "Giá bán lẻ", "Hành động"])

        self.tableLoSach.setRowHeight(0, 40)
        self.tableLoSach.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableLoSach.verticalHeader().setVisible(False)
        self.tableLoSach.setColumnWidth(0, 70)
        self.tableLoSach.setColumnWidth(1, 60)
        self.tableLoSach.setColumnWidth(2, 60)
        self.tableLoSach.setColumnWidth(3, 150)
        self.tableLoSach.setColumnWidth(4, 112)
        self.tableLoSach.setColumnWidth(5, 120)
        self.tableLoSach.setColumnWidth(6, 90)
        self.tableLoSach.setColumnWidth(7, 90)
        self.tableLoSach.setColumnWidth(8, 60)
        self.tableLoSach.setColumnWidth(9, 90)
        self.tableLoSach.setColumnWidth(10, 90)
        self.tableLoSach.setColumnWidth(11, 115)
        
    def create_connection(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',       
            password='',   
            database='db_nhom7_python'
        )
        self.cursor = self.mydb.cursor()

    def them_lo_sach_form(self):
        dialog = QLNhapSach_ThemLoSach(self.cursor)
        dialog.lo_sach_moi_da_them.connect(self.them_du_lieu_vao_table)    
        dialog.exec()

    def sua_lo_sach_form(self, row_data):
        dialog = QLNhapSach_SuaLoSach(self.cursor, row_data)
        dialog.lo_sach_moi_da_them.connect(self.them_du_lieu_vao_table)   
        dialog.exec()

    def them_du_lieu_vao_table(self):
        try:
            query = "SELECT * FROM losach"
            self.cursor.execute(query)
            du_lieu = self.cursor.fetchall()
            self.tableLoSach.setRowCount(len(du_lieu))

            for row, data in enumerate(du_lieu):
                for col, value in enumerate(data):
                    item = QTableWidgetItem(str(value))
                    if col == 8:
                        item.setTextAlignment(Qt.AlignCenter)
                    self.tableLoSach.setItem(row, col, item)

                btn_edit = QToolButton()
                btn_edit.setIcon(QIcon("icons/editLS.png")) 
                btn_edit.setIconSize(QSize(25,25))
                btn_edit.setFixedSize(25,25)  
                btn_edit.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
                btn_edit.clicked.connect(lambda _, row=row: self.edit_item(row)) 

                btn_delete = QToolButton()
                btn_delete.setIcon(QIcon("icons/deleteLS.png")) 
                btn_delete.setIconSize(QSize(25,25))
                btn_delete.setFixedSize(25,25)  
                btn_delete.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
                btn_delete.clicked.connect(lambda _, row=row: self.delete_item(row)) 

                btn_invoice = QToolButton()
                btn_invoice.setIcon(QIcon("icons/invoiceLS.png")) 
                btn_invoice.setIconSize(QSize(25,25))
                btn_invoice.setFixedSize(25,25)  
                btn_invoice.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
                btn_invoice.clicked.connect(lambda _, row=row: self.export_invoice(row)) 
               
                action_layout = QHBoxLayout()
                action_layout.addWidget(btn_edit)
                action_layout.addWidget(btn_delete)
                action_layout.addWidget(btn_invoice)
                action_widget = QWidget()
                action_widget.setLayout(action_layout)
                self.tableLoSach.setCellWidget(row, 11, action_widget)
                self.tableLoSach.setRowHeight(row, 40)
                action_widget.setFixedWidth(115)
                action_widget.setFixedHeight(40)

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi truy vấn dữ liệu: {err}")

    def edit_item(self, row):
        row_data = [
            self.tableLoSach.item(row, 0).text(),
            self.tableLoSach.item(row, 1).text(),
            self.tableLoSach.item(row, 2).text(),
            self.tableLoSach.item(row, 7).text(),
            self.tableLoSach.item(row, 8).text(),
            self.tableLoSach.item(row, 9).text(),
            self.tableLoSach.item(row, 10).text(),
            self.tableLoSach.item(row, 3).text()
        ]
        self.sua_lo_sach_form(row_data)

    # Xóa lô sách
    def delete_item(self, row):
        try:
            confirm_box = QMessageBox()
            confirm_box.setIcon(QMessageBox.Question)
            confirm_box.setWindowTitle("Xác nhận xóa")
            confirm_box.setText("Bạn có chắc chắn muốn xóa lô sách này?")
            confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_box.setDefaultButton(QMessageBox.No)
            response = confirm_box.exec() 
            if response == QMessageBox.Yes:
                query_delete = "DELETE FROM losach WHERE ls_id = %s"
                query_check_HDN = "SELECT * FROM hoadonnhap WHERE hdn_ls_id = %s" 
                query_update_sach = "UPDATE sach SET s_soluong = s_soluong - %s WHERE s_id = %s"   
                id = self.tableLoSach.item(row, 0).text()
                self.cursor.execute(query_check_HDN, (id,))
                ketQuaCheck = self.cursor.fetchall()
                if ketQuaCheck:
                    QMessageBox.warning(self, "Lỗi", "Không thể xóa lô sách đã được nhập vào hóa đơn!")
                else:
                    self.cursor.execute(query_delete, (id,))
                    self.cursor.execute(query_update_sach, (self.tableLoSach.item(row, 8).text(), self.tableLoSach.item(row, 1).text()))
                    self.cursor._connection.commit()
                    QMessageBox.information(self, "Thành công", "Xóa lô sách thành công!")
                    self.refreshAll()
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa lô sách: {err}")

    def export_invoice(self, row):
        try:
            idLoSach = self.tableLoSach.item(row, 0).text()
            idSach = self.tableLoSach.item(row, 1).text()
            tenSach = self.tableLoSach.item(row, 3).text()
            donGia = self.tableLoSach.item(row, 7).text()
            soLuong = self.tableLoSach.item(row, 8).text()
            thanhTien = self.tableLoSach.item(row, 9).text()
            confirm_box = QMessageBox()
            confirm_box.setIcon(QMessageBox.Question)
            confirm_box.setWindowTitle("Xác nhận xuất hóa đơn nhập")
            confirm_box.setText(f"Xuất hóa đơn nhập cho lô sách này?\n\n "
                                f"- Mã lô sách: {idLoSach}\n"
                                f"- Mã sách: {idSach}\n"
                                f"- Tên sách: {tenSach}\n"
                                f"- Đơn giá: {donGia}\n"
                                f"- Số lượng: {soLuong}\n"
                                f"- Thành tiền: {thanhTien}\n"
                                f"Sau khi thao tác sẽ không thể sửa hoặc xóa lô sách này.")
            confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_box.setDefaultButton(QMessageBox.No)
            response = confirm_box.exec() 
            if response == QMessageBox.Yes:
                query_them_HDN = "INSERT INTO hoadonnhap (hdn_ls_id, hdn_ngayxuat, hdn_dongia, hdn_soluong, hdn_thanhtien) VALUES (%s, %s, %s, %s, %s)"
                values_them_HDN = (idLoSach, QDateTime.currentDateTime().toString(Qt.ISODate), donGia, soLuong, thanhTien)
                self.cursor.execute(query_them_HDN, values_them_HDN)
                self.cursor._connection.commit()
                QMessageBox.information(self, "Thành công", "Xuất hóa đơn nhập thành công!")
            else:
                return
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xuất hóa đơn nhập cho lô sách: {err}")

    def tim_kiem(self):
        text = self.txtTimKiemLoSach.text().strip()
        if text == "":
            self.them_du_lieu_vao_table()
        else:
            query = "SELECT * FROM losach WHERE ls_id LIKE %s OR ls_tensach LIKE %s OR ls_theloaisach LIKE %s OR ls_nhaxuatban LIKE %s OR ls_s_id LIKE %s OR ls_ncc_id LIKE %s"
            self.cursor.execute(query, ('%' + text + '%', '%' + text + '%', '%' + text + '%', '%' + text + '%', '%' + text + '%', '%' + text + '%'))
            du_lieu = self.cursor.fetchall()
            self.cap_nhat_table(du_lieu)

    def tim_kiem_theo_loai(self):
        theLoaiSach = self.cbbTimKiemTheLoaiSach.currentText()
        query = "SELECT * FROM losach"
        
        if theLoaiSach != "Thể loại sách":
            query += f" WHERE ls_theloaisach = '{theLoaiSach}'"
            self.cursor.execute(query)
            du_lieu = self.cursor.fetchall()
            self.cap_nhat_table(du_lieu)
        else:
            self.them_du_lieu_vao_table()  

    def tim_kiem_theo_nxb(self):
        nxb = self.cbbTimKiemNXB.currentText()
        query = "SELECT * FROM losach"
        
        if nxb != "Nhà xuất bản":
            query += f" WHERE ls_nhaxuatban = '{nxb}'"
            self.cursor.execute(query)
            du_lieu = self.cursor.fetchall()
            self.cap_nhat_table(du_lieu)
        else:
            self.them_du_lieu_vao_table()  
          
    def cap_nhat_table(self, data):
        self.tableLoSach.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                if col == 8:
                    item.setTextAlignment(Qt.AlignCenter)
                self.tableLoSach.setItem(row, col, item)
            
            self.tableLoSach.setRowHeight(row, 40)
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

            btn_invoice = QToolButton()
            btn_invoice.setIcon(QIcon("icons/invoiceLS.png"))
            btn_invoice.setIconSize(QSize(25, 25))
            btn_invoice.setFixedSize(25, 25)
            btn_invoice.setStyleSheet("QToolButton {border: 2px solid black; padding: 1px; border-radius: 5px; background-color: white;}")
            btn_invoice.clicked.connect(lambda _, row=row: self.export_invoice(row))

            action_layout = QHBoxLayout()
            action_layout.addWidget(btn_edit)
            action_layout.addWidget(btn_delete)
            action_layout.addWidget(btn_invoice)
            action_widget = QWidget()
            action_widget.setLayout(action_layout)
            self.tableLoSach.setCellWidget(row, 11, action_widget)
        
            action_widget.setFixedWidth(115) 
            action_widget.setFixedHeight(40) 
                
    def refreshAll(self):
        self.them_du_lieu_vao_table()
        self.cbbTimKiemTheLoaiSach.setCurrentIndex(0)
        self.cbbTimKiemNXB.setCurrentIndex(0)
        self.txtTimKiemLoSach.clear() 
        

# Xử lý form thêm lô sách
class QLNhapSach_ThemLoSach(QDialog, Ui_qlnhapsach_ThemLoSach):
    lo_sach_moi_da_them = Signal()
    def __init__(self, cursor):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Thêm lô sách")
        self.cursor = cursor
        self.btnThemLoSach.clicked.connect(self.themLoSach)
        self.btnThoat.clicked.connect(self.close)

        self.completer = QCompleter()
        self.txtChonMaSach.setCompleter(self.completer)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.load_all_sach()
        self.load_all_nhacungcap()
        self.txtChonMaSach.textChanged.connect(self.on_search)
        self.txtSoLuong.textChanged.connect(self.updateThanhTien)
        self.txtDonGia.textChanged.connect(self.updateThanhTien)

    def load_all_sach(self):
        query = "SELECT s_id, s_tensach FROM sach"
        self.cursor.execute(query)
        sach_list = self.cursor.fetchall()

        completions = []
        for sach in sach_list:
            formatted_text = f"{sach[0]} - {sach[1]}"
            completions.append(formatted_text)

        self.completer.setModel(QStringListModel(completions))

    def load_all_nhacungcap(self):
        query = "SELECT ncc_id, ncc_ten FROM nhacungcap"
        self.cursor.execute(query)
        ncc_list = self.cursor.fetchall()

        for ncc in ncc_list:
            formatted_text = f"{ncc[0]} - {ncc[1]}"
            self.cbbChonMaNCC.addItem(formatted_text)

    def on_search(self, text):
        query = "SELECT s_id, s_tensach FROM sach WHERE s_id LIKE %s"
        self.cursor.execute(query, ('%' + text + '%',))
        sach_list = self.cursor.fetchall()

    def updateThanhTien(self):
        try:
            soLuong = float(self.txtSoLuong.text())
            donGia = float(self.txtDonGia.text())
            thanhTien = soLuong * donGia
            self.txtThanhTien.setText(f"{thanhTien:.2f}")
        except ValueError:
            self.txtThanhTien.setText("Không hợp lệ")  

    def themLoSach(self):
        try:
            text = self.txtChonMaSach.text().strip()  
            if not text:
                QMessageBox.warning(self, "Lỗi", "Vui lòng chọn mã sách.")
                return
            idSach = self.txtChonMaSach.text().split()[0]
            idNCC = self.cbbChonMaNCC.currentText().split()[0]
            ngayNhap = QDateTime.currentDateTime().toString(Qt.ISODate)
            soLuong = self.txtSoLuong.text()
            donGia = self.txtDonGia.text()
            thanhTien = self.txtThanhTien.text()
            if thanhTien == "Không hợp lệ":
                QMessageBox.warning(self, "Lỗi", "Giá trị không hợp lệ.")
                return
            giaBanLe = self.txtGiaBanLe.text()
            if giaBanLe < donGia:
                QMessageBox.warning(self, "Lỗi", "Giá bán lẻ không thể nhỏ hơn giá nhập.")
                return
            if giaBanLe == "" or donGia == "" or soLuong == "" or thanhTien == "":
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
                return
            
            queryLayDuLieu = "SELECT s_tensach, s_nhaxuatban, s_theloaisach FROM sach WHERE s_id = %s"
            self.cursor.execute(queryLayDuLieu, (idSach,))
            result = self.cursor.fetchone()
            
            if result:
                tenSach = result[0]
                nhaXuatBan = result[1]
                theLoaiSach = result[2] 

                query = "INSERT INTO losach (ls_s_id, ls_ncc_id, ls_tensach, ls_theloaisach, ls_nhaxuatban, ls_ngaynhap, ls_dongia, ls_soluong, ls_thanhtien, ls_giabanle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (idSach, idNCC, tenSach, theLoaiSach, nhaXuatBan, ngayNhap, donGia, soLuong, thanhTien, giaBanLe)
                self.cursor.execute(query, values)
                self.cursor._connection.commit()

                query_update = "UPDATE sach SET s_soluong = s_soluong + %s, s_gia = %s WHERE s_id = %s"
                values_update = (soLuong, giaBanLe, idSach)
                self.cursor.execute(query_update, values_update)
                self.cursor._connection.commit()
                
                QMessageBox.information(self, "Thông báo", "Thêm lô sách thành công.")
                self.clearFormThem()
                self.lo_sach_moi_da_them.emit()
            else:
                QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin sách. Hãy thêm sách trước.")
                
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm lô sách: {err}")

    def clearFormThem(self):
        self.txtChonMaSach.clear()
        self.cbbChonMaNCC.setCurrentIndex(0)
        self.txtDonGia.clear()
        self.txtSoLuong.clear()
        self.txtThanhTien.clear()
        self.txtGiaBanLe.clear()

# Xử lý form sửa lô sách
class QLNhapSach_SuaLoSach(QDialog, Ui_qlnhapsach_SuaLoSach):
    lo_sach_moi_da_them = Signal()
    def __init__(self, cursor, row_data):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sửa lô sách")
        self.cursor = cursor
        self.row_data = row_data
        self.btnSuaLoSach.clicked.connect(self.suaLoSach)
        self.btnThoat.clicked.connect(self.close)
        self.load_row_data()
        self.txtMaLoSach.setReadOnly(True)
        self.txtChonMaSach.setReadOnly(True)

        self.txtSoLuong.textChanged.connect(self.updateThanhTien)
        self.txtDonGia.textChanged.connect(self.updateThanhTien)
        self.load_all_nhacungcap()

    def load_row_data(self):
        self.txtMaLoSach.setText(self.row_data[0])
        self.txtChonMaSach.setText(self.row_data[1] + " - " + self.row_data[7])  
        self.cbbChonMaNCC.setCurrentText(self.row_data[2])  
        self.txtDonGia.setText(self.row_data[3])  
        self.txtSoLuong.setText(self.row_data[4])  
        self.txtThanhTien.setText(self.row_data[5])  
        self.txtGiaBanLe.setText(self.row_data[6])    
        self.tenSach = self.row_data[7]  
        self.soLuongCu = int(self.row_data[4])

    def load_all_nhacungcap(self):
        query = "SELECT ncc_id, ncc_ten FROM nhacungcap"
        self.cursor.execute(query)
        ncc_list = self.cursor.fetchall()

        for ncc in ncc_list:
            formatted_text = f"{ncc[0]} - {ncc[1]}"
            self.cbbChonMaNCC.addItem(formatted_text)

    def updateThanhTien(self):
        try:
            soLuong = float(self.txtSoLuong.text())
            donGia = float(self.txtDonGia.text())
            thanhTien = soLuong * donGia
            self.txtThanhTien.setText(f"{thanhTien:.2f}")
        except ValueError:
            self.txtThanhTien.setText("Không hợp lệ")

    def suaLoSach(self):
        query_check_HDN = "SELECT * FROM hoadonnhap WHERE hdn_ls_id = %s"
        self.cursor.execute(query_check_HDN, (self.txtMaLoSach.text(),))
        ketQuaCheck = self.cursor.fetchall()
        if ketQuaCheck:
            QMessageBox.warning(self, "Lỗi", "Không thể sửa lô sách đã được xuất hóa đơn nhập!")
            return
        else:
            try:
                idLoSach = self.txtMaLoSach.text()
                idSach = self.txtChonMaSach.text().split()[0]
                idNCC = self.cbbChonMaNCC.currentText().split()[0]
                soLuong = int(self.txtSoLuong.text())
                donGia = self.txtDonGia.text()
                thanhTien = self.txtThanhTien.text()
                if thanhTien == "Không hợp lệ":
                    QMessageBox.warning(self, "Lỗi", "Giá trị không hợp lệ.")
                    return
                giaBanLe = self.txtGiaBanLe.text()
                if giaBanLe < donGia:
                    QMessageBox.warning(self, "Lỗi", "Giá bán lẻ không thể nhỏ hơn giá nhập.")
                    return
                if giaBanLe == "" or donGia == "" or soLuong == "" or thanhTien == "":
                    QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
                    return
                getSoLuongSach = "SELECT s_soluong FROM sach WHERE s_id = %s"
                self.cursor.execute(getSoLuongSach, (idSach,))
                soLuongSach = int(self.cursor.fetchone()[0])
                
                query_update_lo_sach = "UPDATE losach SET  ls_ncc_id = %s, ls_dongia = %s, ls_soluong = %s, ls_thanhtien = %s, ls_giabanle = %s WHERE ls_id = %s"
                values_update_lo_sach = (idNCC, donGia, soLuong, thanhTien, giaBanLe, idLoSach)
                self.cursor.execute(query_update_lo_sach, values_update_lo_sach)

                soLuongMoi = soLuongSach - self.soLuongCu + soLuong
                query_update_sach = "UPDATE sach SET s_soluong = %s, s_gia = %s WHERE s_id = %s"
                values_update_sach = (soLuongMoi, giaBanLe, idSach)
                self.cursor.execute(query_update_sach, values_update_sach)
                self.cursor._connection.commit()
                QMessageBox.information(self, "Thông báo", "Sửa lô sách thành công.")
                self.lo_sach_moi_da_them.emit()   
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi sửa lô sách: {err}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QLNhapSach()
    window.show()
    sys.exit(app.exec())
