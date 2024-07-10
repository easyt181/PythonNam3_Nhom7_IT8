# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlkh.ui'
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
                               QTableWidget, QTableWidgetItem, QToolBar, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,
                               QDateEdit)
import new_resource_rc

class Ui_khachhangmain(object):
    def setupUi(self, khachhangmain):
        if not khachhangmain.objectName():
            khachhangmain.setObjectName(u"khachhangmain")
        khachhangmain.resize(1141, 758)
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(12)
        khachhangmain.setFont(font)
        self.centralwidget = QWidget(khachhangmain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnThemKhachHang = QPushButton(self.centralwidget)
        self.btnThemKhachHang.setObjectName(u"btnThemKhachHang")
        self.btnThemKhachHang.setGeometry(QRect(10, 70, 201, 45))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.btnThemKhachHang.setFont(font1)
        self.btnThemKhachHang.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.lbNametk = QLabel(self.centralwidget)
        self.lbNametk.setObjectName(u"lbNametk")
        self.lbNametk.setGeometry(QRect(500, 10, 291, 40))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.lbNametk.setFont(font2)
        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(980, 70, 130, 45))
        self.btnSearch.setMaximumSize(QSize(130, 45))
        self.btnSearch.setFont(font)
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
        self.tableKhachHang = QTableWidget(self.centralwidget)
        if (self.tableKhachHang.columnCount() < 9):
            self.tableKhachHang.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableKhachHang.setObjectName(u"tableKhachHang")
        self.tableKhachHang.setGeometry(QRect(0, 150, 1141, 581))
        self.tableKhachHang.setMaximumSize(QSize(1141, 16777215))
        self.tableKhachHang.setFont(font)
        self.tableKhachHang.horizontalHeader().setMinimumSectionSize(55)
        self.tableKhachHang.horizontalHeader().setDefaultSectionSize(110)
        self.tableKhachHang.verticalHeader().setCascadingSectionResizes(False)
        self.tableKhachHang.verticalHeader().setStretchLastSection(False)
        khachhangmain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(khachhangmain)
        self.statusbar.setObjectName(u"statusbar")
        khachhangmain.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(khachhangmain)
        self.toolBar.setObjectName(u"toolBar")
        khachhangmain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(khachhangmain)

        QMetaObject.connectSlotsByName(khachhangmain)
    # setupUi

    def retranslateUi(self, khachhangmain):
        khachhangmain.setWindowTitle(QCoreApplication.translate("khachhangmain", u"MainWindow", None))
        self.btnThemKhachHang.setText(QCoreApplication.translate("khachhangmain", u"Th\u00eam Kh\u00e1ch H\u00e0ng", None))
        self.lbNametk.setText(QCoreApplication.translate("khachhangmain", u"Qu\u1ea3n L\u00fd Kh\u00e1ch H\u00e0ng", None))
        self.btnSearch.setText(QCoreApplication.translate("khachhangmain", u"T\u00ecm ki\u1ebfm", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("khachhangmain", u"Search here...", None))
        ___qtablewidgetitem = self.tableKhachHang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("khachhangmain", u"STT", None));
        ___qtablewidgetitem1 = self.tableKhachHang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("khachhangmain", u"S\u0110T Kh\u00e1ch H\u00e0ng", None));
        ___qtablewidgetitem2 = self.tableKhachHang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("khachhangmain", u"T\u00ean Kh\u00e1ch H\u00e0ng", None));
        ___qtablewidgetitem3 = self.tableKhachHang.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("khachhangmain", u"Gi\u1edbi T\u00ednh", None));
        ___qtablewidgetitem4 = self.tableKhachHang.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("khachhangmain", u"Ng\u00e0y Sinh", None));
        ___qtablewidgetitem5 = self.tableKhachHang.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("khachhangmain", u"CCCD", None));
        ___qtablewidgetitem6 = self.tableKhachHang.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("khachhangmain", u"Email", None));
        ___qtablewidgetitem7 = self.tableKhachHang.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("khachhangmain", u"\u0110\u1ecba Ch\u1ec9", None));
        ___qtablewidgetitem8 = self.tableKhachHang.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("khachhangmain", u"Ho\u1ea1t \u0110\u1ed9ng", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("khachhangmain", u"toolBar", None))
    # retranslateUi

class Ui_ThemKhachHang(object):
    def setupUi(self, ThemKhachHang):
        if not ThemKhachHang.objectName():
            ThemKhachHang.setObjectName(u"ThemKhachHang")
        ThemKhachHang.resize(807, 599)
        self.lbNametk2 = QLabel(ThemKhachHang)
        self.lbNametk2.setObjectName(u"lbNametk2")
        self.lbNametk2.setGeometry(QRect(10, 0, 271, 51))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbNametk2.setFont(font)
        self.txtTenKH = QLineEdit(ThemKhachHang)
        self.txtTenKH.setObjectName(u"txtTenKH")
        self.txtTenKH.setGeometry(QRect(10, 175, 759, 35))
        self.txtTenKH.setMinimumSize(QSize(0, 35))
        self.txtTenKH.setMaximumSize(QSize(16777215, 35))
        self.label_3 = QLabel(ThemKhachHang)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 759, 28))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_5 = QLabel(ThemKhachHang)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 375, 759, 28))
        self.label_5.setFont(font1)
        self.txtEmail = QLineEdit(ThemKhachHang)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(10, 410, 759, 35))
        self.txtEmail.setMinimumSize(QSize(0, 35))
        self.txtEmail.setMaximumSize(QSize(16777215, 35))
        self.label_6 = QLabel(ThemKhachHang)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 455, 759, 28))
        self.label_6.setFont(font1)
        self.txtDiaChi = QLineEdit(ThemKhachHang)
        self.txtDiaChi.setObjectName(u"txtDiaChi")
        self.txtDiaChi.setGeometry(QRect(10, 490, 759, 35))
        self.txtDiaChi.setMinimumSize(QSize(0, 35))
        self.txtDiaChi.setMaximumSize(QSize(16777215, 35))
        self.txtCCCD = QLineEdit(ThemKhachHang)
        self.txtCCCD.setObjectName(u"txtCCCD")
        self.txtCCCD.setGeometry(QRect(10, 330, 759, 35))
        self.txtCCCD.setMinimumSize(QSize(0, 35))
        self.txtCCCD.setMaximumSize(QSize(16777215, 35))
        self.label_7 = QLabel(ThemKhachHang)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 300, 759, 28))
        self.label_7.setFont(font1)
        self.layoutWidget = QWidget(ThemKhachHang)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 761, 72))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.txtSdtKH = QLineEdit(self.layoutWidget)
        self.txtSdtKH.setObjectName(u"txtSdtKH")
        self.txtSdtKH.setMinimumSize(QSize(0, 35))
        self.txtSdtKH.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtSdtKH)

        self.layoutWidget1 = QWidget(ThemKhachHang)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 220, 761, 69))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.boxGioiTinhKH = QComboBox(self.layoutWidget1)
        self.boxGioiTinhKH.addItem("")
        self.boxGioiTinhKH.addItem("")
        self.boxGioiTinhKH.addItem("")
        self.boxGioiTinhKH.setObjectName(u"boxGioiTinhKH")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.boxGioiTinhKH.setFont(font2)

        self.verticalLayout_2.addWidget(self.boxGioiTinhKH)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.BoxNgaySinhKH = QDateEdit(self.layoutWidget1)
        self.BoxNgaySinhKH.setObjectName(u"BoxNgaySinhKH")
        self.BoxNgaySinhKH.setFont(font2)

        self.verticalLayout_3.addWidget(self.BoxNgaySinhKH)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.btnThem = QPushButton(ThemKhachHang)
        self.btnThem.setObjectName(u"btnThem")
        self.btnThem.setGeometry(QRect(550, 550, 101, 28))
        self.btnThem.setFont(font1)
        self.btnThem.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.btnCancel = QPushButton(ThemKhachHang)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(670, 550, 101, 28))
        self.btnCancel.setFont(font1)
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")

        self.retranslateUi(ThemKhachHang)

        QMetaObject.connectSlotsByName(ThemKhachHang)
    # setupUi

    def retranslateUi(self, ThemKhachHang):
        ThemKhachHang.setWindowTitle(QCoreApplication.translate("ThemKhachHang", u"Dialog", None))
        self.lbNametk2.setText(QCoreApplication.translate("ThemKhachHang", u"Th\u00eam Kh\u00e1ch H\u00e0ng", None))
        self.label_3.setText(QCoreApplication.translate("ThemKhachHang", u"T\u00ean Kh\u00e1ch H\u00e0ng", None))
        self.label_5.setText(QCoreApplication.translate("ThemKhachHang", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("ThemKhachHang", u"\u0110\u1ecba Ch\u1ec9", None))
        self.label_7.setText(QCoreApplication.translate("ThemKhachHang", u"CCCD", None))
        self.label.setText(QCoreApplication.translate("ThemKhachHang", u"S\u1ed1 \u0110i\u1ec7n Tho\u1ea1i", None))
        self.label_2.setText(QCoreApplication.translate("ThemKhachHang", u"Gi\u1edbi T\u00ednh", None))
        self.boxGioiTinhKH.setItemText(0, QCoreApplication.translate("ThemKhachHang", u"Nam", None))
        self.boxGioiTinhKH.setItemText(1, QCoreApplication.translate("ThemKhachHang", u"N\u1eef", None))
        self.boxGioiTinhKH.setItemText(2, QCoreApplication.translate("ThemKhachHang", u"Khac", None))

        self.label_4.setText(QCoreApplication.translate("ThemKhachHang", u"Ng\u00e0y Sinh", None))
        self.btnThem.setText(QCoreApplication.translate("ThemKhachHang", u"Th\u00eam", None))
        self.btnCancel.setText(QCoreApplication.translate("ThemKhachHang", u"Cancel", None))
    # retranslateUi

class Ui_SuaKhachHang(object):
    def setupUi(self, SuaKhachHang):
        if not SuaKhachHang.objectName():
            SuaKhachHang.setObjectName(u"SuaKhachHang")
        SuaKhachHang.resize(807, 601)
        self.lbNametk22 = QLabel(SuaKhachHang)
        self.lbNametk22.setObjectName(u"lbNametk22")
        self.lbNametk22.setGeometry(QRect(10, 0, 231, 51))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbNametk22.setFont(font)
        self.btnSua = QPushButton(SuaKhachHang)
        self.btnSua.setObjectName(u"btnSua")
        self.btnSua.setGeometry(QRect(550, 560, 101, 28))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.btnSua.setFont(font1)
        self.btnSua.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.btnCancel = QPushButton(SuaKhachHang)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(670, 560, 101, 28))
        self.btnCancel.setFont(font1)
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.label_6 = QLabel(SuaKhachHang)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 450, 759, 28))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(SuaKhachHang)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 295, 759, 28))
        self.label_7.setFont(font1)
        self.txtcnCCCD = QLineEdit(SuaKhachHang)
        self.txtcnCCCD.setObjectName(u"txtcnCCCD")
        self.txtcnCCCD.setGeometry(QRect(10, 325, 759, 35))
        self.txtcnCCCD.setMinimumSize(QSize(0, 35))
        self.txtcnCCCD.setMaximumSize(QSize(16777215, 35))
        self.layoutWidget = QWidget(SuaKhachHang)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 55, 761, 72))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.txtcnSdtKH = QLineEdit(self.layoutWidget)
        self.txtcnSdtKH.setObjectName(u"txtcnSdtKH")
        self.txtcnSdtKH.setMinimumSize(QSize(0, 35))
        self.txtcnSdtKH.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtcnSdtKH)

        self.label_3 = QLabel(SuaKhachHang)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 135, 759, 28))
        self.label_3.setFont(font1)
        self.layoutWidget_2 = QWidget(SuaKhachHang)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 215, 761, 69))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.boxcnGioiTinhKH = QComboBox(self.layoutWidget_2)
        self.boxcnGioiTinhKH.addItem("")
        self.boxcnGioiTinhKH.addItem("")
        self.boxcnGioiTinhKH.addItem("")
        self.boxcnGioiTinhKH.setObjectName(u"boxcnGioiTinhKH")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.boxcnGioiTinhKH.setFont(font2)

        self.verticalLayout_2.addWidget(self.boxcnGioiTinhKH)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.BoxcnNgaySinhKH = QDateEdit(self.layoutWidget_2)
        self.BoxcnNgaySinhKH.setObjectName(u"BoxcnNgaySinhKH")
        self.BoxcnNgaySinhKH.setFont(font2)

        self.verticalLayout_3.addWidget(self.BoxcnNgaySinhKH)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.txtcnEmail = QLineEdit(SuaKhachHang)
        self.txtcnEmail.setObjectName(u"txtcnEmail")
        self.txtcnEmail.setGeometry(QRect(10, 405, 759, 35))
        self.txtcnEmail.setMinimumSize(QSize(0, 35))
        self.txtcnEmail.setMaximumSize(QSize(16777215, 35))
        self.txtcnDiaChi = QLineEdit(SuaKhachHang)
        self.txtcnDiaChi.setObjectName(u"txtcnDiaChi")
        self.txtcnDiaChi.setGeometry(QRect(10, 485, 759, 35))
        self.txtcnDiaChi.setMinimumSize(QSize(0, 35))
        self.txtcnDiaChi.setMaximumSize(QSize(16777215, 35))
        self.txtcnTenKH = QLineEdit(SuaKhachHang)
        self.txtcnTenKH.setObjectName(u"txtcnTenKH")
        self.txtcnTenKH.setGeometry(QRect(10, 170, 759, 35))
        self.txtcnTenKH.setMinimumSize(QSize(0, 35))
        self.txtcnTenKH.setMaximumSize(QSize(16777215, 35))
        self.label_5 = QLabel(SuaKhachHang)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 370, 759, 28))
        self.label_5.setFont(font1)

        self.retranslateUi(SuaKhachHang)

        QMetaObject.connectSlotsByName(SuaKhachHang)
    # setupUi

    def retranslateUi(self, SuaKhachHang):
        SuaKhachHang.setWindowTitle(QCoreApplication.translate("SuaKhachHang", u"Dialog", None))
        self.lbNametk22.setText(QCoreApplication.translate("SuaKhachHang", u"S\u1eeda Kh\u00e1ch H\u00e0ng", None))
        self.btnSua.setText(QCoreApplication.translate("SuaKhachHang", u"S\u1eeda", None))
        self.btnCancel.setText(QCoreApplication.translate("SuaKhachHang", u"Cancel", None))
        self.label_6.setText(QCoreApplication.translate("SuaKhachHang", u"\u0110\u1ecba Ch\u1ec9", None))
        self.label_7.setText(QCoreApplication.translate("SuaKhachHang", u"CCCD", None))
        self.label.setText(QCoreApplication.translate("SuaKhachHang", u"S\u1ed1 \u0110i\u1ec7n Tho\u1ea1i", None))
        self.label_3.setText(QCoreApplication.translate("SuaKhachHang", u"T\u00ean Kh\u00e1ch H\u00e0ng", None))
        self.label_2.setText(QCoreApplication.translate("SuaKhachHang", u"Gi\u1edbi T\u00ednh", None))
        self.boxcnGioiTinhKH.setItemText(0, QCoreApplication.translate("SuaKhachHang", u"Nam", None))
        self.boxcnGioiTinhKH.setItemText(1, QCoreApplication.translate("SuaKhachHang", u"N\u1eef", None))
        self.boxcnGioiTinhKH.setItemText(2, QCoreApplication.translate("SuaKhachHang", u"Khac", None))

        self.label_4.setText(QCoreApplication.translate("SuaKhachHang", u"Ng\u00e0y Sinh", None))
        self.label_5.setText(QCoreApplication.translate("SuaKhachHang", u"Email", None))
    # retranslateUi



