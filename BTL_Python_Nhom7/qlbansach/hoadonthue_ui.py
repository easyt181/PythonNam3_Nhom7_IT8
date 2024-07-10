# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hoadonthue.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 580)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/borrow (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: #fff;\n"
"color:#000;")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 151, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 120, 241, 81))
        self.widget.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 81, 20))
        self.sdt = QLineEdit(self.widget)
        self.sdt.setObjectName(u"sdt")
        self.sdt.setGeometry(QRect(90, 5, 141, 25))
        self.sdt.setStyleSheet(u"")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 50, 81, 20))
        self.ten = QLineEdit(self.widget)
        self.ten.setObjectName(u"ten")
        self.ten.setGeometry(QRect(90, 45, 141, 25))
        self.ten.setStyleSheet(u"")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(350, 120, 241, 81))
        self.widget_2.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 81, 20))
        self.email = QLineEdit(self.widget_2)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(90, 5, 141, 25))
        self.email.setStyleSheet(u"")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 50, 81, 20))
        self.diachi = QLineEdit(self.widget_2)
        self.diachi.setObjectName(u"diachi")
        self.diachi.setGeometry(QRect(90, 45, 141, 25))
        self.diachi.setStyleSheet(u"")
        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(680, 120, 241, 81))
        self.widget_3.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 81, 20))
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 50, 81, 20))
        self.ngaythue = QDateEdit(self.widget_3)
        self.ngaythue.setObjectName(u"ngaythue")
        self.ngaythue.setGeometry(QRect(100, 5, 130, 25))
        self.ngayhh = QDateEdit(self.widget_3)
        self.ngayhh.setObjectName(u"ngayhh")
        self.ngayhh.setGeometry(QRect(100, 45, 130, 25))
        self.hdt_table = QTableWidget(Dialog)
        if (self.hdt_table.columnCount() < 4):
            self.hdt_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.hdt_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hdt_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hdt_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.hdt_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.hdt_table.setObjectName(u"hdt_table")
        self.hdt_table.setGeometry(QRect(10, 210, 931, 281))
        self.hdt_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"QTableWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.hdt_table.setAlternatingRowColors(True)
        self.hdt_table.horizontalHeader().setDefaultSectionSize(99)
        self.hdt_table.horizontalHeader().setStretchLastSection(True)
        self.tongtien = QLabel(Dialog)
        self.tongtien.setObjectName(u"tongtien")
        self.tongtien.setGeometry(QRect(550, 500, 381, 21))
        self.tongtien.setFont(font)
        self.btn_thanhtoan = QPushButton(Dialog)
        self.btn_thanhtoan.setObjectName(u"btn_thanhtoan")
        self.btn_thanhtoan.setGeometry(QRect(640, 540, 131, 31))
        self.btn_thanhtoan.setStyleSheet(u"background-color: green;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        self.btn_thanhtoan.setIcon(icon)
        self.btn_huy = QPushButton(Dialog)
        self.btn_huy.setObjectName(u"btn_huy")
        self.btn_huy.setGeometry(QRect(800, 540, 131, 31))
        self.btn_huy.setStyleSheet(u"background-color: red;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/exitLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_huy.setIcon(icon1)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 951, 51))
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
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Th\u00f4ng tin", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"H\u1ecd T\u00ean", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0110\u1ecba ch\u1ec9", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y thu\u00ea", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y h\u1ebft h\u1ea1n", None))
        ___qtablewidgetitem = self.hdt_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"T\u00ean s\u00e1ch", None));
        ___qtablewidgetitem1 = self.hdt_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Lo\u1ea1i s\u00e1ch", None));
        ___qtablewidgetitem2 = self.hdt_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem3 = self.hdt_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Gi\u00e1 b\u00e1n", None));
        self.tongtien.setText(QCoreApplication.translate("Dialog", u"T\u1ed5ng ti\u1ec1n: ", None))
        self.btn_thanhtoan.setText(QCoreApplication.translate("Dialog", u"Thanh to\u00e1n", None))
        self.btn_huy.setText(QCoreApplication.translate("Dialog", u"H\u1ee7y", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Thanh to\u00e1n h\u00f3a \u0111\u01a1n cho thu\u00ea", None))
    # retranslateUi

