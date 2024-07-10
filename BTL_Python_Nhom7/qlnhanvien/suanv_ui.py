# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suanv.ui'
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
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

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

