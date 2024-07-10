# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suakh.ui'
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

