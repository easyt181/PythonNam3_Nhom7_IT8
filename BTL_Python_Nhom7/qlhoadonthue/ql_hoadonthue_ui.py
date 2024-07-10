# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ql_hoadonthue.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 781)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.thue_table = QTableWidget(self.centralwidget)
        if (self.thue_table.columnCount() < 8):
            self.thue_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.thue_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.thue_table.setObjectName(u"thue_table")
        self.thue_table.setGeometry(QRect(10, 170, 1191, 601))
        self.thue_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"QTableWidget{\n"
"	border: none;\n"
"	background-color:#F4F9FA;\n"
"}")
        self.thue_table.horizontalHeader().setStretchLastSection(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 151, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 110, 231, 51))
        self.widget_4.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 71, 20))
        self.masach = QLineEdit(self.widget_4)
        self.masach.setObjectName(u"masach")
        self.masach.setGeometry(QRect(110, 5, 111, 25))
        self.masach.setStyleSheet(u"")
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(250, 110, 241, 51))
        self.widget_5.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 71, 20))
        self.ngaythue = QDateEdit(self.widget_5)
        self.ngaythue.setObjectName(u"ngaythue")
        self.ngaythue.setGeometry(QRect(100, 5, 130, 25))
        self.ngaythue.setStyleSheet(u"background-color: #F4F9FA;")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(500, 110, 241, 51))
        self.widget_6.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 71, 20))
        self.ngayhh = QDateEdit(self.widget_6)
        self.ngayhh.setObjectName(u"ngayhh")
        self.ngayhh.setGeometry(QRect(100, 5, 130, 25))
        self.ngayhh.setStyleSheet(u"background-color: #F4F9FA;")
        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(1040, 105, 121, 41))
        self.btn_search.setStyleSheet(u"background-color: blue;\n"
"color: #fff ;\n"
"border:none;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/searchLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search.setIcon(icon1)
        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(760, 110, 241, 51))
        self.widget_7.setStyleSheet(u"QLineEdit, QComboBox{\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"")
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 71, 20))
        self.trangthai = QComboBox(self.widget_7)
        self.trangthai.addItem("")
        self.trangthai.addItem("")
        self.trangthai.addItem("")
        self.trangthai.addItem("")
        self.trangthai.setObjectName(u"trangthai")
        self.trangthai.setGeometry(QRect(90, 5, 130, 25))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(6, 0, 1191, 51))
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.thue_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 H\u00f3a \u0110\u01a1n", None));
        ___qtablewidgetitem1 = self.thue_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 Kh\u00e1ch", None));
        ___qtablewidgetitem2 = self.thue_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 Nh\u00e2n Vi\u00ean", None));
        ___qtablewidgetitem3 = self.thue_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y Thu\u00ea", None));
        ___qtablewidgetitem4 = self.thue_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y H\u1ebft H\u1ea1n", None));
        ___qtablewidgetitem5 = self.thue_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng Ti\u1ec1n", None));
        ___qtablewidgetitem6 = self.thue_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng Th\u00e1i", None));
        ___qtablewidgetitem7 = self.thue_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee9c n\u0103ng", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm h\u00f3a \u0111\u01a1n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 h\u00f3a \u0111\u01a1n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y thu\u00ea", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y h\u1ebft h\u1ea1n", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm Ki\u1ebfm", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None))
        self.trangthai.setItemText(0, QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None))
        self.trangthai.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0110\u00e3 tr\u1ea3 h\u00e0ng", None))
        self.trangthai.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0110ang cho thu\u00ea", None))
        self.trangthai.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0110\u00e3 qu\u00e1 h\u1ea1n cho thu\u00ea", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n L\u00fd Thu\u00ea S\u00e1ch", None))
    # retranslateUi

