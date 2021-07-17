# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_CreateWindow(object):
    def setupUi(self, CreateWindow):
        if not CreateWindow.objectName():
            CreateWindow.setObjectName(u"CreateWindow")
        CreateWindow.resize(452, 548)
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
        CreateWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"assets/icon/600x600.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile('assets/icon/16x16.png', QSize(16, 16))
        icon.addFile('assets/icon/24x24.png', QSize(24, 24))
        icon.addFile('assets/icon/32x32.png', QSize(32, 32))
        icon.addFile('assets/icon/48x48.png', QSize(48, 48))
        icon.addFile('assets/icon/256x256.png', QSize(256, 256))
        CreateWindow.setWindowIcon(icon)
        CreateWindow.setTabShape(QTabWidget.Rounded)
        self.actionlocalhost = QAction(CreateWindow)
        self.actionlocalhost.setObjectName(u"actionlocalhost")
        self.centralwidget = QWidget(CreateWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.central_gridLayout = QGridLayout()
        self.central_gridLayout.setObjectName(u"central_gridLayout")
        self.form_verticalLayout = QVBoxLayout()
        self.form_verticalLayout.setObjectName(u"form_verticalLayout")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        font = QFont()
        font.setPointSize(9)
        self.name_label.setFont(font)

        self.form_verticalLayout.addWidget(self.name_label)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setMinimumSize(QSize(155, 0))
        self.name_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.name_field)

        self.server_port_label = QLabel(self.centralwidget)
        self.server_port_label.setObjectName(u"server_port_label")
        self.server_port_label.setFont(font)

        self.form_verticalLayout.addWidget(self.server_port_label)

        self.server_port_field = QLineEdit(self.centralwidget)
        self.server_port_field.setObjectName(u"server_port_field")
        self.server_port_field.setMinimumSize(QSize(155, 0))
        self.server_port_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.server_port_field)

        self.query_port_label = QLabel(self.centralwidget)
        self.query_port_label.setObjectName(u"query_port_label")

        self.form_verticalLayout.addWidget(self.query_port_label)

        self.query_port_field = QLineEdit(self.centralwidget)
        self.query_port_field.setObjectName(u"query_port_field")
        self.query_port_field.setMinimumSize(QSize(155, 0))
        self.query_port_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.query_port_field)

        self.rcon_port_label = QLabel(self.centralwidget)
        self.rcon_port_label.setObjectName(u"rcon_port_label")

        self.form_verticalLayout.addWidget(self.rcon_port_label)

        self.rcon_port_field = QLineEdit(self.centralwidget)
        self.rcon_port_field.setObjectName(u"rcon_port_field")
        self.rcon_port_field.setMinimumSize(QSize(155, 0))
        self.rcon_port_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.rcon_port_field)

        self.max_ram_label = QLabel(self.centralwidget)
        self.max_ram_label.setObjectName(u"max_ram_label")
        self.max_ram_label.setFont(font)

        self.form_verticalLayout.addWidget(self.max_ram_label)

        self.max_ram_field = QLineEdit(self.centralwidget)
        self.max_ram_field.setObjectName(u"max_ram_field")
        self.max_ram_field.setMinimumSize(QSize(155, 0))
        self.max_ram_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.max_ram_field)

        self.min_ram_label = QLabel(self.centralwidget)
        self.min_ram_label.setObjectName(u"min_ram_label")

        self.form_verticalLayout.addWidget(self.min_ram_label)

        self.min_ram_field = QLineEdit(self.centralwidget)
        self.min_ram_field.setObjectName(u"min_ram_field")
        self.min_ram_field.setMinimumSize(QSize(155, 0))
        self.min_ram_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.min_ram_field)

        self.jar_path_label = QLabel(self.centralwidget)
        self.jar_path_label.setObjectName(u"jar_path_label")

        self.form_verticalLayout.addWidget(self.jar_path_label)

        self.jar_path_field = QLineEdit(self.centralwidget)
        self.jar_path_field.setObjectName(u"jar_path_field")
        self.jar_path_field.setMinimumSize(QSize(240, 0))
        self.jar_path_field.setStyleSheet(u"QLineEdit {\n"
"	height: 15px;\n"
"	border-radius: 4px;\n"
"	color: #black;\n"
"	border: 1px solid grey;\n"
"	padding: 2.5px;\n"
"	text-indent: 15px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	color: grey;\n"
"	background-color: #cecece;\n"
"	border: 1px solid grey;\n"
"}")

        self.form_verticalLayout.addWidget(self.jar_path_field)


        self.central_gridLayout.addLayout(self.form_verticalLayout, 1, 1, 1, 1)

        self.form_right_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_gridLayout.addItem(self.form_right_horizontalSpacer, 1, 2, 1, 1)

        self.form_bottom_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.central_gridLayout.addItem(self.form_bottom_verticalSpacer, 2, 0, 1, 3)

        self.form_left_horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_gridLayout.addItem(self.form_left_horizontalSpacer, 1, 0, 1, 1)


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

        self.create_button = QPushButton(self.centralwidget)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setEnabled(True)
        self.create_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_button.setStyleSheet(u"QPushButton {\n"
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
        self.create_button.setCheckable(False)
        self.create_button.setAutoExclusive(False)
        self.create_button.setAutoDefault(False)
        self.create_button.setFlat(False)

        self.button_gridLayout.addWidget(self.create_button, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.button_gridLayout, 2, 0, 1, 1)

        self.central_bottom_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.central_bottom_verticalSpacer, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        CreateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CreateWindow)
        self.statusbar.setObjectName(u"statusbar")
        CreateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CreateWindow)

        self.create_button.setDefault(False)


        QMetaObject.connectSlotsByName(CreateWindow)
    # setupUi

    def retranslateUi(self, CreateWindow):
        CreateWindow.setWindowTitle(QCoreApplication.translate("CreateWindow", u"Creating new server", None))
        self.actionlocalhost.setText(QCoreApplication.translate("CreateWindow", u"localhost", None))
        self.name_label.setText(QCoreApplication.translate("CreateWindow", u"Name", None))
#if QT_CONFIG(tooltip)
        self.name_field.setToolTip(QCoreApplication.translate("CreateWindow", u"The server's name", None))
#endif // QT_CONFIG(tooltip)
        self.name_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"Example: Minecraft Server", None))
        self.server_port_label.setText(QCoreApplication.translate("CreateWindow", u"Server port", None))
#if QT_CONFIG(tooltip)
        self.server_port_field.setToolTip(QCoreApplication.translate("CreateWindow", u"The server's TCP port (used to connect to the server)", None))
#endif // QT_CONFIG(tooltip)
        self.server_port_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"[0- 65,535] Must differ from query and rcon", None))
        self.query_port_label.setText(QCoreApplication.translate("CreateWindow", u"Query port", None))
#if QT_CONFIG(tooltip)
        self.query_port_field.setToolTip(QCoreApplication.translate("CreateWindow", u"The server's query port (used to get info about the server)", None))
#endif // QT_CONFIG(tooltip)
        self.query_port_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"[0- 65,535] Must differ from server and rcon", None))
        self.rcon_port_label.setText(QCoreApplication.translate("CreateWindow", u"RCON port", None))
#if QT_CONFIG(tooltip)
        self.rcon_port_field.setToolTip(QCoreApplication.translate("CreateWindow", u"The server's TCP port (used to connect to the server)", None))
#endif // QT_CONFIG(tooltip)
        self.rcon_port_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"[0- 65,535] Must differ from server and query", None))
        self.max_ram_label.setText(QCoreApplication.translate("CreateWindow", u"Maximum RAM", None))
#if QT_CONFIG(tooltip)
        self.max_ram_field.setToolTip(QCoreApplication.translate("CreateWindow", u"Maximum RAM allocated to the server", None))
#endif // QT_CONFIG(tooltip)
        self.max_ram_field.setText(QCoreApplication.translate("CreateWindow", u"1G", None))
        self.max_ram_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"Example: 2G, 1G, 512M, ...", None))
        self.min_ram_label.setText(QCoreApplication.translate("CreateWindow", u"Minimum RAM", None))
#if QT_CONFIG(tooltip)
        self.min_ram_field.setToolTip(QCoreApplication.translate("CreateWindow", u"Minimum RAM allocated to the server", None))
#endif // QT_CONFIG(tooltip)
        self.min_ram_field.setText(QCoreApplication.translate("CreateWindow", u"1G", None))
        self.min_ram_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"Example: 2G, 1G, 512M, ...", None))
        self.jar_path_label.setText(QCoreApplication.translate("CreateWindow", u"Jar path", None))
#if QT_CONFIG(tooltip)
        self.jar_path_field.setToolTip(QCoreApplication.translate("CreateWindow", u"Server's jar path, can be local or a URL", None))
#endif // QT_CONFIG(tooltip)
        self.jar_path_field.setText(QCoreApplication.translate("CreateWindow", u"https://static.macca.cloud/qbic/jars/spigot.jar", None))
        self.jar_path_field.setPlaceholderText(QCoreApplication.translate("CreateWindow", u"Server's jar path, can be local or a URL", None))
        self.error_label.setText(QCoreApplication.translate("CreateWindow", u"Error", None))
        self.create_button.setText(QCoreApplication.translate("CreateWindow", u"Create", None))
    # retranslateUi

