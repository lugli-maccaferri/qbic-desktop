# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serverfiles.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class FileLabel(QLabel):
    def __init__(self, parent=None, name=None, function=None):
        self.name = name
        self.function = function
        QLabel.__init__(self, parent)

    def mousePressEvent(self, event):
        if self.name is not None:
            self.function(False, self.name)


class Ui_ServerFilesWindow(object):
    def setupUi(self, ServerFilesWindow):
        if not ServerFilesWindow.objectName():
            ServerFilesWindow.setObjectName(u"ServerFilesWindow")
        ServerFilesWindow.resize(896, 796)
        ServerFilesWindow.setBaseSize(QSize(863, 0))
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
        ServerFilesWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"assets/icon/600x600.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile('assets/icon/16x16.png', QSize(16, 16))
        icon.addFile('assets/icon/24x24.png', QSize(24, 24))
        icon.addFile('assets/icon/32x32.png', QSize(32, 32))
        icon.addFile('assets/icon/48x48.png', QSize(48, 48))
        icon.addFile('assets/icon/256x256.png', QSize(256, 256))
        ServerFilesWindow.setWindowIcon(icon)
        ServerFilesWindow.setTabShape(QTabWidget.Rounded)
        self.actionlocalhost = QAction(ServerFilesWindow)
        self.actionlocalhost.setObjectName(u"actionlocalhost")
        self.centralwidget = QWidget(ServerFilesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.central_layout = QGridLayout()
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(10, -1, 10, -1)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(17)
        self.title_label.setFont(font)
        self.title_label.setCursor(QCursor(Qt.ArrowCursor))
        self.title_label.setStyleSheet(u"margin: 15px 0px 10px 0px;")

        self.central_layout.addWidget(self.title_label, 0, 0, 1, 2)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(False)
        self.sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.sizePolicy1.setHorizontalStretch(0)
        self.sizePolicy1.setVerticalStretch(0)
        self.sizePolicy1.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(self.sizePolicy1)
        self.error_label.setMinimumSize(QSize(40, 20))
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

        self.central_layout.addWidget(self.error_label, 4, 0, 1, 2)

        self.current_path_label = QLabel(self.centralwidget)
        self.current_path_label.setObjectName(u"current_path_label")
        self.sizePolicy1.setHeightForWidth(self.current_path_label.sizePolicy().hasHeightForWidth())
        self.current_path_label.setSizePolicy(self.sizePolicy1)
        font2 = QFont()
        font2.setUnderline(True)
        self.current_path_label.setFont(font2)
        self.current_path_label.setStyleSheet(u"margin-bottom: 10px")

        self.central_layout.addWidget(self.current_path_label, 1, 0, 1, 1)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy2)
        self.back_button.setMinimumSize(QSize(0, 17))
        self.back_button.setMaximumSize(QSize(50, 16777215))
        self.back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75, 52, 212);\n"
"	color: rgb(254, 254, 254);\n"
"	border-style: none;\n"
"	border-radius: 2px;\n"
"	padding: 2px;\n"
"	height: 10px;\n"
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

        self.central_layout.addWidget(self.back_button, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet(
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
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 852, 619))
        self.scrollAreaWidgetContents.setStyleSheet(
"QWidget {\n"
"   background-color: #ffffff"
"}\n")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 20)

        self.files = []

        self.files_error_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.central_layout.addWidget(self.scrollArea, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.central_layout, 2, 1, 1, 1)

        ServerFilesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ServerFilesWindow)
        self.statusbar.setObjectName(u"statusbar")
        ServerFilesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ServerFilesWindow)

        QMetaObject.connectSlotsByName(ServerFilesWindow)
    # setupUi

    def retranslateUi(self, ServerFilesWindow):
        ServerFilesWindow.setWindowTitle(QCoreApplication.translate("ServerFilesWindow", u"Browsing *servername*'s files", None))
        self.actionlocalhost.setText(QCoreApplication.translate("ServerFilesWindow", u"localhost", None))
        self.title_label.setText(QCoreApplication.translate("ServerFilesWindow", u"*server name*'s files", None))
        self.error_label.setText(QCoreApplication.translate("ServerFilesWindow", u"Error", None))
        self.current_path_label.setText(QCoreApplication.translate("ServerFilesWindow", u"/", None))
        self.back_button.setText(QCoreApplication.translate("ServerFilesWindow", u"Back", None))
    # retranslateUi

    def add_file(self, name, function):
        file = FileLabel(self.centralwidget, name, function)
        sep = QFrame(self.centralwidget)

        file.setText(name)
        file.setObjectName(u"file_label_" + name)
        self.sizePolicy1.setHeightForWidth(file.sizePolicy().hasHeightForWidth())
        file.setSizePolicy(self.sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        file.setFont(font3)
        file.setCursor(QCursor(Qt.PointingHandCursor))
        file.setStyleSheet(u"")
        file.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        sep.setObjectName(u"files_separator_" + name)
        self.sizePolicy1.setHeightForWidth(sep.sizePolicy().hasHeightForWidth())
        sep.setSizePolicy(self.sizePolicy1)
        sep.setMinimumSize(QSize(0, 37))
        sep.setStyleSheet(u"margin-bottom: 20px;\n"
                                             "padding-top: 15px;\n"
                                             "border: 2px solid #ececec;\n"
                                             "border-top: 0px;\n"
                                             "border-right: 0px;\n"
                                             "border-left: 0px;")
        sep.setFrameShadow(QFrame.Plain)
        sep.setFrameShape(QFrame.HLine)

        self.files.append( (file, sep) )

        return

        self.file_label_1 = QLabel(self.centralwidget)
        self.file_label_1.setObjectName(u"file_label_1")
        self.sizePolicy1.setHeightForWidth(self.file_label_1.sizePolicy().hasHeightForWidth())
        self.file_label_1.setSizePolicy(self.sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        self.file_label_1.setFont(font3)
        self.file_label_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.file_label_1.setStyleSheet(u"")
        self.file_label_1.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.files_layout.addWidget(self.file_label_1)

        self.files_separator_1 = QFrame(self.centralwidget)
        self.files_separator_1.setObjectName(u"files_separator_1")
        self.sizePolicy1.setHeightForWidth(self.files_separator_1.sizePolicy().hasHeightForWidth())
        self.files_separator_1.setSizePolicy(self.sizePolicy1)
        self.files_separator_1.setMinimumSize(QSize(0, 37))
        self.files_separator_1.setStyleSheet(u"margin-bottom: 20px;\n"
                                             "padding-top: 15px;\n"
                                             "border: 2px solid #ececec;\n"
                                             "border-top: 0px;\n"
                                             "border-right: 0px;\n"
                                             "border-left: 0px;")
        self.files_separator_1.setFrameShadow(QFrame.Plain)
        self.files_separator_1.setFrameShape(QFrame.HLine)

        self.files_layout.addWidget(self.files_separator_1)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def reload_files(self):
        self.clear_layout(self.verticalLayout_2)
        for file, separator in self.files:
            self.verticalLayout_2.addWidget(file)
            self.verticalLayout_2.addWidget(separator)
        self.verticalLayout_2.addItem(self.files_error_spacer)
