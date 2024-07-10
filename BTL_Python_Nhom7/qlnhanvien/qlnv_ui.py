# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlnv.ui'
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

class Ui_nhanvienmain(object):
    def setupUi(self, nhanvienmain):
        if not nhanvienmain.objectName():
            nhanvienmain.setObjectName(u"nhanvienmain")
        nhanvienmain.resize(1141, 758)
        self.centralwidget = QWidget(nhanvienmain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnThemNhanVien = QPushButton(self.centralwidget)
        self.btnThemNhanVien.setObjectName(u"btnThemNhanVien")
        self.btnThemNhanVien.setGeometry(QRect(10, 70, 201, 45))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(14)
        font.setBold(True)
        self.btnThemNhanVien.setFont(font)
        self.btnThemNhanVien.setStyleSheet(u"QPushButton{\n"
"background-color: #34D481;\n"
"border: none;\n"
"border-radius: 8px;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.lbNametk = QLabel(self.centralwidget)
        self.lbNametk.setObjectName(u"lbNametk")
        self.lbNametk.setGeometry(QRect(500, 10, 258, 40))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbNametk.setFont(font1)
        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(980, 70, 130, 45))
        self.btnSearch.setMaximumSize(QSize(130, 45))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        self.btnSearch.setFont(font2)
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
        self.tableNhanVien = QTableWidget(self.centralwidget)
        if (self.tableNhanVien.columnCount() < 10):
            self.tableNhanVien.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableNhanVien.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableNhanVien.setObjectName(u"tableNhanVien")
        self.tableNhanVien.setGeometry(QRect(0, 150, 1141, 581))
        self.tableNhanVien.setMaximumSize(QSize(1141, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(10)
        self.tableNhanVien.setFont(font3)
        self.tableNhanVien.horizontalHeader().setDefaultSectionSize(114)
        nhanvienmain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(nhanvienmain)
        self.statusbar.setObjectName(u"statusbar")
        nhanvienmain.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(nhanvienmain)
        self.toolBar.setObjectName(u"toolBar")
        nhanvienmain.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(nhanvienmain)

        QMetaObject.connectSlotsByName(nhanvienmain)
    # setupUi

    def retranslateUi(self, nhanvienmain):
        nhanvienmain.setWindowTitle(QCoreApplication.translate("nhanvienmain", u"MainWindow", None))
        self.btnThemNhanVien.setText(QCoreApplication.translate("nhanvienmain", u"Th\u00eam Nh\u00e2n Vi\u00ean", None))
        self.lbNametk.setText(QCoreApplication.translate("nhanvienmain", u"Qu\u1ea3n L\u00fd Nh\u00e2n Vi\u00ean", None))
        self.btnSearch.setText(QCoreApplication.translate("nhanvienmain", u"T\u00ecm ki\u1ebfm", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("nhanvienmain", u"Search here...", None))
        ___qtablewidgetitem = self.tableNhanVien.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("nhanvienmain", u"ID NH\u00c2N VI\u00caN", None));
        ___qtablewidgetitem1 = self.tableNhanVien.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("nhanvienmain", u"ID TK NH\u00c2N VI\u00caN", None));
        ___qtablewidgetitem2 = self.tableNhanVien.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("nhanvienmain", u"T\u00caN NH\u00c2N VI\u00caN", None));
        ___qtablewidgetitem3 = self.tableNhanVien.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("nhanvienmain", u"GI\u1edaI T\u00cdNH", None));
        ___qtablewidgetitem4 = self.tableNhanVien.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("nhanvienmain", u"NG\u00c0Y SINH", None));
        ___qtablewidgetitem5 = self.tableNhanVien.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("nhanvienmain", u"S\u1ed0 \u0110I\u1ec6N THO\u1ea0I", None));
        ___qtablewidgetitem6 = self.tableNhanVien.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("nhanvienmain", u"EMAIL", None));
        ___qtablewidgetitem7 = self.tableNhanVien.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("nhanvienmain", u"\u0110\u1ecaA CH\u1ec8", None));
        ___qtablewidgetitem8 = self.tableNhanVien.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("nhanvienmain", u"L\u01af\u01a0NG", None));
        ___qtablewidgetitem9 = self.tableNhanVien.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("nhanvienmain", u"HO\u1ea0T \u0110\u1ed8NG", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("nhanvienmain", u"toolBar", None))
    # retranslateUi

