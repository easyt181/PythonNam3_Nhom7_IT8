# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlnhapsach_sualosach.ui'
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

class Ui_qlnhapsach_SuaLoSach(object):
    def setupUi(self, qlnhapsach_SuaLoSach):
        if not qlnhapsach_SuaLoSach.objectName():
            qlnhapsach_SuaLoSach.setObjectName(u"qlnhapsach_SuaLoSach")
        qlnhapsach_SuaLoSach.resize(402, 552)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/editLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        qlnhapsach_SuaLoSach.setWindowIcon(icon)
        self.layoutWidget = QWidget(qlnhapsach_SuaLoSach)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 381, 451))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.label_8.setFont(font)

        self.verticalLayout_9.addWidget(self.label_8)

        self.txtMaLoSach = QLineEdit(self.layoutWidget)
        self.txtMaLoSach.setObjectName(u"txtMaLoSach")
        self.txtMaLoSach.setMinimumSize(QSize(0, 35))
        self.txtMaLoSach.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_9.addWidget(self.txtMaLoSach)


        self.verticalLayout.addLayout(self.verticalLayout_9)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.txtChonMaSach = QLineEdit(self.layoutWidget)
        self.txtChonMaSach.setObjectName(u"txtChonMaSach")
        self.txtChonMaSach.setMinimumSize(QSize(0, 35))
        self.txtChonMaSach.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtChonMaSach)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_6.addWidget(self.label_7)

        self.cbbChonMaNCC = QComboBox(self.layoutWidget)
        self.cbbChonMaNCC.addItem("")
        self.cbbChonMaNCC.addItem("")
        self.cbbChonMaNCC.setObjectName(u"cbbChonMaNCC")
        self.cbbChonMaNCC.setMinimumSize(QSize(0, 35))
        self.cbbChonMaNCC.setMaximumSize(QSize(16777215, 35))
        self.cbbChonMaNCC.setFont(font)
        self.cbbChonMaNCC.setAutoFillBackground(False)
        self.cbbChonMaNCC.setStyleSheet(u"")
        self.cbbChonMaNCC.setEditable(True)
        self.cbbChonMaNCC.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.cbbChonMaNCC)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.txtDonGia = QLineEdit(self.layoutWidget)
        self.txtDonGia.setObjectName(u"txtDonGia")
        self.txtDonGia.setMinimumSize(QSize(0, 35))
        self.txtDonGia.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.txtDonGia)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.txtSoLuong = QLineEdit(self.layoutWidget)
        self.txtSoLuong.setObjectName(u"txtSoLuong")
        self.txtSoLuong.setMinimumSize(QSize(0, 35))
        self.txtSoLuong.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.txtSoLuong)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_4.addWidget(self.label_5)

        self.txtThanhTien = QLineEdit(self.layoutWidget)
        self.txtThanhTien.setObjectName(u"txtThanhTien")
        self.txtThanhTien.setMinimumSize(QSize(0, 35))
        self.txtThanhTien.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.txtThanhTien)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_5.addWidget(self.label_6)

        self.txtGiaBanLe = QLineEdit(self.layoutWidget)
        self.txtGiaBanLe.setObjectName(u"txtGiaBanLe")
        self.txtGiaBanLe.setMinimumSize(QSize(0, 35))
        self.txtGiaBanLe.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_5.addWidget(self.txtGiaBanLe)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.btnThoat = QPushButton(qlnhapsach_SuaLoSach)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setGeometry(QRect(280, 500, 111, 35))
        self.btnThoat.setMinimumSize(QSize(0, 35))
        self.btnThoat.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        self.btnThoat.setFont(font1)
        self.btnThoat.setStyleSheet(u"background-color: #FF6666;\n"
"border: 1px solid #FF6666;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/exitLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnThoat.setIcon(icon1)
        self.btnSuaLoSach = QPushButton(qlnhapsach_SuaLoSach)
        self.btnSuaLoSach.setObjectName(u"btnSuaLoSach")
        self.btnSuaLoSach.setGeometry(QRect(10, 500, 111, 35))
        self.btnSuaLoSach.setMinimumSize(QSize(0, 35))
        self.btnSuaLoSach.setMaximumSize(QSize(16777215, 35))
        self.btnSuaLoSach.setFont(font1)
        self.btnSuaLoSach.setStyleSheet(u"background-color: #00FF66;\n"
"border: 1px solid #00FF66;")
        self.btnSuaLoSach.setIcon(icon)
        self.verticalLayoutWidget = QWidget(qlnhapsach_SuaLoSach)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 401, 41))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(22)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)


        self.retranslateUi(qlnhapsach_SuaLoSach)

        QMetaObject.connectSlotsByName(qlnhapsach_SuaLoSach)
    # setupUi

    def retranslateUi(self, qlnhapsach_SuaLoSach):
        qlnhapsach_SuaLoSach.setWindowTitle(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"M\u00e3 l\u00f4 s\u00e1ch:", None))
        self.txtMaLoSach.setInputMask("")
        self.txtMaLoSach.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"M\u00e3 s\u00e1ch:", None))
        self.txtChonMaSach.setInputMask("")
        self.txtChonMaSach.setPlaceholderText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"Nh\u1eadp m\u00e3 s\u00e1ch ho\u1eb7c t\u00ean s\u00e1ch c\u00f3 trong h\u1ec7 th\u1ed1ng...", None))
        self.label_7.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"M\u00e3 nh\u00e0 cung c\u1ea5p:", None))
        self.cbbChonMaNCC.setItemText(0, QCoreApplication.translate("qlnhapsach_SuaLoSach", u"Ch\u1ecdn nh\u00e0 cung c\u1ea5p", None))
        self.cbbChonMaNCC.setItemText(1, QCoreApplication.translate("qlnhapsach_SuaLoSach", u"-------------------", None))

        self.label_3.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"\u0110\u01a1n gi\u00e1:", None))
        self.label_4.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"S\u1ed1 l\u01b0\u1ee3ng:", None))
        self.label_5.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"Th\u00e0nh ti\u1ec1n:", None))
        self.label_6.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"Gi\u00e1 b\u00e1n l\u1ebb:", None))
        self.btnThoat.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"H\u1ee7y", None))
        self.btnSuaLoSach.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"S\u1eeda l\u00f4 s\u00e1ch", None))
        self.label.setText(QCoreApplication.translate("qlnhapsach_SuaLoSach", u"S\u1eeda l\u00f4 s\u00e1ch", None))
    # retranslateUi

