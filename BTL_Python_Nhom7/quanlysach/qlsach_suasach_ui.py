# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlsach_suasach.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_qlsach_suasach(object):
    def setupUi(self, qlsach_suasach):
        if not qlsach_suasach.objectName():
            qlsach_suasach.setObjectName(u"qlsach_suasach")
        qlsach_suasach.resize(401, 482)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/updateLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        qlsach_suasach.setWindowIcon(icon)
        self.layoutWidget = QWidget(qlsach_suasach)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 381, 371))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.txtMaSach = QLineEdit(self.layoutWidget)
        self.txtMaSach.setObjectName(u"txtMaSach")
        self.txtMaSach.setMinimumSize(QSize(0, 35))
        self.txtMaSach.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.txtMaSach)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_4.addWidget(self.label_5)

        self.txtTenSach = QLineEdit(self.layoutWidget)
        self.txtTenSach.setObjectName(u"txtTenSach")
        self.txtTenSach.setMinimumSize(QSize(0, 35))
        self.txtTenSach.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.txtTenSach)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_6.addWidget(self.label_7)

        self.txtTheLoaiSach = QLineEdit(self.layoutWidget)
        self.txtTheLoaiSach.setObjectName(u"txtTheLoaiSach")
        self.txtTheLoaiSach.setMinimumSize(QSize(0, 35))
        self.txtTheLoaiSach.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_6.addWidget(self.txtTheLoaiSach)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.txtNhaXuatBan = QLineEdit(self.layoutWidget)
        self.txtNhaXuatBan.setObjectName(u"txtNhaXuatBan")
        self.txtNhaXuatBan.setMinimumSize(QSize(0, 35))
        self.txtNhaXuatBan.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.txtNhaXuatBan)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.txtGiaBanLe = QLineEdit(self.layoutWidget)
        self.txtGiaBanLe.setObjectName(u"txtGiaBanLe")
        self.txtGiaBanLe.setMinimumSize(QSize(0, 35))
        self.txtGiaBanLe.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.txtGiaBanLe)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayoutWidget = QWidget(qlsach_suasach)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 401, 37))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.btnSuaSach = QPushButton(qlsach_suasach)
        self.btnSuaSach.setObjectName(u"btnSuaSach")
        self.btnSuaSach.setGeometry(QRect(10, 430, 111, 35))
        self.btnSuaSach.setMinimumSize(QSize(0, 35))
        self.btnSuaSach.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        self.btnSuaSach.setFont(font2)
        self.btnSuaSach.setStyleSheet(u"background-color: #00FF66;\n"
"border: 1px solid #00FF66;")
        self.btnSuaSach.setIcon(icon)
        self.btnThoat = QPushButton(qlsach_suasach)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setGeometry(QRect(280, 430, 111, 35))
        self.btnThoat.setMinimumSize(QSize(0, 35))
        self.btnThoat.setMaximumSize(QSize(16777215, 35))
        self.btnThoat.setFont(font2)
        self.btnThoat.setStyleSheet(u"background-color: #FF6666;\n"
"border: 1px solid #FF6666;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/exitLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnThoat.setIcon(icon1)

        self.retranslateUi(qlsach_suasach)

        QMetaObject.connectSlotsByName(qlsach_suasach)
    # setupUi

    def retranslateUi(self, qlsach_suasach):
        qlsach_suasach.setWindowTitle(QCoreApplication.translate("qlsach_suasach", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("qlsach_suasach", u"M\u00e3 s\u00e1ch:", None))
        self.txtMaSach.setInputMask("")
        self.txtMaSach.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("qlsach_suasach", u"T\u00ean s\u00e1ch:", None))
        self.label_7.setText(QCoreApplication.translate("qlsach_suasach", u"Th\u1ec3 lo\u1ea1i s\u00e1ch:", None))
        self.label_3.setText(QCoreApplication.translate("qlsach_suasach", u"Nh\u00e0 xu\u1ea5t b\u1ea3n:", None))
        self.label_4.setText(QCoreApplication.translate("qlsach_suasach", u"Gi\u00e1 b\u00e1n l\u1ebb:", None))
        self.label.setText(QCoreApplication.translate("qlsach_suasach", u"S\u1eeda th\u00f4ng tin s\u00e1ch", None))
        self.btnSuaSach.setText(QCoreApplication.translate("qlsach_suasach", u"S\u1eeda", None))
        self.btnThoat.setText(QCoreApplication.translate("qlsach_suasach", u"H\u1ee7y", None))
    # retranslateUi

