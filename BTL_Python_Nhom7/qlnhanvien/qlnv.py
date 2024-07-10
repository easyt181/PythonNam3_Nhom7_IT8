# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlnv.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QStatusBar,
                               QTableWidget, QTableWidgetItem, QToolBar, QWidget, QHBoxLayout, QVBoxLayout, QComboBox,
                               QDateEdit, QLayout)


class Ui_nhanvienmain(object):
    def setupUi(self, nhanvienmain):
        if not nhanvienmain.objectName():
            nhanvienmain.setObjectName(u"nhanvienmain")
        nhanvienmain.resize(1141, 758)
        self.centralwidget = QWidget(nhanvienmain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnThemNhanVien = QPushButton(self.centralwidget)
        self.btnThemNhanVien.setObjectName(u"btnThemNhanVien")
        self.btnThemNhanVien.setGeometry(QRect(10, 70, 201, 45))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(14)
        font.setBold(True)
        self.btnThemNhanVien.setFont(font)
        self.btnThemNhanVien.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.lbNametk = QLabel(self.centralwidget)
        self.lbNametk.setObjectName(u"lbNametk")
        self.lbNametk.setGeometry(QRect(500, 10, 258, 40))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbNametk.setFont(font1)
        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(980, 70, 130, 45))
        self.btnSearch.setMaximumSize(QSize(130, 45))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        self.btnSearch.setFont(font2)
        self.btnSearch.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 170, 255)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/research.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QSize(25, 25))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(420, 70, 521, 45))
        self.lineEdit.setMaximumSize(QSize(16777215, 45))
        self.lineEdit.setStyleSheet(u"")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 150, 1141, 581))
        self.tableWidget.setMaximumSize(QSize(1141, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(10)
        self.tableWidget.setFont(font3)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(114)
        nhanvienmain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(nhanvienmain)
        self.statusbar.setObjectName(u"statusbar")
        nhanvienmain.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(nhanvienmain)
        self.toolBar.setObjectName(u"toolBar")
        nhanvienmain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(nhanvienmain)

        QMetaObject.connectSlotsByName(nhanvienmain)
    # setupUi

    def retranslateUi(self, nhanvienmain):
        nhanvienmain.setWindowTitle(QCoreApplication.translate("nhanvienmain", u"MainWindow", None))
        self.btnThemNhanVien.setText(QCoreApplication.translate("nhanvienmain", u"Th\u00eam Nh\u00e2n Vi\u00ean", None))
        self.lbNametk.setText(QCoreApplication.translate("nhanvienmain", u"Qu\u1ea3n L\u00fd Nh\u00e2n Vi\u00ean", None))
        self.btnSearch.setText(QCoreApplication.translate("nhanvienmain", u"T\u00ecm ki\u1ebfm", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("nhanvienmain", u"Search here...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("nhanvienmain", u"ID NH\u00c2N VI\u00caN", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("nhanvienmain", u"ID TK NH\u00c2N VI\u00caN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("nhanvienmain", u"T\u00caN NH\u00c2N VI\u00caN", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("nhanvienmain", u"GI\u1edaI T\u00cdNH", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("nhanvienmain", u"NG\u00c0Y SINH", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("nhanvienmain", u"S\u1ed0 \u0110I\u1ec6N THO\u1ea0I", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("nhanvienmain", u"EMAIL", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("nhanvienmain", u"\u0110\u1ecaA CH\u1ec8", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("nhanvienmain", u"L\u01af\u01a0NG", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("nhanvienmain", u"HO\u1ea0T \u0110\u1ed8NG", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("nhanvienmain", u"toolBar", None))
    # retranslateUi


class Ui_them(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(807, 653)
        self.lbNametk2 = QLabel(Dialog)
        self.lbNametk2.setObjectName(u"lbNametk2")
        self.lbNametk2.setGeometry(QRect(10, 0, 231, 51))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbNametk2.setFont(font)
        self.txtSdt = QLineEdit(Dialog)
        self.txtSdt.setObjectName(u"txtSdt")
        self.txtSdt.setGeometry(QRect(10, 255, 759, 35))
        self.txtSdt.setMinimumSize(QSize(0, 35))
        self.txtSdt.setMaximumSize(QSize(16777215, 35))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 220, 759, 28))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 295, 759, 28))
        self.label_5.setFont(font1)
        self.txtEmail = QLineEdit(Dialog)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(10, 330, 759, 35))
        self.txtEmail.setMinimumSize(QSize(0, 35))
        self.txtEmail.setMaximumSize(QSize(16777215, 35))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 370, 759, 28))
        self.label_6.setFont(font1)
        self.txtDiaChi = QLineEdit(Dialog)
        self.txtDiaChi.setObjectName(u"txtDiaChi")
        self.txtDiaChi.setGeometry(QRect(10, 405, 759, 35))
        self.txtDiaChi.setMinimumSize(QSize(0, 35))
        self.txtDiaChi.setMaximumSize(QSize(16777215, 35))
        self.txtLuong = QLineEdit(Dialog)
        self.txtLuong.setObjectName(u"txtLuong")
        self.txtLuong.setGeometry(QRect(10, 470, 759, 35))
        self.txtLuong.setMinimumSize(QSize(0, 35))
        self.txtLuong.setMaximumSize(QSize(16777215, 35))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 440, 759, 28))
        self.label_7.setFont(font1)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 761, 72))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.txtTenNv = QLineEdit(self.layoutWidget)
        self.txtTenNv.setObjectName(u"txtTenNv")
        self.txtTenNv.setMinimumSize(QSize(0, 35))
        self.txtTenNv.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtTenNv)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 140, 761, 69))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.boxGioiTinh = QComboBox(self.layoutWidget1)
        self.boxGioiTinh.addItem("")
        self.boxGioiTinh.addItem("")
        self.boxGioiTinh.addItem("")
        self.boxGioiTinh.setObjectName(u"boxGioiTinh")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.boxGioiTinh.setFont(font2)
        self.boxGioiTinh.setMinimumSize(QSize(0, 40))  # Cập nhật kích thước của QComboBox
        self.boxGioiTinh.setMaximumSize(QSize(16777215, 40))  # Cập nhật kích thước của QComboBox

        self.verticalLayout_2.addWidget(self.boxGioiTinh)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.BoxNgaySinh = QDateEdit(self.layoutWidget1)
        self.BoxNgaySinh.setObjectName(u"BoxNgaySinh")
        self.BoxNgaySinh.setFont(font2)
        self.BoxNgaySinh.setMinimumSize(QSize(0, 40))  # Cập nhật kích thước của QDateEdit
        self.BoxNgaySinh.setMaximumSize(QSize(16777215, 40))  # Cập nhật kích thước của QDateEdit

        self.verticalLayout_3.addWidget(self.BoxNgaySinh)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.btnThem = QPushButton(Dialog)
        self.btnThem.setObjectName(u"btnThem")
        self.btnThem.setGeometry(QRect(550, 610, 101, 28))
        self.btnThem.setFont(font1)
        self.btnThem.setStyleSheet(u"QPushButton{\n"
                                   "background-color: #34D481;\n"
                                   "border: none;\n"
                                   "border-radius: 8px;\n"
                                   "font-weight:bold;\n"
                                   "\n"
                                   "}")
        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(670, 610, 101, 28))
        self.btnCancel.setFont(font1)
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
                                     "background-color: rgb(255, 0, 0);\n"
                                     "border: none;\n"
                                     "border-radius: 8px;\n"
                                     "font-weight:bold;\n"
                                     "\n"
                                     "}")
        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 510, 761, 74))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_8)

        self.txtTaiKhoan = QLineEdit(self.layoutWidget2)
        self.txtTaiKhoan.setObjectName(u"txtTaiKhoan")
        self.txtTaiKhoan.setMinimumSize(QSize(0, 35))
        self.txtTaiKhoan.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.txtTaiKhoan)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.txtMatKhau = QLineEdit(self.layoutWidget2)
        self.txtMatKhau.setObjectName(u"txtMatKhau")
        self.txtMatKhau.setMinimumSize(QSize(0, 35))
        self.txtMatKhau.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_5.addWidget(self.txtMatKhau)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbNametk2.setText(QCoreApplication.translate("Dialog", u"Th\u00eam Nh\u00e2n Vi\u00ean", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 \u0110i\u1ec7n Tho\u1ea1i", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0110\u1ecba Ch\u1ec9", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"L\u01b0\u01a1ng", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"T\u00ean Nh\u00e2n Vi\u00ean", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Gi\u1edbi T\u00ednh", None))
        self.boxGioiTinh.setItemText(0, QCoreApplication.translate("Dialog", u"Nam", None))
        self.boxGioiTinh.setItemText(1, QCoreApplication.translate("Dialog", u"N\u1eef", None))
        self.boxGioiTinh.setItemText(2, QCoreApplication.translate("Dialog", u"Khac", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y Sinh", None))
        self.btnThem.setText(QCoreApplication.translate("Dialog", u"Th\u00eam", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"T\u00e0i Kho\u1ea3n", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"M\u1eadt Kh\u1ea9u", None))
    # retranslateUi


class Ui_SuaNhanVien(object):
    def setupUi(self, SuaNhanVien):
        if not SuaNhanVien.objectName():
            SuaNhanVien.setObjectName(u"SuaNhanVien")
        SuaNhanVien.resize(807, 653)
        self.txtcnEmail = QLineEdit(SuaNhanVien)
        self.txtcnEmail.setObjectName(u"txtcnEmail")
        self.txtcnEmail.setGeometry(QRect(10, 360, 759, 35))
        self.txtcnEmail.setMinimumSize(QSize(0, 35))
        self.txtcnEmail.setMaximumSize(QSize(16777215, 35))
        self.layoutWidget = QWidget(SuaNhanVien)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 540, 761, 74))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(14)
        font.setBold(True)
        self.label8.setFont(font)

        self.verticalLayout_4.addWidget(self.label8)

        self.txtcnTaiKhoan = QLineEdit(self.layoutWidget)
        self.txtcnTaiKhoan.setObjectName(u"txtcnTaiKhoan")
        self.txtcnTaiKhoan.setMinimumSize(QSize(0, 35))
        self.txtcnTaiKhoan.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.txtcnTaiKhoan)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label9 = QLabel(self.layoutWidget)
        self.label9.setObjectName(u"label9")
        self.label9.setFont(font)

        self.verticalLayout_5.addWidget(self.label9)

        self.txtcnMatKhau = QLineEdit(self.layoutWidget)
        self.txtcnMatKhau.setObjectName(u"txtcnMatKhau")
        self.txtcnMatKhau.setMinimumSize(QSize(0, 35))
        self.txtcnMatKhau.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_5.addWidget(self.txtcnMatKhau)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.txtcnSdt = QLineEdit(SuaNhanVien)
        self.txtcnSdt.setObjectName(u"txtcnSdt")
        self.txtcnSdt.setGeometry(QRect(10, 300, 759, 35))
        self.txtcnSdt.setMinimumSize(QSize(0, 35))
        self.txtcnSdt.setMaximumSize(QSize(16777215, 35))
        self.label5 = QLabel(SuaNhanVien)
        self.label5.setObjectName(u"label5")
        self.label5.setGeometry(QRect(10, 330, 759, 28))
        self.label5.setFont(font)
        self.layoutWidget_2 = QWidget(SuaNhanVien)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 120, 761, 72))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.txtcnTenNv = QLineEdit(self.layoutWidget_2)
        self.txtcnTenNv.setObjectName(u"txtcnTenNv")
        self.txtcnTenNv.setEnabled(True)
        self.txtcnTenNv.setMinimumSize(QSize(0, 35))
        self.txtcnTenNv.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtcnTenNv)

        self.txtcnLuong = QLineEdit(SuaNhanVien)
        self.txtcnLuong.setObjectName(u"txtcnLuong")
        self.txtcnLuong.setGeometry(QRect(10, 500, 759, 35))
        self.txtcnLuong.setMinimumSize(QSize(0, 35))
        self.txtcnLuong.setMaximumSize(QSize(16777215, 35))
        self.label7 = QLabel(SuaNhanVien)
        self.label7.setObjectName(u"label7")
        self.label7.setGeometry(QRect(10, 470, 759, 28))
        self.label7.setFont(font)
        self.label3 = QLabel(SuaNhanVien)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(10, 270, 759, 28))
        self.label3.setFont(font)
        self.txtcnDiaChi = QLineEdit(SuaNhanVien)
        self.txtcnDiaChi.setObjectName(u"txtcnDiaChi")
        self.txtcnDiaChi.setGeometry(QRect(10, 435, 759, 35))
        self.txtcnDiaChi.setMinimumSize(QSize(0, 35))
        self.txtcnDiaChi.setMaximumSize(QSize(16777215, 35))
        self.lbNametk2 = QLabel(SuaNhanVien)
        self.lbNametk2.setObjectName(u"lbNametk2")
        self.lbNametk2.setGeometry(QRect(10, -10, 231, 51))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbNametk2.setFont(font1)
        self.btnSua = QPushButton(SuaNhanVien)
        self.btnSua.setObjectName(u"btnSua")
        self.btnSua.setGeometry(QRect(550, 620, 101, 28))
        self.btnSua.setFont(font)
        self.btnSua.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.label6 = QLabel(SuaNhanVien)
        self.label6.setObjectName(u"label6")
        self.label6.setGeometry(QRect(10, 400, 759, 28))
        self.label6.setFont(font)
        self.btnCancel = QPushButton(SuaNhanVien)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(670, 620, 101, 28))
        self.btnCancel.setFont(font)
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.layoutWidget1 = QWidget(SuaNhanVien)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 202, 761, 69))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label2 = QLabel(self.layoutWidget1)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)

        self.verticalLayout_2.addWidget(self.label2)

        self.boxcnGioiTinh = QComboBox(self.layoutWidget1)
        self.boxcnGioiTinh.addItem("")
        self.boxcnGioiTinh.addItem("")
        self.boxcnGioiTinh.addItem("")
        self.boxcnGioiTinh.setObjectName(u"boxcnGioiTinh")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.boxcnGioiTinh.setFont(font2)

        self.verticalLayout_2.addWidget(self.boxcnGioiTinh)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label4 = QLabel(self.layoutWidget1)
        self.label4.setObjectName(u"label4")
        self.label4.setFont(font)

        self.verticalLayout_3.addWidget(self.label4)

        self.BoxcnNgaySinh = QDateEdit(self.layoutWidget1)
        self.BoxcnNgaySinh.setObjectName(u"BoxcnNgaySinh")
        self.BoxcnNgaySinh.setFont(font2)

        self.verticalLayout_3.addWidget(self.BoxcnNgaySinh)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.layoutWidget2 = QWidget(SuaNhanVien)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(11, 40, 761, 74))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_6.addWidget(self.label_2)

        self.txtIdnv = QLineEdit(self.layoutWidget2)
        self.txtIdnv.setObjectName(u"txtIdnv")
        self.txtIdnv.setEnabled(True)
        self.txtIdnv.setMinimumSize(QSize(0, 35))
        self.txtIdnv.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_6.addWidget(self.txtIdnv)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.txtrole = QLineEdit(self.layoutWidget2)
        self.txtrole.setObjectName(u"txtrole")
        self.txtrole.setEnabled(True)
        self.txtrole.setMinimumSize(QSize(0, 35))
        self.txtrole.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_8.addWidget(self.txtrole)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.txtidtknv = QLineEdit(self.layoutWidget2)
        self.txtidtknv.setObjectName(u"txtidtknv")
        self.txtidtknv.setEnabled(True)
        self.txtidtknv.setMinimumSize(QSize(0, 35))
        self.txtidtknv.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.txtidtknv)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.retranslateUi(SuaNhanVien)

        QMetaObject.connectSlotsByName(SuaNhanVien)
    # setupUi

    def retranslateUi(self, SuaNhanVien):
        SuaNhanVien.setWindowTitle(QCoreApplication.translate("SuaNhanVien", u"Dialog", None))
        self.label8.setText(QCoreApplication.translate("SuaNhanVien", u"T\u00e0i Kho\u1ea3n", None))
        self.label9.setText(QCoreApplication.translate("SuaNhanVien", u"M\u1eadt Kh\u1ea9u", None))
        self.label5.setText(QCoreApplication.translate("SuaNhanVien", u"Email", None))
        self.label.setText(QCoreApplication.translate("SuaNhanVien", u"T\u00ean Nh\u00e2n Vi\u00ean", None))
        self.label7.setText(QCoreApplication.translate("SuaNhanVien", u"L\u01b0\u01a1ng", None))
        self.label3.setText(QCoreApplication.translate("SuaNhanVien", u"S\u1ed1 \u0110i\u1ec7n Tho\u1ea1i", None))
        self.lbNametk2.setText(QCoreApplication.translate("SuaNhanVien", u"S\u1eeda Nh\u00e2n Vi\u00ean", None))
        self.btnSua.setText(QCoreApplication.translate("SuaNhanVien", u"S\u1eeda", None))
        self.label6.setText(QCoreApplication.translate("SuaNhanVien", u"\u0110\u1ecba Ch\u1ec9", None))
        self.btnCancel.setText(QCoreApplication.translate("SuaNhanVien", u"Cancel", None))
        self.label2.setText(QCoreApplication.translate("SuaNhanVien", u"Gi\u1edbi T\u00ednh", None))
        self.boxcnGioiTinh.setItemText(0, QCoreApplication.translate("SuaNhanVien", u"Nam", None))
        self.boxcnGioiTinh.setItemText(1, QCoreApplication.translate("SuaNhanVien", u"N\u1eef", None))
        self.boxcnGioiTinh.setItemText(2, QCoreApplication.translate("SuaNhanVien", u"Khac", None))

        self.label4.setText(QCoreApplication.translate("SuaNhanVien", u"Ng\u00e0y Sinh", None))
        self.label_2.setText(QCoreApplication.translate("SuaNhanVien", u"ID Nh\u00e2n Vi\u00ean", None))
        self.label_4.setText(QCoreApplication.translate("SuaNhanVien", u"Role", None))
        self.label_3.setText(QCoreApplication.translate("SuaNhanVien", u"ID TK Nh\u00e2n Vi\u00ean", None))
    # retranslateUi
