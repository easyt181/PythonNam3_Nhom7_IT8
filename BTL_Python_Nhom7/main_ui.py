# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1467, 878)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"}\n"
"QLineEdit{\n"
"padding-left:20px;\n"
"border:1px solid gray;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnInOff = QPushButton(self.header)
        self.btnInOff.setObjectName(u"btnInOff")
        self.btnInOff.setMaximumSize(QSize(30, 30))
        self.btnInOff.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnInOff.setIcon(icon1)
        self.btnInOff.setIconSize(QSize(20, 20))
        self.btnInOff.setCheckable(True)
        self.btnInOff.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.btnInOff)

        self.horizontalSpacer = QSpacerItem(295, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.header)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.btnSearch = QPushButton(self.header)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMaximumSize(QSize(50, 50))
        self.btnSearch.setStyleSheet(u"border:none")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/research.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearch.setIcon(icon2)
        self.btnSearch.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.btnSearch)

        self.horizontalSpacer_2 = QSpacerItem(215, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnAvartar = QPushButton(self.header)
        self.btnAvartar.setObjectName(u"btnAvartar")
        self.btnAvartar.setMaximumSize(QSize(80, 80))
        self.btnAvartar.setStyleSheet(u"border:none")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/profile (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAvartar.setIcon(icon3)
        self.btnAvartar.setIconSize(QSize(40, 40))
        self.btnAvartar.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnAvartar)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)

        self.verticalLayout_8.addWidget(self.label_4)

        self.lbNametk = QLabel(self.header)
        self.lbNametk.setObjectName(u"lbNametk")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbNametk.setFont(font1)

        self.verticalLayout_8.addWidget(self.lbNametk)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.header, 0, 2, 1, 1)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);")
        self.verticalLayout_7 = QVBoxLayout(self.main)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(20)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"padding-top: 10px;")

        self.verticalLayout_11.addWidget(self.label_3)

        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 35))
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-color: rgb(255, 170, 127);\n"
"}\n"
"QWidget{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(12)
        self.pushButton.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift"])
        font4.setPointSize(14)
        self.label_5.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_9.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-color: rgb(255, 170, 127);\n"
"}\n"
"QWidget{\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/bill (3).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_9.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"}\n"
"QWidget{\n"
"background-color: rgb(255, 234, 110);\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_3 = QPushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/invoice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_7)


        self.horizontalLayout_9.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"}\n"
"QWidget{\n"
"background-color: rgb(43, 190, 17);\n"
"}\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_4 = QPushButton(self.widget_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/reading-book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_4)

        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_9.addWidget(self.widget_7)


        self.verticalLayout_11.addWidget(self.widget)

        self.dothi = QWidget(self.main)
        self.dothi.setObjectName(u"dothi")
        self.dothi.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_10 = QVBoxLayout(self.dothi)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_11.addWidget(self.dothi)


        self.verticalLayout_7.addLayout(self.verticalLayout_11)


        self.gridLayout.addWidget(self.main, 1, 2, 1, 1)

        self.icon_only_menu = QWidget(self.centralwidget)
        self.icon_only_menu.setObjectName(u"icon_only_menu")
        self.icon_only_menu.setEnabled(True)
        self.icon_only_menu.setMaximumSize(QSize(70, 16777215))
        self.icon_only_menu.setStyleSheet(u"QWidget{\n"
"	border:none;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 200, 160);\n"
"\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 200, 160);\n"
"\n"
"border-radius:8px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_only_menu)
        self.verticalLayout_6.setSpacing(11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 34, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 12)
        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.icon_only_menu)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/newPrefix/icons/bookstore.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-20)
        self.label.setIndent(0)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.btnTKicon = QPushButton(self.icon_only_menu)
        self.btnTKicon.setObjectName(u"btnTKicon")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/dashboard (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/newPrefix/icons/dashboard (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnTKicon.setIcon(icon8)
        self.btnTKicon.setIconSize(QSize(30, 30))
        self.btnTKicon.setCheckable(True)
        self.btnTKicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnTKicon)

        self.btnBHicon = QPushButton(self.icon_only_menu)
        self.btnBHicon.setObjectName(u"btnBHicon")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/add-to-cart (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/newPrefix/icons/add-to-cart (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnBHicon.setIcon(icon9)
        self.btnBHicon.setIconSize(QSize(30, 30))
        self.btnBHicon.setCheckable(True)
        self.btnBHicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnBHicon)

        self.btnQLTSicon = QPushButton(self.icon_only_menu)
        self.btnQLTSicon.setObjectName(u"btnQLTSicon")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/borrow (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/newPrefix/icons/borrow (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnQLTSicon.setIcon(icon10)
        self.btnQLTSicon.setIconSize(QSize(30, 30))
        self.btnQLTSicon.setCheckable(True)
        self.btnQLTSicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnQLTSicon)

        self.btnSanPhamicon = QPushButton(self.icon_only_menu)
        self.btnSanPhamicon.setObjectName(u"btnSanPhamicon")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/open-book (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/newPrefix/icons/open-book (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSanPhamicon.setIcon(icon11)
        self.btnSanPhamicon.setIconSize(QSize(30, 30))
        self.btnSanPhamicon.setCheckable(True)
        self.btnSanPhamicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnSanPhamicon)

        self.btnKHicon_2 = QPushButton(self.icon_only_menu)
        self.btnKHicon_2.setObjectName(u"btnKHicon_2")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/icons/warehouse (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/newPrefix/icons/warehouse (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnKHicon_2.setIcon(icon12)
        self.btnKHicon_2.setIconSize(QSize(30, 30))
        self.btnKHicon_2.setCheckable(True)
        self.btnKHicon_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnKHicon_2)

        self.btnNVicon = QPushButton(self.icon_only_menu)
        self.btnNVicon.setObjectName(u"btnNVicon")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/icons/employee (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/newPrefix/icons/employee (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnNVicon.setIcon(icon13)
        self.btnNVicon.setIconSize(QSize(30, 30))
        self.btnNVicon.setCheckable(True)
        self.btnNVicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnNVicon)

        self.btnKHicon = QPushButton(self.icon_only_menu)
        self.btnKHicon.setObjectName(u"btnKHicon")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/icons/target (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/newPrefix/icons/public-relation.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnKHicon.setIcon(icon14)
        self.btnKHicon.setIconSize(QSize(30, 30))
        self.btnKHicon.setCheckable(True)
        self.btnKHicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnKHicon)

        self.btnHoaDonicon = QPushButton(self.icon_only_menu)
        self.btnHoaDonicon.setObjectName(u"btnHoaDonicon")
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix/icons/bill (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/newPrefix/icons/bill (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnHoaDonicon.setIcon(icon15)
        self.btnHoaDonicon.setIconSize(QSize(30, 30))
        self.btnHoaDonicon.setCheckable(True)
        self.btnHoaDonicon.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btnHoaDonicon)

        self.verticalSpacer = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnSTicon = QPushButton(self.icon_only_menu)
        self.btnSTicon.setObjectName(u"btnSTicon")
        icon16 = QIcon()
        icon16.addFile(u":/newPrefix/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon16.addFile(u":/newPrefix/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSTicon.setIcon(icon16)
        self.btnSTicon.setIconSize(QSize(20, 20))
        self.btnSTicon.setCheckable(True)
        self.btnSTicon.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btnSTicon)

        self.btnLOicon = QPushButton(self.icon_only_menu)
        self.btnLOicon.setObjectName(u"btnLOicon")
        icon17 = QIcon()
        icon17.addFile(u":/newPrefix/icons/logout (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/newPrefix/icons/logout (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnLOicon.setIcon(icon17)
        self.btnLOicon.setIconSize(QSize(20, 20))
        self.btnLOicon.setCheckable(True)
        self.btnLOicon.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btnLOicon)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.icon_only_menu, 0, 0, 2, 1)

        self.sibarmenu = QWidget(self.centralwidget)
        self.sibarmenu.setObjectName(u"sibarmenu")
        self.sibarmenu.setMaximumSize(QSize(231, 16777215))
        self.sibarmenu.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"text-align:left ;\n"
"border:none;\n"
"padding-left:20px;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 200, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 200, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.sibarmenu)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.sibarmenu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/bookstore.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(-31)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.btnThongKe = QPushButton(self.sibarmenu)
        self.btnThongKe.setObjectName(u"btnThongKe")
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.btnThongKe.setFont(font5)
        self.btnThongKe.setIcon(icon8)
        self.btnThongKe.setIconSize(QSize(30, 30))
        self.btnThongKe.setCheckable(True)
        self.btnThongKe.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnThongKe)

        self.btnBanHang = QPushButton(self.sibarmenu)
        self.btnBanHang.setObjectName(u"btnBanHang")
        self.btnBanHang.setFont(font5)
        self.btnBanHang.setIcon(icon9)
        self.btnBanHang.setIconSize(QSize(30, 30))
        self.btnBanHang.setCheckable(True)
        self.btnBanHang.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnBanHang)

        self.btnQuanLyThue = QPushButton(self.sibarmenu)
        self.btnQuanLyThue.setObjectName(u"btnQuanLyThue")
        self.btnQuanLyThue.setFont(font5)
        self.btnQuanLyThue.setIcon(icon10)
        self.btnQuanLyThue.setIconSize(QSize(30, 30))
        self.btnQuanLyThue.setCheckable(True)
        self.btnQuanLyThue.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnQuanLyThue)

        self.btnQLSach = QPushButton(self.sibarmenu)
        self.btnQLSach.setObjectName(u"btnQLSach")
        self.btnQLSach.setFont(font5)
        self.btnQLSach.setIcon(icon11)
        self.btnQLSach.setIconSize(QSize(30, 30))
        self.btnQLSach.setCheckable(True)
        self.btnQLSach.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnQLSach)

        self.btnQLNhapSach = QPushButton(self.sibarmenu)
        self.btnQLNhapSach.setObjectName(u"btnQLNhapSach")
        self.btnQLNhapSach.setFont(font5)
        self.btnQLNhapSach.setIcon(icon12)
        self.btnQLNhapSach.setIconSize(QSize(30, 30))
        self.btnQLNhapSach.setCheckable(True)
        self.btnQLNhapSach.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnQLNhapSach)

        self.btnNhanVien = QPushButton(self.sibarmenu)
        self.btnNhanVien.setObjectName(u"btnNhanVien")
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.btnNhanVien.setFont(font6)
        self.btnNhanVien.setIcon(icon13)
        self.btnNhanVien.setIconSize(QSize(30, 30))
        self.btnNhanVien.setCheckable(True)
        self.btnNhanVien.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnNhanVien)

        self.btnKhachHang = QPushButton(self.sibarmenu)
        self.btnKhachHang.setObjectName(u"btnKhachHang")
        self.btnKhachHang.setFont(font5)
        self.btnKhachHang.setIcon(icon14)
        self.btnKhachHang.setIconSize(QSize(30, 30))
        self.btnKhachHang.setCheckable(True)
        self.btnKhachHang.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btnKhachHang)

        self.frame_2 = QFrame(self.sibarmenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnHoaDon = QPushButton(self.frame_2)
        self.btnHoaDon.setObjectName(u"btnHoaDon")
        self.btnHoaDon.setFont(font5)
        self.btnHoaDon.setStyleSheet(u"padding-left:10px;\n"
"")
        self.btnHoaDon.setIcon(icon15)
        self.btnHoaDon.setIconSize(QSize(30, 30))
        self.btnHoaDon.setCheckable(True)
        self.btnHoaDon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btnHoaDon)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnHoaDonBanHang = QPushButton(self.frame)
        self.btnHoaDonBanHang.setObjectName(u"btnHoaDonBanHang")
        self.btnHoaDonBanHang.setFont(font)

        self.verticalLayout.addWidget(self.btnHoaDonBanHang)

        self.btnHoaDonNhapHang = QPushButton(self.frame)
        self.btnHoaDonNhapHang.setObjectName(u"btnHoaDonNhapHang")
        self.btnHoaDonNhapHang.setFont(font)

        self.verticalLayout.addWidget(self.btnHoaDonNhapHang)

        self.btnHoaDonTraHang = QPushButton(self.frame)
        self.btnHoaDonTraHang.setObjectName(u"btnHoaDonTraHang")
        self.btnHoaDonTraHang.setFont(font)
        self.btnHoaDonTraHang.setStyleSheet(u"QPushButton:checked{\n"
"background-color: rgb(255, 200, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 200, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}")

        self.verticalLayout.addWidget(self.btnHoaDonTraHang)

        self.btnHoaDonThueTruyen = QPushButton(self.frame)
        self.btnHoaDonThueTruyen.setObjectName(u"btnHoaDonThueTruyen")
        self.btnHoaDonThueTruyen.setFont(font)

        self.verticalLayout.addWidget(self.btnHoaDonThueTruyen)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.btnSetting = QPushButton(self.sibarmenu)
        self.btnSetting.setObjectName(u"btnSetting")
        font7 = QFont()
        font7.setPointSize(9)
        self.btnSetting.setFont(font7)
        self.btnSetting.setIcon(icon16)
        self.btnSetting.setIconSize(QSize(20, 20))
        self.btnSetting.setCheckable(True)
        self.btnSetting.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btnSetting)

        self.btnLogOut = QPushButton(self.sibarmenu)
        self.btnLogOut.setObjectName(u"btnLogOut")
        self.btnLogOut.setFont(font7)
        self.btnLogOut.setIcon(icon17)
        self.btnLogOut.setIconSize(QSize(20, 20))
        self.btnLogOut.setCheckable(True)
        self.btnLogOut.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btnLogOut)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.sibarmenu, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main.raise_()
        self.header.raise_()
        self.sibarmenu.raise_()
        self.icon_only_menu.raise_()

        self.retranslateUi(MainWindow)
        self.btnInOff.toggled.connect(self.icon_only_menu.setHidden)
        self.btnInOff.toggled.connect(self.sibarmenu.setVisible)
        self.btnKHicon.toggled.connect(self.btnKhachHang.setChecked)
        self.btnNVicon.toggled.connect(self.btnNhanVien.setChecked)
        self.btnHoaDonicon.toggled.connect(self.btnHoaDon.setChecked)
        self.btnKHicon_2.toggled.connect(self.btnQLNhapSach.setChecked)
        self.btnSanPhamicon.toggled.connect(self.btnQLSach.setChecked)
        self.btnQLTSicon.toggled.connect(self.btnQuanLyThue.setChecked)
        self.btnBHicon.toggled.connect(self.btnBanHang.setChecked)
        self.btnTKicon.toggled.connect(self.btnThongKe.setChecked)
        self.btnThongKe.toggled.connect(self.btnTKicon.setChecked)
        self.btnBanHang.toggled.connect(self.btnBHicon.setChecked)
        self.btnQuanLyThue.toggled.connect(self.btnQLTSicon.setChecked)
        self.btnQLSach.toggled.connect(self.btnSanPhamicon.setChecked)
        self.btnQLNhapSach.toggled.connect(self.btnKHicon_2.setChecked)
        self.btnHoaDon.toggled.connect(self.btnHoaDonicon.setChecked)
        self.btnNhanVien.toggled.connect(self.btnNVicon.setChecked)
        self.btnKhachHang.toggled.connect(self.btnKHicon.setChecked)
        self.btnHoaDon.toggled.connect(self.frame.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnInOff.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here...", None))
        self.btnSearch.setText("")
        self.btnAvartar.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Xin ch\u00e0o!", None))
        self.lbNametk.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TH\u1ed0NG K\u00ca H\u00d4M NAY", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Truy\u1ec7n", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n b\u00e1n ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n nh\u1eadp", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Thu\u00ea truy\u1ec7n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText("")
        self.btnTKicon.setText("")
        self.btnBHicon.setText("")
        self.btnQLTSicon.setText("")
        self.btnSanPhamicon.setText("")
        self.btnKHicon_2.setText("")
        self.btnNVicon.setText("")
        self.btnKHicon.setText("")
        self.btnHoaDonicon.setText("")
        self.btnSTicon.setText("")
        self.btnLOicon.setText("")
        self.label_2.setText("")
        self.btnThongKe.setText(QCoreApplication.translate("MainWindow", u"  Th\u1ed1ng k\u00ea ", None))
        self.btnBanHang.setText(QCoreApplication.translate("MainWindow", u"  B\u00e1n v\u00e0 cho thu\u00ea s\u00e1ch", None))
        self.btnQuanLyThue.setText(QCoreApplication.translate("MainWindow", u"Thu h\u1ed3i s\u00e1ch cho thu\u00ea", None))
        self.btnQLSach.setText(QCoreApplication.translate("MainWindow", u" Qu\u1ea3n l\u00fd s\u00e1ch", None))
        self.btnQLNhapSach.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd nh\u1eadp s\u00e1ch", None))
        self.btnNhanVien.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd nh\u00e2n vi\u00ean", None))
        self.btnKhachHang.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd  kh\u00e1ch h\u00e0ng", None))
        self.btnHoaDon.setText(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd h\u00f3a \u0111\u01a1n", None))
        self.btnHoaDonBanHang.setText(QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n b\u00e1n s\u00e1ch", None))
        self.btnHoaDonNhapHang.setText(QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n nh\u1eadp s\u00e1ch", None))
        self.btnHoaDonTraHang.setText(QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n tr\u1ea3 s\u00e1ch", None))
        self.btnHoaDonThueTruyen.setText(QCoreApplication.translate("MainWindow", u"H\u00f3a \u0111\u01a1n thu\u00ea truy\u1ec7n", None))
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btnLogOut.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

