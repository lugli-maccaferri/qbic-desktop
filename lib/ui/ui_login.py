# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(298, 392)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        LoginWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"assets/icon/600x600.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile('assets/icon/16x16.png', QSize(16, 16))
        icon.addFile('assets/icon/24x24.png', QSize(24, 24))
        icon.addFile('assets/icon/32x32.png', QSize(32, 32))
        icon.addFile('assets/icon/48x48.png', QSize(48, 48))
        icon.addFile('assets/icon/256x256.png', QSize(256, 256))
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setTabShape(QTabWidget.Rounded)
        self.actionlocalhost = QAction(LoginWindow)
        self.actionlocalhost.setObjectName(u"actionlocalhost")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.central_gridLayout = QGridLayout()
        self.central_gridLayout.setObjectName(u"central_gridLayout")
        self.form_right_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_gridLayout.addItem(self.form_right_horizontalSpacer, 1, 2, 1, 1)

        self.form_left_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_gridLayout.addItem(self.form_left_horizontalSpacer, 1, 0, 1, 1)

        self.form_verticalLayout = QVBoxLayout()
        self.form_verticalLayout.setObjectName(u"form_verticalLayout")
        self.serveraddress_label = QLabel(self.centralwidget)
        self.serveraddress_label.setObjectName(u"serveraddress_label")
        font = QFont()
        font.setPointSize(9)
        self.serveraddress_label.setFont(font)

        self.form_verticalLayout.addWidget(self.serveraddress_label)

        self.serveraddress_field = QLineEdit(self.centralwidget)
        self.serveraddress_field.setObjectName(u"serveraddress_field")
        self.serveraddress_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #1a1a1a;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.serveraddress_field)

        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setFont(font)

        self.form_verticalLayout.addWidget(self.username_label)

        self.username_field = QLineEdit(self.centralwidget)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #1a1a1a;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.username_field)

        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font)

        self.form_verticalLayout.addWidget(self.password_label)

        self.password_field = QLineEdit(self.centralwidget)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #1a1a1a;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")
        self.password_field.setMaxLength(32767)
        self.password_field.setEchoMode(QLineEdit.Password)

        self.form_verticalLayout.addWidget(self.password_field)


        self.central_gridLayout.addLayout(self.form_verticalLayout, 1, 1, 1, 1)

        self.form_bottom_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.central_gridLayout.addItem(self.form_bottom_verticalSpacer, 2, 0, 1, 3)


        self.gridLayout.addLayout(self.central_gridLayout, 1, 0, 1, 1)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.error_label.setFont(font1)
        self.error_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.error_label.setFrameShape(QFrame.NoFrame)
        self.error_label.setMidLineWidth(0)
        self.error_label.setTextFormat(Qt.PlainText)
        self.error_label.setScaledContents(False)
        self.error_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.error_label, 4, 0, 1, 1)

        self.central_top_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.central_top_verticalSpacer, 0, 0, 1, 1)

        self.button_gridLayout = QGridLayout()
        self.button_gridLayout.setObjectName(u"button_gridLayout")
        self.button_right_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_gridLayout.addItem(self.button_right_horizontalSpacer, 0, 2, 1, 1)

        self.button_left_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_gridLayout.addItem(self.button_left_horizontalSpacer, 0, 0, 1, 1)

        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setEnabled(True)
        self.connect_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75, 52, 212);\n"
"	color: rgb(254, 254, 254);\n"
"	border-style: none;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	height: 15px;\n"
"	width: 100%;\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: 	rgb(0,0,128);\n"
"	color: #cecece;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: 	rgb(0,0,128);\n"
"	color: #cecece;\n"
"}")
        self.connect_button.setCheckable(False)
        self.connect_button.setAutoExclusive(False)
        self.connect_button.setAutoDefault(False)
        self.connect_button.setFlat(False)

        self.button_gridLayout.addWidget(self.connect_button, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.button_gridLayout, 2, 0, 1, 1)

        self.central_bottom_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.central_bottom_verticalSpacer, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 298, 21))
        self.menuRecent = QMenu(self.menubar)
        self.menuRecent.setObjectName(u"menuRecent")
        LoginWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuRecent.menuAction())

        self.retranslateUi(LoginWindow)

        self.connect_button.setDefault(False)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Desktop client for qbic", None))
        self.actionlocalhost.setText(QCoreApplication.translate("LoginWindow", u"localhost", None))
        self.serveraddress_label.setText(QCoreApplication.translate("LoginWindow", u"Server address", None))
        self.serveraddress_field.setPlaceholderText("")
        self.username_label.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.password_field.setPlaceholderText("")
        self.error_label.setText(QCoreApplication.translate("LoginWindow", u"Error", None))
        self.connect_button.setText(QCoreApplication.translate("LoginWindow", u"Connect", None))
        self.menuRecent.setTitle(QCoreApplication.translate("LoginWindow", u"Recent", None))
    # retranslateUi

