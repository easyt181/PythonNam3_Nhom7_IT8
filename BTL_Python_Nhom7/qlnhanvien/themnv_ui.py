# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'themnv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
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

