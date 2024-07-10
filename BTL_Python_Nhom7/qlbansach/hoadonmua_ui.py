# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hoadonmua.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_hoadonmua_dialog(object):
    def setupUi(self, hoadonmua_dialog):
        if not hoadonmua_dialog.objectName():
            hoadonmua_dialog.setObjectName(u"hoadonmua_dialog")
        hoadonmua_dialog.resize(950, 580)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/add-to-cart (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        hoadonmua_dialog.setWindowIcon(icon)
        hoadonmua_dialog.setStyleSheet(u"background-color: #fff;\n"
"color:#000;")
        self.label_3 = QLabel(hoadonmua_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 151, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.widget = QWidget(hoadonmua_dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 100, 211, 41))
        self.widget.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 81, 20))
        self.sdt = QLineEdit(self.widget)
        self.sdt.setObjectName(u"sdt")
        self.sdt.setGeometry(QRect(90, 10, 121, 25))
        self.sdt.setStyleSheet(u"")
        self.hdm_table = QTableWidget(hoadonmua_dialog)
        if (self.hdm_table.columnCount() < 4):
            self.hdm_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.hdm_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hdm_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hdm_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.hdm_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.hdm_table.setObjectName(u"hdm_table")
        self.hdm_table.setGeometry(QRect(10, 160, 931, 301))
        self.hdm_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"QTableWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.hdm_table.setAlternatingRowColors(True)
        self.hdm_table.horizontalHeader().setDefaultSectionSize(99)
        self.hdm_table.horizontalHeader().setStretchLastSection(True)
        self.thanhtoan = QPushButton(hoadonmua_dialog)
        self.thanhtoan.setObjectName(u"thanhtoan")
        self.thanhtoan.setGeometry(QRect(660, 530, 131, 31))
        self.thanhtoan.setStyleSheet(u"background-color: green;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        self.thanhtoan.setIcon(icon)
        self.huy = QPushButton(hoadonmua_dialog)
        self.huy.setObjectName(u"huy")
        self.huy.setGeometry(QRect(800, 530, 131, 31))
        self.huy.setStyleSheet(u"background-color: red;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/exitLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.huy.setIcon(icon1)
        self.tongtien = QLabel(hoadonmua_dialog)
        self.tongtien.setObjectName(u"tongtien")
        self.tongtien.setGeometry(QRect(560, 470, 381, 21))
        self.tongtien.setFont(font)
        self.verticalLayoutWidget = QWidget(hoadonmua_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 951, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(hoadonmua_dialog)

        QMetaObject.connectSlotsByName(hoadonmua_dialog)
    # setupUi

    def retranslateUi(self, hoadonmua_dialog):
        hoadonmua_dialog.setWindowTitle(QCoreApplication.translate("hoadonmua_dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("hoadonmua_dialog", u"Th\u00f4ng tin", None))
        self.label_4.setText(QCoreApplication.translate("hoadonmua_dialog", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        ___qtablewidgetitem = self.hdm_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("hoadonmua_dialog", u"T\u00ean s\u00e1ch", None));
        ___qtablewidgetitem1 = self.hdm_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("hoadonmua_dialog", u"Lo\u1ea1i s\u00e1ch", None));
        ___qtablewidgetitem2 = self.hdm_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("hoadonmua_dialog", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem3 = self.hdm_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("hoadonmua_dialog", u"Gi\u00e1 b\u00e1n", None));
        self.thanhtoan.setText(QCoreApplication.translate("hoadonmua_dialog", u"Thanh to\u00e1n", None))
        self.huy.setText(QCoreApplication.translate("hoadonmua_dialog", u"H\u1ee7y", None))
        self.tongtien.setText(QCoreApplication.translate("hoadonmua_dialog", u"T\u1ed5ng ti\u1ec1n: ", None))
        self.label.setText(QCoreApplication.translate("hoadonmua_dialog", u"Ti\u1ebfn h\u00e0nh thanh to\u00e1n", None))
    # retranslateUi

