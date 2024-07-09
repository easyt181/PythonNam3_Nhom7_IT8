# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlsach_themsach.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import new_resource_rc

class Ui_qlsach_themsach(object):
    def setupUi(self, qlsach_themsach):
        if not qlsach_themsach.objectName():
            qlsach_themsach.setObjectName(u"qlsach_themsach")
        qlsach_themsach.resize(401, 431)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/addBook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        qlsach_themsach.setWindowIcon(icon)
        self.layoutWidget = QWidget(qlsach_themsach)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 381, 321))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.txtTenSach = QLineEdit(self.layoutWidget)
        self.txtTenSach.setObjectName(u"txtTenSach")
        self.txtTenSach.setMinimumSize(QSize(0, 35))
        self.txtTenSach.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtTenSach)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_6.addWidget(self.label_7)

        self.cbbTheLoaiSach = QComboBox(self.layoutWidget)
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.addItem("")
        self.cbbTheLoaiSach.setObjectName(u"cbbTheLoaiSach")
        self.cbbTheLoaiSach.setMinimumSize(QSize(0, 35))
        self.cbbTheLoaiSach.setMaximumSize(QSize(16777215, 35))
        self.cbbTheLoaiSach.setFont(font)
        self.cbbTheLoaiSach.setAutoFillBackground(False)
        self.cbbTheLoaiSach.setStyleSheet(u"")
        self.cbbTheLoaiSach.setEditable(False)
        self.cbbTheLoaiSach.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.cbbTheLoaiSach)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.cbbNhaXuatBan = QComboBox(self.layoutWidget)
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.addItem("")
        self.cbbNhaXuatBan.setObjectName(u"cbbNhaXuatBan")
        self.cbbNhaXuatBan.setMinimumSize(QSize(0, 35))
        self.cbbNhaXuatBan.setMaximumSize(QSize(16777215, 35))
        self.cbbNhaXuatBan.setFont(font)
        self.cbbNhaXuatBan.setAutoFillBackground(False)
        self.cbbNhaXuatBan.setStyleSheet(u"")
        self.cbbNhaXuatBan.setEditable(False)
        self.cbbNhaXuatBan.setIconSize(QSize(16, 16))

        self.verticalLayout_2.addWidget(self.cbbNhaXuatBan)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.txtGiaBanLe = QLineEdit(self.layoutWidget)
        self.txtGiaBanLe.setObjectName(u"txtGiaBanLe")
        self.txtGiaBanLe.setMinimumSize(QSize(0, 35))
        self.txtGiaBanLe.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.txtGiaBanLe)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayoutWidget = QWidget(qlsach_themsach)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 401, 37))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.btnThemSach = QPushButton(qlsach_themsach)
        self.btnThemSach.setObjectName(u"btnThemSach")
        self.btnThemSach.setGeometry(QRect(10, 380, 111, 35))
        self.btnThemSach.setMinimumSize(QSize(0, 35))
        self.btnThemSach.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        self.btnThemSach.setFont(font2)
        self.btnThemSach.setStyleSheet(u"background-color: #00FF66;\n"
"border: 1px solid #00FF66;")
        self.btnThemSach.setIcon(icon)
        self.btnThoat = QPushButton(qlsach_themsach)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setGeometry(QRect(280, 380, 111, 35))
        self.btnThoat.setMinimumSize(QSize(0, 35))
        self.btnThoat.setMaximumSize(QSize(16777215, 35))
        self.btnThoat.setFont(font2)
        self.btnThoat.setStyleSheet(u"background-color: #FF6666;\n"
"border: 1px solid #FF6666;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/exitLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnThoat.setIcon(icon1)

        self.retranslateUi(qlsach_themsach)

        QMetaObject.connectSlotsByName(qlsach_themsach)
    # setupUi

    def retranslateUi(self, qlsach_themsach):
        qlsach_themsach.setWindowTitle(QCoreApplication.translate("qlsach_themsach", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("qlsach_themsach", u"T\u00ean s\u00e1ch:", None))
        self.txtTenSach.setInputMask("")
        self.txtTenSach.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("qlsach_themsach", u"Th\u1ec3 lo\u1ea1i s\u00e1ch:", None))
        self.cbbTheLoaiSach.setItemText(0, QCoreApplication.translate("qlsach_themsach", u"Ch\u1ecdn th\u1ec3 lo\u1ea1i s\u00e1ch", None))
        self.cbbTheLoaiSach.setItemText(1, QCoreApplication.translate("qlsach_themsach", u"-------------------", None))
        self.cbbTheLoaiSach.setItemText(2, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch thi\u00ea\u0301u nhi", None))
        self.cbbTheLoaiSach.setItemText(3, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch t\u00e2m ly\u0301, ti\u0300nh ca\u0309m", None))
        self.cbbTheLoaiSach.setItemText(4, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch t\u00f4n gia\u0301o", None))
        self.cbbTheLoaiSach.setItemText(5, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch v\u0103n hoa\u0301 xa\u0303 h\u00f4\u0323i", None))
        self.cbbTheLoaiSach.setItemText(6, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch li\u0323ch s\u01b0\u0309", None))
        self.cbbTheLoaiSach.setItemText(7, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch v\u0103n ho\u0323c vi\u00ea\u0303n t\u01b0\u01a1\u0309ng", None))
        self.cbbTheLoaiSach.setItemText(8, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch ti\u00ea\u0309u s\u01b0\u0309, t\u01b0\u0323 truy\u00ea\u0323n", None))
        self.cbbTheLoaiSach.setItemText(9, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch kinh di\u0323, bi\u0301 \u00e2\u0309n", None))
        self.cbbTheLoaiSach.setItemText(10, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch khoa ho\u0323c c\u00f4ng ngh\u00ea\u0323", None))
        self.cbbTheLoaiSach.setItemText(11, QCoreApplication.translate("qlsach_themsach", u"Sa\u0301ch truy\u00ea\u0300n ca\u0309m h\u01b0\u0301ng", None))

        self.cbbTheLoaiSach.setCurrentText(QCoreApplication.translate("qlsach_themsach", u"Ch\u1ecdn th\u1ec3 lo\u1ea1i s\u00e1ch", None))
        self.label_3.setText(QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u00e2t b\u1ea3n:", None))
        self.cbbNhaXuatBan.setItemText(0, QCoreApplication.translate("qlsach_themsach", u"Ch\u1ecdn nh\u00e0 xu\u1ea5t b\u1ea3n", None))
        self.cbbNhaXuatBan.setItemText(1, QCoreApplication.translate("qlsach_themsach", u"-------------------", None))
        self.cbbNhaXuatBan.setItemText(2, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n gi\u00e1o d\u1ee5c Vi\u1ec7t Nam", None))
        self.cbbNhaXuatBan.setItemText(3, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n Tr\u1ebb", None))
        self.cbbNhaXuatBan.setItemText(4, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n Kim \u0110\u1ed3ng", None))
        self.cbbNhaXuatBan.setItemText(5, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n ch\u00ednh tr\u1ecb qu\u1ed1c gia s\u1ef1 th\u1eadt", None))
        self.cbbNhaXuatBan.setItemText(6, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n T\u1ed5ng h\u1ee3p th\u00e0nh ph\u1ed1 H\u1ed3 Ch\u00ed Minh", None))
        self.cbbNhaXuatBan.setItemText(7, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n T\u01b0 ph\u00e1p", None))
        self.cbbNhaXuatBan.setItemText(8, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n H\u1ed9i Nh\u00e0 v\u0103n", None))
        self.cbbNhaXuatBan.setItemText(9, QCoreApplication.translate("qlsach_themsach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n lao \u0111\u1ed9ng", None))

        self.cbbNhaXuatBan.setCurrentText(QCoreApplication.translate("qlsach_themsach", u"Ch\u1ecdn nh\u00e0 xu\u1ea5t b\u1ea3n", None))
        self.label_4.setText(QCoreApplication.translate("qlsach_themsach", u"Gi\u00e1 b\u00e1n l\u1ebb:", None))
        self.label.setText(QCoreApplication.translate("qlsach_themsach", u"Th\u00eam s\u00e1ch m\u1edbi", None))
        self.btnThemSach.setText(QCoreApplication.translate("qlsach_themsach", u"Th\u00eam s\u00e1ch", None))
        self.btnThoat.setText(QCoreApplication.translate("qlsach_themsach", u"H\u1ee7y", None))
    # retranslateUi

