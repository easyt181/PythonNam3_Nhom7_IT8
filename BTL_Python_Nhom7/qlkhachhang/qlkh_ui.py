# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlkh.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolBar, QWidget)
import new_resource_rc

class Ui_khachhangmain(object):
    def setupUi(self, khachhangmain):
        if not khachhangmain.objectName():
            khachhangmain.setObjectName(u"khachhangmain")
        khachhangmain.resize(1141, 758)
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(12)
        khachhangmain.setFont(font)
        self.centralwidget = QWidget(khachhangmain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnThemKhachHang = QPushButton(self.centralwidget)
        self.btnThemKhachHang.setObjectName(u"btnThemKhachHang")
        self.btnThemKhachHang.setGeometry(QRect(10, 70, 201, 45))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.btnThemKhachHang.setFont(font1)
        self.btnThemKhachHang.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.lbNametk = QLabel(self.centralwidget)
        self.lbNametk.setObjectName(u"lbNametk")
        self.lbNametk.setGeometry(QRect(500, 10, 291, 40))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.lbNametk.setFont(font2)
        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(980, 70, 130, 45))
        self.btnSearch.setMaximumSize(QSize(130, 45))
        self.btnSearch.setFont(font)
        self.btnSearch.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 170, 255)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/research.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QSize(25, 25))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(420, 70, 521, 45))
        self.lineEdit.setMaximumSize(QSize(16777215, 45))
        self.lineEdit.setStyleSheet(u"")
        self.tableKhachHang = QTableWidget(self.centralwidget)
        if (self.tableKhachHang.columnCount() < 9):
            self.tableKhachHang.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableKhachHang.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableKhachHang.setObjectName(u"tableKhachHang")
        self.tableKhachHang.setGeometry(QRect(0, 150, 1141, 581))
        self.tableKhachHang.setMaximumSize(QSize(1141, 16777215))
        self.tableKhachHang.setFont(font)
        self.tableKhachHang.setSortingEnabled(True)
        self.tableKhachHang.horizontalHeader().setMinimumSectionSize(55)
        self.tableKhachHang.horizontalHeader().setDefaultSectionSize(126)
        self.tableKhachHang.verticalHeader().setCascadingSectionResizes(False)
        self.tableKhachHang.verticalHeader().setStretchLastSection(False)
        khachhangmain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(khachhangmain)
        self.statusbar.setObjectName(u"statusbar")
        khachhangmain.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(khachhangmain)
        self.toolBar.setObjectName(u"toolBar")
        khachhangmain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(khachhangmain)

        QMetaObject.connectSlotsByName(khachhangmain)
    # setupUi

    def retranslateUi(self, khachhangmain):
        khachhangmain.setWindowTitle(QCoreApplication.translate("khachhangmain", u"MainWindow", None))
        self.btnThemKhachHang.setText(QCoreApplication.translate("khachhangmain", u"Th\u00eam Kh\u00e1ch H\u00e0ng", None))
        self.lbNametk.setText(QCoreApplication.translate("khachhangmain", u"Qu\u1ea3n L\u00fd Kh\u00e1ch H\u00e0ng", None))
        self.btnSearch.setText(QCoreApplication.translate("khachhangmain", u"T\u00ecm ki\u1ebfm", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("khachhangmain", u"Search here...", None))
        ___qtablewidgetitem = self.tableKhachHang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("khachhangmain", u"STT", None));
        ___qtablewidgetitem1 = self.tableKhachHang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("khachhangmain", u"S\u0110T Kh\u00e1ch H\u00e0ng", None));
        ___qtablewidgetitem2 = self.tableKhachHang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("khachhangmain", u"T\u00ean Kh\u00e1ch H\u00e0ng", None));
        ___qtablewidgetitem3 = self.tableKhachHang.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("khachhangmain", u"Gi\u1edbi T\u00ednh", None));
        ___qtablewidgetitem4 = self.tableKhachHang.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("khachhangmain", u"Ng\u00e0y Sinh", None));
        ___qtablewidgetitem5 = self.tableKhachHang.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("khachhangmain", u"CCCD", None));
        ___qtablewidgetitem6 = self.tableKhachHang.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("khachhangmain", u"Email", None));
        ___qtablewidgetitem7 = self.tableKhachHang.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("khachhangmain", u"\u0110\u1ecba Ch\u1ec9", None));
        ___qtablewidgetitem8 = self.tableKhachHang.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("khachhangmain", u"Ho\u1ea1t \u0110\u1ed9ng", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("khachhangmain", u"toolBar", None))
    # retranslateUi

