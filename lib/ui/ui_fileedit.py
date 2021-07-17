# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileedit.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_FileEditWindow(object):
    def setupUi(self, FileEditWindow):
        if not FileEditWindow.objectName():
            FileEditWindow.setObjectName(u"FileEditWindow")
        FileEditWindow.resize(896, 796)
        FileEditWindow.setBaseSize(QSize(863, 0))
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
        FileEditWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"assets/icon/600x600.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile('assets/icon/16x16.png', QSize(16, 16))
        icon.addFile('assets/icon/24x24.png', QSize(24, 24))
        icon.addFile('assets/icon/32x32.png', QSize(32, 32))
        icon.addFile('assets/icon/48x48.png', QSize(48, 48))
        icon.addFile('assets/icon/256x256.png', QSize(256, 256))
        FileEditWindow.setWindowIcon(icon)
        FileEditWindow.setTabShape(QTabWidget.Rounded)
        self.actionlocalhost = QAction(FileEditWindow)
        self.actionlocalhost.setObjectName(u"actionlocalhost")
        self.centralwidget = QWidget(FileEditWindow)
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

        self.central_layout.addWidget(self.title_label, 0, 0, 1, 3)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy1)
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

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 25))
        self.pushButton.setMaximumSize(QSize(75, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2ecc71;\n"
"	color: rgb(254, 254, 254);\n"
"	border-style: none;\n"
"	border-radius: 2px;\n"
"	padding: 2px;\n"
"	height: 10px;\n"
"	width: 100%;\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: 	#27ae60;\n"
"	color: #cecece;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: 	#27ae60;\n"
"	color: #cecece;\n"
"}")

        self.central_layout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy2)
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

        self.central_layout.addWidget(self.error_label, 4, 0, 1, 3)

        self.current_path_label = QLabel(self.centralwidget)
        self.current_path_label.setObjectName(u"current_path_label")
        sizePolicy2.setHeightForWidth(self.current_path_label.sizePolicy().hasHeightForWidth())
        self.current_path_label.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setUnderline(True)
        self.current_path_label.setFont(font3)
        self.current_path_label.setStyleSheet(u"margin-bottom: 10px")

        self.central_layout.addWidget(self.current_path_label, 1, 0, 1, 1)

        self.files_layout = QVBoxLayout()
        self.files_layout.setSpacing(0)
        self.files_layout.setObjectName(u"files_layout")
        self.files_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.files_layout.setContentsMargins(0, 20, 0, 20)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	background: #ececec;\n"
"	border: 3px;\n"
"	border-radius: 5px;\n"
"	border-style: solid;\n"
"	border-color: #ececec;\n"
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

        self.files_layout.addWidget(self.textEdit)


        self.central_layout.addLayout(self.files_layout, 3, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.central_layout.addItem(self.horizontalSpacer, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.central_layout, 2, 1, 1, 1)

        FileEditWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FileEditWindow)
        self.statusbar.setObjectName(u"statusbar")
        FileEditWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FileEditWindow)

        QMetaObject.connectSlotsByName(FileEditWindow)
    # setupUi

    def retranslateUi(self, FileEditWindow):
        FileEditWindow.setWindowTitle(QCoreApplication.translate("FileEditWindow", u"Editing file *filename*", None))
        self.actionlocalhost.setText(QCoreApplication.translate("FileEditWindow", u"localhost", None))
        self.title_label.setText(QCoreApplication.translate("FileEditWindow", u"*filename*", None))
        self.back_button.setText(QCoreApplication.translate("FileEditWindow", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("FileEditWindow", u"Save", None))
        self.error_label.setText(QCoreApplication.translate("FileEditWindow", u"Error", None))
        self.current_path_label.setText(QCoreApplication.translate("FileEditWindow", u"/", None))
        self.textEdit.setHtml(QCoreApplication.translate("FileEditWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

    def on_text_changed(self):
        if not self.title_label.text().endswith("*"):
            self.title_label.setText(self.title_label.text() + " *")
        self.pushButton.setEnabled(True)

    def on_file_saved(self):
        self.title_label.setText(self.title_label.text().rstrip(" *"))
        self.pushButton.setEnabled(False)
