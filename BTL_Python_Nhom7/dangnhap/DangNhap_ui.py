# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DangNhap.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import new_resource_rc
import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(707, 406)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QTextEdit{\n"
"border: 1px solid gray\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 301, 411))
        self.widget.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 261, 311))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/1.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(300, 0, 411, 411))
        self.txtTaiKhoan = QTextEdit(self.widget_2)
        self.txtTaiKhoan.setObjectName(u"txtTaiKhoan")
        self.txtTaiKhoan.setGeometry(QRect(90, 130, 281, 31))
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 40, 40))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/icons/user.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 190, 40, 40))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/icons/padlock.png"))
        self.label_4.setScaledContents(True)
        self.txtMatKhau = QTextEdit(self.widget_2)
        self.txtMatKhau.setObjectName(u"txtMatKhau")
        self.txtMatKhau.setGeometry(QRect(90, 200, 281, 31))
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 110, 81, 16))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 180, 61, 16))
        self.label_6.setFont(font)
        self.btnDangNhap = QPushButton(self.widget_2)
        self.btnDangNhap.setObjectName(u"btnDangNhap")
        self.btnDangNhap.setGeometry(QRect(260, 260, 111, 51))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.btnDangNhap.setFont(font1)
        self.btnDangNhap.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border: none;\n"
"border-radius: 10px;")
        self.btnThoat = QPushButton(self.widget_2)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setGeometry(QRect(90, 260, 111, 51))
        self.btnThoat.setFont(font1)
        self.btnThoat.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"border: none;\n"
"")
        self.verticalLayoutWidget = QWidget(self.widget_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 411, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(26)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i kho\u1ea3n ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u", None))
        self.btnDangNhap.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.btnThoat.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0102NG NH\u1eacP", None))
    # retranslateUi

