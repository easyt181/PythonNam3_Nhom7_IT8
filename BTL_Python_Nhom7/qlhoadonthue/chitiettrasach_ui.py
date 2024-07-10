# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chitiettrasach.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import new_resource_rc

class Ui_chitiet(object):
    def setupUi(self, chitiet):
        if not chitiet.objectName():
            chitiet.setObjectName(u"chitiet")
        chitiet.resize(950, 580)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        chitiet.setWindowIcon(icon)
        chitiet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000\n"
"")
        self.table = QTableWidget(chitiet)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 170, 931, 331))
        font = QFont()
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"QTableWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setDefaultSectionSize(99)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.btn_thue = QPushButton(chitiet)
        self.btn_thue.setObjectName(u"btn_thue")
        self.btn_thue.setGeometry(QRect(800, 520, 131, 41))
        self.btn_thue.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_thue.setStyleSheet(u"background-color: red;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/exitLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_thue.setIcon(icon1)
        self.mak = QLabel(chitiet)
        self.mak.setObjectName(u"mak")
        self.mak.setGeometry(QRect(10, 90, 211, 16))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        self.mak.setFont(font1)
        self.manv = QLabel(chitiet)
        self.manv.setObjectName(u"manv")
        self.manv.setGeometry(QRect(10, 130, 211, 16))
        self.manv.setFont(font1)
        self.tongtien = QLabel(chitiet)
        self.tongtien.setObjectName(u"tongtien")
        self.tongtien.setGeometry(QRect(300, 100, 211, 16))
        self.tongtien.setFont(font1)
        self.trangthai = QLabel(chitiet)
        self.trangthai.setObjectName(u"trangthai")
        self.trangthai.setGeometry(QRect(300, 130, 211, 16))
        self.trangthai.setFont(font1)
        self.btn_thue_2 = QPushButton(chitiet)
        self.btn_thue_2.setObjectName(u"btn_thue_2")
        self.btn_thue_2.setGeometry(QRect(630, 520, 131, 41))
        self.btn_thue_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_thue_2.setStyleSheet(u"background-color: green;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        self.btn_thue_2.setIcon(icon)
        self.verticalLayoutWidget = QWidget(chitiet)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 931, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(chitiet)

        QMetaObject.connectSlotsByName(chitiet)
    # setupUi

    def retranslateUi(self, chitiet):
        chitiet.setWindowTitle(QCoreApplication.translate("chitiet", u"Dialog", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("chitiet", u"M\u00e3 h\u00f3a \u0111\u01a1n", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("chitiet", u"M\u00e3 s\u00e1ch", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("chitiet", u"T\u00ean s\u00e1ch", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("chitiet", u"\u0110\u01a1n gi\u00e1", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("chitiet", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("chitiet", u"Th\u00e0nh ti\u1ec1n", None));
        self.btn_thue.setText(QCoreApplication.translate("chitiet", u"Tho\u00e1t", None))
        self.mak.setText(QCoreApplication.translate("chitiet", u"M\u00e3 kh\u00e1ch", None))
        self.manv.setText(QCoreApplication.translate("chitiet", u"M\u00e3 nh\u00e2n vi\u00ean", None))
        self.tongtien.setText(QCoreApplication.translate("chitiet", u"T\u1ed5ng ti\u1ec1n", None))
        self.trangthai.setText(QCoreApplication.translate("chitiet", u"Tr\u1ea1ng th\u00e1i", None))
        self.btn_thue_2.setText(QCoreApplication.translate("chitiet", u"Tr\u1ea3 s\u00e1ch", None))
        self.label.setText(QCoreApplication.translate("chitiet", u"Chi Ti\u1ebft H\u00f3a \u0110\u01a1n Thu\u00ea S\u00e1ch", None))
    # retranslateUi

