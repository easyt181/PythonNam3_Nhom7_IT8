# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlbanhang.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 745)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sach_table = QTableWidget(self.centralwidget)
        if (self.sach_table.columnCount() < 8):
            self.sach_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.sach_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.sach_table.setObjectName(u"sach_table")
        self.sach_table.setGeometry(QRect(8, 220, 851, 481))
        self.sach_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"QTableWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.sach_table.setAlternatingRowColors(True)
        self.sach_table.horizontalHeader().setDefaultSectionSize(99)
        self.sach_table.horizontalHeader().setStretchLastSection(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 30, 291, 41))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.gio_table = QTableWidget(self.centralwidget)
        if (self.gio_table.columnCount() < 4):
            self.gio_table.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.gio_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.gio_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.gio_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.gio_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.gio_table.setObjectName(u"gio_table")
        self.gio_table.setGeometry(QRect(870, 100, 331, 531))
        self.gio_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"     \n"
"}\n"
"QTableWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.gio_table.horizontalHeader().setDefaultSectionSize(66)
        self.gio_table.horizontalHeader().setStretchLastSection(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 100, 320, 110))
        self.widget.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 44, 20))
        self.Masach = QLineEdit(self.widget)
        self.Masach.setObjectName(u"Masach")
        self.Masach.setGeometry(QRect(110, 10, 180, 25))
        self.Masach.setStyleSheet(u"")
        self.tensach = QLineEdit(self.widget)
        self.tensach.setObjectName(u"tensach")
        self.tensach.setGeometry(QRect(110, 60, 180, 25))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 60, 45, 28))
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 320, 110))
        self.widget_4.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 44, 20))
        self.Masach_2 = QLineEdit(self.widget_4)
        self.Masach_2.setObjectName(u"Masach_2")
        self.Masach_2.setGeometry(QRect(110, 10, 180, 25))
        self.Masach_2.setStyleSheet(u"")
        self.tensach_2 = QLineEdit(self.widget_4)
        self.tensach_2.setObjectName(u"tensach_2")
        self.tensach_2.setGeometry(QRect(110, 60, 180, 25))
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 60, 45, 28))
        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(680, 160, 91, 31))
        self.btn_search.setStyleSheet(u"background-color: blue;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(340, 100, 320, 110))
        self.widget_2.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.loaisach = QComboBox(self.widget_2)
        self.loaisach.setObjectName(u"loaisach")
        self.loaisach.setGeometry(QRect(110, 10, 180, 25))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 49, 28))
        self.gia = QLineEdit(self.widget_2)
        self.gia.setObjectName(u"gia")
        self.gia.setGeometry(QRect(110, 60, 180, 25))
        self.gia.setMinimumSize(QSize(0, 0))
        self.gia.setMaximumSize(QSize(9999, 999999))
        self.gia.setStyleSheet(u"")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 60, 71, 28))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 151, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(870, 70, 101, 21))
        self.label_6.setFont(font1)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(870, 640, 331, 61))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.btn_mua = QPushButton(self.widget_3)
        self.btn_mua.setObjectName(u"btn_mua")
        self.btn_mua.setGeometry(QRect(30, 10, 111, 41))
        self.btn_mua.setStyleSheet(u"background-color: green;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/invoice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_mua.setIcon(icon1)
        self.btn_thue = QPushButton(self.widget_3)
        self.btn_thue.setObjectName(u"btn_thue")
        self.btn_thue.setGeometry(QRect(190, 10, 111, 41))
        self.btn_thue.setStyleSheet(u"\n"
"color: white ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"\n"
"background-color: #33CCFF\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/borrow (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_thue.setIcon(icon2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.sach_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 s\u00e1ch", None));
        ___qtablewidgetitem1 = self.sach_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u00e1ch", None));
        ___qtablewidgetitem2 = self.sach_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i s\u00e1ch", None));
        ___qtablewidgetitem3 = self.sach_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 xu\u1ea5t b\u1ea3n", None));
        ___qtablewidgetitem4 = self.sach_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 b\u00e1n", None));
        ___qtablewidgetitem5 = self.sach_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem6 = self.sach_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        ___qtablewidgetitem7 = self.sach_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee9c n\u0103ng", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n L\u00fd B\u00e1n H\u00e0ng", None))
        ___qtablewidgetitem8 = self.gio_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u00e1ch", None));
        ___qtablewidgetitem9 = self.gio_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 b\u00e1n", None));
        ___qtablewidgetitem10 = self.gio_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"SL", None));
        ___qtablewidgetitem11 = self.gio_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee9c n\u0103ng", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 s\u00e1ch", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u00e1ch", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 s\u00e1ch", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u00e1ch", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i s\u00e1ch", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm s\u00e1ch", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gi\u1ecf h\u00e0ng", None))
        self.btn_mua.setText(QCoreApplication.translate("MainWindow", u"Mua", None))
        self.btn_thue.setText(QCoreApplication.translate("MainWindow", u"Thu\u00ea", None))
    # retranslateUi

