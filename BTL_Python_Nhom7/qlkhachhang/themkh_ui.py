# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'themkh.ui'
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

