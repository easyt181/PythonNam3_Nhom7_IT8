# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlsach.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_qlsach(object):
    def setupUi(self, qlsach):
        if not qlsach.objectName():
            qlsach.setObjectName(u"qlsach")
        qlsach.resize(1131, 789)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        qlsach.setWindowIcon(icon)
        qlsach.setStyleSheet(u"QComboBox{\n"
" 			padding: 6px; \n"
"            border: 2px solid #0066CC; \n"
"            border-radius: 5px;  \n"
"            font-size: 16px;\n"
"            background-color: #0066CC; \n"
"            color: white; \n"
"        }\n"
"QComboBox:focus {\n"
"            border: 2px solid #003366;  \n"
"        }\n"
"QLineEdit#txtTimKiemSach {\n"
"    padding: 6px;  /* Kho\u1ea3ng c\u00e1ch gi\u1eefa v\u0103n b\u1ea3n v\u00e0 bi\u00ean c\u1ee7a QLineEdit */\n"
"    border: 2px solid #3366CC;  /* Bo vi\u1ec1n m\u00e0u xanh l\u00e1 c\u00e2y */\n"
"    border-radius: 10px;  /* Bo g\u00f3c cho QLineEdit */\n"
"    font-size: 16px;  /* K\u00edch th\u01b0\u1edbc ph\u00f4ng ch\u1eef */\n"
"}\n"
"\n"
"QLineEdit#txtTimKiemSach:focus {\n"
"    border: 2px solid #45a049;  /* M\u00e0u vi\u1ec1n khi QLineEdit \u0111\u01b0\u1ee3c ch\u1ecdn */\n"
"}\n"
"QPushButton#btnThemSach {\n"
"    background-color: #33CC99;\n"
"    border: 2px solid #33CC99;  \n"
"    color: white;  \n"
"    padding: 10px 24px; \n"
"    text-align:"
                        " center;  \n"
"    text-decoration: none; \n"
"    font-size: 16px;\n"
"    margin: 4px 2px; \n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#btnLamMoi {\n"
"    background-color: #33CC99;\n"
"    border: 2px solid #33CC99;  \n"
"    color: white;  \n"
"    padding: 10px 24px; \n"
"    text-align: center;  \n"
"    text-decoration: none; \n"
"    font-size: 16px;\n"
"    margin: 4px 2px; \n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#btnThemSach:hover {\n"
"    background-color: #33CC66; \n"
"	border: 2px solid #33CC66; \n"
"}\n"
"QPushButton#btnLamMoi:hover {\n"
"    background-color: #33CC66; \n"
"	border: 2px solid #33CC66; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"                background-color: #003366; \n"
"                border: 1px solid #d3d3d3; \n"
"                padding: 4px; \n"
"                font-weight: bold;  \n"
"                color: white;           \n"
" }\n"
"QTableWidget{\n"
"alternate-background-color: #B0EDFB;\n"
"background-color: #F4F9FA;\n"
"border: 2px solid"
                        " #003366;\n"
"}\n"
"QTableWidget::item {\n"
" border: 1px solid #003366;\n"
"}\n"
"QTableWidget::item:selected {\n"
"                background-color: yellow;\n"
"                color: black;\n"
" }\n"
"")
        self.centralwidget = QWidget(qlsach)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1131, 49))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.btnThemSach = QPushButton(self.centralwidget)
        self.btnThemSach.setObjectName(u"btnThemSach")
        self.btnThemSach.setGeometry(QRect(10, 60, 190, 50))
        font1 = QFont()
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.btnThemSach.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/addBook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnThemSach.setIcon(icon1)
        self.btnLamMoi = QPushButton(self.centralwidget)
        self.btnLamMoi.setObjectName(u"btnLamMoi")
        self.btnLamMoi.setGeometry(QRect(230, 60, 190, 51))
        self.btnLamMoi.setMinimumSize(QSize(170, 51))
        self.btnLamMoi.setMaximumSize(QSize(190, 37))
        self.btnLamMoi.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/updateLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLamMoi.setIcon(icon2)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 130, 1071, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cbbTimKiemTheLoaiSach = QComboBox(self.layoutWidget)
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.addItem("")
        self.cbbTimKiemTheLoaiSach.setObjectName(u"cbbTimKiemTheLoaiSach")
        font2 = QFont()
        self.cbbTimKiemTheLoaiSach.setFont(font2)
        self.cbbTimKiemTheLoaiSach.setAutoFillBackground(False)
        self.cbbTimKiemTheLoaiSach.setStyleSheet(u"")
        self.cbbTimKiemTheLoaiSach.setEditable(False)
        self.cbbTimKiemTheLoaiSach.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.cbbTimKiemTheLoaiSach)

        self.cbbTimKiemNXB = QComboBox(self.layoutWidget)
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.addItem("")
        self.cbbTimKiemNXB.setObjectName(u"cbbTimKiemNXB")
        self.cbbTimKiemNXB.setMinimumSize(QSize(214, 0))
        self.cbbTimKiemNXB.setMaximumSize(QSize(214, 16777215))
        self.cbbTimKiemNXB.setFont(font2)
        self.cbbTimKiemNXB.setAutoFillBackground(False)
        self.cbbTimKiemNXB.setStyleSheet(u"")
        self.cbbTimKiemNXB.setDuplicatesEnabled(False)

        self.horizontalLayout.addWidget(self.cbbTimKiemNXB)

        self.txtTimKiemSach = QLineEdit(self.layoutWidget)
        self.txtTimKiemSach.setObjectName(u"txtTimKiemSach")
        self.txtTimKiemSach.setFont(font2)
        self.txtTimKiemSach.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.txtTimKiemSach)

        self.btnTimKiemSach = QPushButton(self.layoutWidget)
        self.btnTimKiemSach.setObjectName(u"btnTimKiemSach")
        self.btnTimKiemSach.setMinimumSize(QSize(50, 0))
        self.btnTimKiemSach.setMaximumSize(QSize(50, 50))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(10)
        self.btnTimKiemSach.setFont(font3)
        self.btnTimKiemSach.setStyleSheet(u"border:none;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/searchLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnTimKiemSach.setIcon(icon3)
        self.btnTimKiemSach.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btnTimKiemSach)

        self.tableSach = QTableWidget(self.centralwidget)
        self.tableSach.setObjectName(u"tableSach")
        self.tableSach.setGeometry(QRect(10, 200, 1111, 531))
        qlsach.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(qlsach)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1131, 21))
        qlsach.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(qlsach)
        self.statusbar.setObjectName(u"statusbar")
        qlsach.setStatusBar(self.statusbar)

        self.retranslateUi(qlsach)

        QMetaObject.connectSlotsByName(qlsach)
    # setupUi

    def retranslateUi(self, qlsach):
        qlsach.setWindowTitle(QCoreApplication.translate("qlsach", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("qlsach", u"QU\u1ea2N L\u00dd S\u00c1CH", None))
        self.btnThemSach.setText(QCoreApplication.translate("qlsach", u"Th\u00eam s\u00e1ch m\u1edbi", None))
        self.btnLamMoi.setText(QCoreApplication.translate("qlsach", u"L\u00e0m m\u1edbi", None))
        self.cbbTimKiemTheLoaiSach.setItemText(0, QCoreApplication.translate("qlsach", u"Th\u1ec3 lo\u1ea1i s\u00e1ch", None))
        self.cbbTimKiemTheLoaiSach.setItemText(1, QCoreApplication.translate("qlsach", u"Sa\u0301ch thi\u00ea\u0301u nhi", None))
        self.cbbTimKiemTheLoaiSach.setItemText(2, QCoreApplication.translate("qlsach", u"Sa\u0301ch t\u00e2m ly\u0301, ti\u0300nh ca\u0309m", None))
        self.cbbTimKiemTheLoaiSach.setItemText(3, QCoreApplication.translate("qlsach", u"Sa\u0301ch t\u00f4n gia\u0301o", None))
        self.cbbTimKiemTheLoaiSach.setItemText(4, QCoreApplication.translate("qlsach", u"Sa\u0301ch v\u0103n hoa\u0301 xa\u0303 h\u00f4\u0323i", None))
        self.cbbTimKiemTheLoaiSach.setItemText(5, QCoreApplication.translate("qlsach", u"Sa\u0301ch li\u0323ch s\u01b0\u0309", None))
        self.cbbTimKiemTheLoaiSach.setItemText(6, QCoreApplication.translate("qlsach", u"Sa\u0301ch v\u0103n ho\u0323c vi\u00ea\u0303n t\u01b0\u01a1\u0309ng", None))
        self.cbbTimKiemTheLoaiSach.setItemText(7, QCoreApplication.translate("qlsach", u"Sa\u0301ch ti\u00ea\u0309u s\u01b0\u0309, t\u01b0\u0323 truy\u00ea\u0323n", None))
        self.cbbTimKiemTheLoaiSach.setItemText(8, QCoreApplication.translate("qlsach", u"Sa\u0301ch kinh di\u0323, bi\u0301 \u00e2\u0309n", None))
        self.cbbTimKiemTheLoaiSach.setItemText(9, QCoreApplication.translate("qlsach", u"Sa\u0301ch khoa ho\u0323c c\u00f4ng ngh\u00ea\u0323", None))
        self.cbbTimKiemTheLoaiSach.setItemText(10, QCoreApplication.translate("qlsach", u"Sa\u0301ch truy\u00ea\u0300n ca\u0309m h\u01b0\u0301ng", None))

        self.cbbTimKiemNXB.setItemText(0, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n", None))
        self.cbbTimKiemNXB.setItemText(1, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n gi\u00e1o d\u1ee5c Vi\u1ec7t Nam", None))
        self.cbbTimKiemNXB.setItemText(2, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n Tr\u1ebb", None))
        self.cbbTimKiemNXB.setItemText(3, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n Kim \u0110\u1ed3ng", None))
        self.cbbTimKiemNXB.setItemText(4, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n ch\u00ednh tr\u1ecb qu\u1ed1c gia s\u1ef1 th\u1eadt", None))
        self.cbbTimKiemNXB.setItemText(5, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n T\u01b0 ph\u00e1p", None))
        self.cbbTimKiemNXB.setItemText(6, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n H\u1ed9i Nh\u00e0 v\u0103n", None))
        self.cbbTimKiemNXB.setItemText(7, QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n lao \u0111\u1ed9ng", None))

        self.cbbTimKiemNXB.setCurrentText(QCoreApplication.translate("qlsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n", None))
        self.txtTimKiemSach.setPlaceholderText(QCoreApplication.translate("qlsach", u"Nh\u1eadp t\u1eeb kh\u00f3a t\u00ecm ki\u1ebfm...", None))
        self.btnTimKiemSach.setText("")
    # retranslateUi

