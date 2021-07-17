# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mcservermanagement.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MCServerManagementWindow(object):
    def setupUi(self, MCServerManagementWindow):
        if not MCServerManagementWindow.objectName():
            MCServerManagementWindow.setObjectName(u"MCServerManagementWindow")
        MCServerManagementWindow.resize(863, 554)
        MCServerManagementWindow.setBaseSize(QSize(863, 0))
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
        MCServerManagementWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"assets/icon/600x600.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile('assets/icon/16x16.png', QSize(16, 16))
        icon.addFile('assets/icon/24x24.png', QSize(24, 24))
        icon.addFile('assets/icon/32x32.png', QSize(32, 32))
        icon.addFile('assets/icon/48x48.png', QSize(48, 48))
        icon.addFile('assets/icon/256x256.png', QSize(256, 256))
        MCServerManagementWindow.setWindowIcon(icon)
        MCServerManagementWindow.setTabShape(QTabWidget.Rounded)
        self.actionlocalhost = QAction(MCServerManagementWindow)
        self.actionlocalhost.setObjectName(u"actionlocalhost")
        self.centralwidget = QWidget(MCServerManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.central_layout = QGridLayout()
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(10, -1, 10, -1)
        self.start_server_button = QPushButton(self.centralwidget)
        self.start_server_button.setObjectName(u"start_server_button")
        self.start_server_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_server_button.sizePolicy().hasHeightForWidth())
        self.start_server_button.setSizePolicy(sizePolicy)
        self.start_server_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_server_button.setStyleSheet(u"QPushButton {\n"
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

        self.central_layout.addWidget(self.start_server_button, 2, 0, 1, 1)

        self.console_log_box = QTextBrowser(self.centralwidget)
        self.console_log_box.setObjectName(u"console_log_box")
        self.console_log_box.setStyleSheet(u"QTextBrowser {\n"
"	background: #ececec;\n"
"	border: 3px;\n"
"	border-radius: 5px;\n"
"	border-style: solid;\n"
"	border-color: #ececec;\n"
"	margin: 10px 0 10px 0;\n"
"}\n"
"QScrollBar:vertical {\n"
"	background: #ececec;\n"
"	width:10px;\n"
"	border: 0px solid #ececec;\n"
"	width: 8px;    \n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #cecece;\n"
"	min-height: 0px;\n"
"	min-height: 0px;\n"
"	border: 0px solid black;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0 px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}")

        self.central_layout.addWidget(self.console_log_box, 4, 0, 1, 3)

        self.content_error_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_layout.addItem(self.content_error_spacer, 6, 0, 1, 5)

        self.stop_server_button = QPushButton(self.centralwidget)
        self.stop_server_button.setObjectName(u"stop_server_button")
        self.stop_server_button.setEnabled(False)
        self.stop_server_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_server_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 99, 71);\n"
"	color: rgb(254, 254, 254);\n"
"	border-style: none;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	height: 15px;\n"
"	width: 100%;\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: 	rgb(178,34,34);\n"
"	color: #cecece;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: 	rgb(178,34,34);\n"
"	color: #cecece;\n"
"}")

        self.central_layout.addWidget(self.stop_server_button, 2, 1, 1, 1)

        self.send_command_button = QPushButton(self.centralwidget)
        self.send_command_button.setObjectName(u"send_command_button")
        self.send_command_button.setEnabled(False)
        self.send_command_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_command_button.setStyleSheet(u"QPushButton {\n"
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

        self.central_layout.addWidget(self.send_command_button, 5, 2, 1, 1)

        self.top_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_layout.addItem(self.top_spacer, 0, 0, 1, 5)

        self.info_layout = QVBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.info_layout.setContentsMargins(5, 10, 0, 10)
        self.info_title_label = QLabel(self.centralwidget)
        self.info_title_label.setObjectName(u"info_title_label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setKerning(True)
        self.info_title_label.setFont(font)
        self.info_title_label.setStyleSheet(u"margin: 0px 0px 10px 0px;")
        self.info_title_label.setTextFormat(Qt.PlainText)

        self.info_layout.addWidget(self.info_title_label)

        self.status_layout = QHBoxLayout()
        self.status_layout.setObjectName(u"status_layout")
        self.status_text_label = QLabel(self.centralwidget)
        self.status_text_label.setObjectName(u"status_text_label")

        self.status_layout.addWidget(self.status_text_label)

        self.status_info_label = QLabel(self.centralwidget)
        self.status_info_label.setObjectName(u"status_info_label")
        self.status_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.status_layout.addWidget(self.status_info_label)


        self.info_layout.addLayout(self.status_layout)

        self.status_version_separator = QFrame(self.centralwidget)
        self.status_version_separator.setObjectName(u"status_version_separator")
        self.status_version_separator.setStyleSheet(u"color: rgb(236, 236, 236);\n"
"background-color: rgb(236, 236, 236);")
        self.status_version_separator.setFrameShadow(QFrame.Plain)
        self.status_version_separator.setLineWidth(0)
        self.status_version_separator.setFrameShape(QFrame.HLine)

        self.info_layout.addWidget(self.status_version_separator)

        self.version_layout = QHBoxLayout()
        self.version_layout.setObjectName(u"version_layout")
        self.version_text_label = QLabel(self.centralwidget)
        self.version_text_label.setObjectName(u"version_text_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.version_text_label.sizePolicy().hasHeightForWidth())
        self.version_text_label.setSizePolicy(sizePolicy1)

        self.version_layout.addWidget(self.version_text_label)

        self.version_info_label = QLabel(self.centralwidget)
        self.version_info_label.setObjectName(u"version_info_label")
        self.version_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.version_layout.addWidget(self.version_info_label)


        self.info_layout.addLayout(self.version_layout)

        self.version_motd_separator = QFrame(self.centralwidget)
        self.version_motd_separator.setObjectName(u"version_motd_separator")
        self.version_motd_separator.setStyleSheet(u"color: rgb(236, 236, 236);\n"
"background-color: rgb(236, 236, 236);")
        self.version_motd_separator.setFrameShadow(QFrame.Plain)
        self.version_motd_separator.setFrameShape(QFrame.HLine)

        self.info_layout.addWidget(self.version_motd_separator)

        self.motd_layout = QHBoxLayout()
        self.motd_layout.setObjectName(u"motd_layout")
        self.motd_text_label = QLabel(self.centralwidget)
        self.motd_text_label.setObjectName(u"motd_text_label")

        self.motd_layout.addWidget(self.motd_text_label)

        self.motd_info_label = QLabel(self.centralwidget)
        self.motd_info_label.setObjectName(u"motd_info_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.motd_info_label.sizePolicy().hasHeightForWidth())
        self.motd_info_label.setSizePolicy(sizePolicy2)
        self.motd_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.motd_layout.addWidget(self.motd_info_label)


        self.info_layout.addLayout(self.motd_layout)

        self.motd_playercount_separator = QFrame(self.centralwidget)
        self.motd_playercount_separator.setObjectName(u"motd_playercount_separator")
        self.motd_playercount_separator.setStyleSheet(u"color: rgb(236, 236, 236);\n"
"background-color: rgb(236, 236, 236);")
        self.motd_playercount_separator.setFrameShadow(QFrame.Plain)
        self.motd_playercount_separator.setFrameShape(QFrame.HLine)

        self.info_layout.addWidget(self.motd_playercount_separator)

        self.player_count_layout = QHBoxLayout()
        self.player_count_layout.setObjectName(u"player_count_layout")
        self.player_count_text_label = QLabel(self.centralwidget)
        self.player_count_text_label.setObjectName(u"player_count_text_label")

        self.player_count_layout.addWidget(self.player_count_text_label)

        self.player_count_info_label = QLabel(self.centralwidget)
        self.player_count_info_label.setObjectName(u"player_count_info_label")
        self.player_count_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.player_count_layout.addWidget(self.player_count_info_label)


        self.info_layout.addLayout(self.player_count_layout)

        self.playercount_onlineplayers_separator = QFrame(self.centralwidget)
        self.playercount_onlineplayers_separator.setObjectName(u"playercount_onlineplayers_separator")
        self.playercount_onlineplayers_separator.setStyleSheet(u"color: rgb(236, 236, 236);\n"
"background-color: rgb(236, 236, 236);")
        self.playercount_onlineplayers_separator.setFrameShadow(QFrame.Plain)
        self.playercount_onlineplayers_separator.setFrameShape(QFrame.HLine)

        self.info_layout.addWidget(self.playercount_onlineplayers_separator)

        self.online_players_layout = QHBoxLayout()
        self.online_players_layout.setObjectName(u"online_players_layout")
        self.online_players_text_label = QLabel(self.centralwidget)
        self.online_players_text_label.setObjectName(u"online_players_text_label")

        self.online_players_layout.addWidget(self.online_players_text_label)


        self.info_layout.addLayout(self.online_players_layout)

        self.online_players_info_box = QTextBrowser(self.centralwidget)
        self.online_players_info_box.setObjectName(u"online_players_info_box")
        self.online_players_info_box.setStyleSheet(u"QScrollBar:vertical {\n"
"	background: #ffffff;\n"
"	width:10px;\n"
"	border: 0px solid #ffffff;\n"
"	width: 8px;    \n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #cecece;\n"
"	min-height: 0px;\n"
"	min-height: 0px;\n"
"	border: 0px solid black;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0 px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}")
        self.online_players_info_box.setFrameShape(QFrame.NoFrame)

        self.info_layout.addWidget(self.online_players_info_box)


        self.central_layout.addLayout(self.info_layout, 4, 3, 1, 2)

        self.info_top_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_layout.addItem(self.info_top_spacer, 2, 4, 1, 1)

        self.server_name_label = QLabel(self.centralwidget)
        self.server_name_label.setObjectName(u"server_name_label")
        font1 = QFont()
        font1.setPointSize(17)
        self.server_name_label.setFont(font1)
        self.server_name_label.setStyleSheet(u"margin-bottom: 10px;")

        self.central_layout.addWidget(self.server_name_label, 1, 0, 1, 5)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(False)
        self.error_label.setMinimumSize(QSize(40, 20))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.error_label.setFont(font2)
        self.error_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.error_label.setFrameShape(QFrame.NoFrame)
        self.error_label.setMidLineWidth(0)
        self.error_label.setTextFormat(Qt.PlainText)
        self.error_label.setScaledContents(False)
        self.error_label.setAlignment(Qt.AlignCenter)

        self.central_layout.addWidget(self.error_label, 7, 0, 1, 5)

        self.server_files_button_layout = QHBoxLayout()
        self.server_files_button_layout.setObjectName(u"server_files_button_layout")
        self.server_files_left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.server_files_button_layout.addItem(self.server_files_left_spacer)

        self.server_files_button = QPushButton(self.centralwidget)
        self.server_files_button.setObjectName(u"server_files_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.server_files_button.sizePolicy().hasHeightForWidth())
        self.server_files_button.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setUnderline(True)
        self.server_files_button.setFont(font3)
        self.server_files_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.server_files_button.setStyleSheet(u"QPushButton {\n"
"	padding: 0px;\n"
"	color: #4834d4;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: 	#000080;\n"
"}")
        self.server_files_button.setFlat(True)

        self.server_files_button_layout.addWidget(self.server_files_button)

        self.server_files_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.server_files_button_layout.addItem(self.server_files_right_spacer)


        self.central_layout.addLayout(self.server_files_button_layout, 5, 4, 1, 1)

        self.send_command_input = QLineEdit(self.centralwidget)
        self.send_command_input.setObjectName(u"send_command_input")
        self.send_command_input.setEnabled(False)
        self.send_command_input.setStyleSheet(u"QLineEdit {\n"
"	height: 27px;\n"
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

        self.central_layout.addWidget(self.send_command_input, 5, 0, 1, 2)

        self.buttons_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_layout.addItem(self.buttons_right_spacer, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.central_layout, 2, 1, 1, 1)

        MCServerManagementWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MCServerManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        MCServerManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MCServerManagementWindow)

        QMetaObject.connectSlotsByName(MCServerManagementWindow)
    # setupUi

    def retranslateUi(self, MCServerManagementWindow):
        MCServerManagementWindow.setWindowTitle(QCoreApplication.translate("MCServerManagementWindow", u"*server name* control panel", None))
        self.actionlocalhost.setText(QCoreApplication.translate("MCServerManagementWindow", u"localhost", None))
        self.start_server_button.setText(QCoreApplication.translate("MCServerManagementWindow", u"Start server", None))
        self.console_log_box.setText("")
        self.stop_server_button.setText(QCoreApplication.translate("MCServerManagementWindow", u"Stop server", None))
        self.send_command_button.setText(QCoreApplication.translate("MCServerManagementWindow", u"Send", None))
        self.info_title_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"Info", None))
        self.status_text_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"Status: ", None))
        self.status_info_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"?", None))
        self.version_text_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"Version: ", None))
        self.version_info_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"?", None))
        self.motd_text_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"MOTD: ", None))
        self.motd_info_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"?", None))
        self.player_count_text_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"Players: ", None))
        self.player_count_info_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"?/?", None))
        self.online_players_text_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"Currently online:", None))
        self.online_players_info_box.setHtml(QCoreApplication.translate("MCServerManagementWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.server_name_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"*server name*", None))
        self.error_label.setText(QCoreApplication.translate("MCServerManagementWindow", u"Error", None))
        self.server_files_button.setText(QCoreApplication.translate("MCServerManagementWindow", u"Server files", None))
        self.send_command_input.setInputMask("")
        self.send_command_input.setPlaceholderText(QCoreApplication.translate("MCServerManagementWindow", u"Send command", None))
    # retranslateUi

    def set_console_box_text(self, text):
        self.console_log_box.setText(text)

    def append_console_box_text(self, text):
        return self.console_log_box.append(text)

    def set_players_box_text(self, text):
        self.online_players_info_box.setText(text)

    def append_players_box_text(self, text):
        return self.online_players_info_box.append(text)
