# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(733, 719)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMinimumSize(QSize(733, 719))
        Main.setMaximumSize(QSize(733, 719))
        Main.setMouseTracking(True)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.listAvailableDevices = QListWidget(self.widget)
        QListWidgetItem(self.listAvailableDevices)
        self.listAvailableDevices.setObjectName(u"listAvailableDevices")
        self.listAvailableDevices.setGeometry(QRect(200, 60, 500, 150))
        self.listAvailableDevices.setMinimumSize(QSize(500, 150))
        self.listAvailableDevices.setMaximumSize(QSize(500, 150))
        self.listAvailableDevices.setAcceptDrops(False)
        self.listAvailableDevices.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.listAvailableDevices.setStyleSheet(u"font: 900 17pt \"Sitka\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.listAvailableDevices.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listAvailableDevices.setFlow(QListView.Flow.TopToBottom)
        self.btnOnOffBluetooth = QPushButton(self.widget)
        self.btnOnOffBluetooth.setObjectName(u"btnOnOffBluetooth")
        self.btnOnOffBluetooth.setGeometry(QRect(620, 10, 85, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnOnOffBluetooth.sizePolicy().hasHeightForWidth())
        self.btnOnOffBluetooth.setSizePolicy(sizePolicy1)
        self.btnOnOffBluetooth.setMinimumSize(QSize(85, 40))
        self.btnOnOffBluetooth.setMaximumSize(QSize(85, 40))
        self.btnOnOffBluetooth.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.btnOnOffBluetooth.setCheckable(True)
        self.listAvailableServices = QListWidget(self.widget)
        QListWidgetItem(self.listAvailableServices)
        self.listAvailableServices.setObjectName(u"listAvailableServices")
        self.listAvailableServices.setGeometry(QRect(200, 220, 500, 150))
        self.listAvailableServices.setMinimumSize(QSize(500, 150))
        self.listAvailableServices.setMaximumSize(QSize(500, 150))
        self.listAvailableServices.setAcceptDrops(False)
        self.listAvailableServices.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.listAvailableServices.setStyleSheet(u"font: 900 17pt \"Sitka\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.listAvailableServices.setFlow(QListView.Flow.TopToBottom)
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(15, 60, 152, 126))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 170, 127);\n"
"font: 800 18pt \"Sitka\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnConnect = QPushButton(self.layoutWidget)
        self.btnConnect.setObjectName(u"btnConnect")
        sizePolicy.setHeightForWidth(self.btnConnect.sizePolicy().hasHeightForWidth())
        self.btnConnect.setSizePolicy(sizePolicy)
        self.btnConnect.setMinimumSize(QSize(150, 40))
        self.btnConnect.setMaximumSize(QSize(150, 40))
        self.btnConnect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConnect.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 700 9pt \"Segoe UI\";")
        self.btnConnect.setCheckable(False)

        self.verticalLayout_2.addWidget(self.btnConnect)

        self.layoutWidget1 = QWidget(self.widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 220, 161, 123))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(159, 30))
        self.label_2.setMaximumSize(QSize(159, 30))
        self.label_2.setStyleSheet(u"color: rgb(0, 170, 127);\n"
"font: 800 18pt \"Sitka\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(156, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btnSelectService = QPushButton(self.layoutWidget1)
        self.btnSelectService.setObjectName(u"btnSelectService")
        sizePolicy.setHeightForWidth(self.btnSelectService.sizePolicy().hasHeightForWidth())
        self.btnSelectService.setSizePolicy(sizePolicy)
        self.btnSelectService.setMinimumSize(QSize(150, 40))
        self.btnSelectService.setMaximumSize(QSize(150, 40))
        self.btnSelectService.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSelectService.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 700 9pt \"Segoe UI\";")
        self.btnSelectService.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btnSelectService, 0, Qt.AlignmentFlag.AlignHCenter)

        self.listAvailableChar = QListWidget(self.widget)
        QListWidgetItem(self.listAvailableChar)
        self.listAvailableChar.setObjectName(u"listAvailableChar")
        self.listAvailableChar.setGeometry(QRect(200, 380, 500, 150))
        self.listAvailableChar.setMinimumSize(QSize(500, 150))
        self.listAvailableChar.setMaximumSize(QSize(500, 150))
        self.listAvailableChar.setAcceptDrops(False)
        self.listAvailableChar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.listAvailableChar.setStyleSheet(u"font: 900 17pt \"Sitka\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.listAvailableChar.setFlow(QListView.Flow.TopToBottom)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 550, 666, 82))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnInput = QPushButton(self.widget1)
        self.btnInput.setObjectName(u"btnInput")
        self.btnInput.setMinimumSize(QSize(83, 40))
        self.btnInput.setMaximumSize(QSize(83, 40))
        self.btnInput.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.btnInput)

        self.textWriteData = QTextEdit(self.widget1)
        self.textWriteData.setObjectName(u"textWriteData")
        self.textWriteData.setMinimumSize(QSize(200, 80))
        self.textWriteData.setMaximumSize(QSize(200, 80))
        self.textWriteData.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"Sitka\";")

        self.horizontalLayout.addWidget(self.textWriteData)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 40))
        self.label_3.setMaximumSize(QSize(130, 40))
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 127);\n"
"font: 800 18pt \"Sitka\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.labelReadData = QLabel(self.widget1)
        self.labelReadData.setObjectName(u"labelReadData")
        sizePolicy.setHeightForWidth(self.labelReadData.sizePolicy().hasHeightForWidth())
        self.labelReadData.setSizePolicy(sizePolicy)
        self.labelReadData.setMinimumSize(QSize(230, 80))
        self.labelReadData.setMaximumSize(QSize(230, 80))
        self.labelReadData.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.labelReadData.setWordWrap(True)

        self.horizontalLayout.addWidget(self.labelReadData)

        self.layoutWidget_2 = QWidget(self.widget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 380, 161, 123))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 30))
        self.label_4.setMaximumSize(QSize(150, 30))
        self.label_4.setStyleSheet(u"color: rgb(0, 170, 127);\n"
"font: 800 18pt \"Sitka\";")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(156, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.btnSelectChar = QPushButton(self.layoutWidget_2)
        self.btnSelectChar.setObjectName(u"btnSelectChar")
        sizePolicy.setHeightForWidth(self.btnSelectChar.sizePolicy().hasHeightForWidth())
        self.btnSelectChar.setSizePolicy(sizePolicy)
        self.btnSelectChar.setMinimumSize(QSize(150, 40))
        self.btnSelectChar.setMaximumSize(QSize(150, 40))
        self.btnSelectChar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSelectChar.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 700 9pt \"Segoe UI\";")
        self.btnSelectChar.setCheckable(False)

        self.verticalLayout_4.addWidget(self.btnSelectChar, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widget)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 733, 25))
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))

        __sortingEnabled = self.listAvailableDevices.isSortingEnabled()
        self.listAvailableDevices.setSortingEnabled(False)
        self.listAvailableDevices.setSortingEnabled(__sortingEnabled)

        self.btnOnOffBluetooth.setText(QCoreApplication.translate("Main", u"OFF", None))

        __sortingEnabled1 = self.listAvailableServices.isSortingEnabled()
        self.listAvailableServices.setSortingEnabled(False)
        self.listAvailableServices.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("Main", u"DEVICES", None))
        self.btnConnect.setText(QCoreApplication.translate("Main", u"SCAN", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"SERVICES", None))
        self.btnSelectService.setText(QCoreApplication.translate("Main", u"SELECT", None))

        __sortingEnabled2 = self.listAvailableChar.isSortingEnabled()
        self.listAvailableChar.setSortingEnabled(False)
        self.listAvailableChar.setSortingEnabled(__sortingEnabled2)

        self.btnInput.setText(QCoreApplication.translate("Main", u"INPUT", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"OUTPUT", None))
        self.labelReadData.setText("")
        self.label_4.setText(QCoreApplication.translate("Main", u"CHAR", None))
        self.btnSelectChar.setText(QCoreApplication.translate("Main", u"SELECT", None))
    # retranslateUi

