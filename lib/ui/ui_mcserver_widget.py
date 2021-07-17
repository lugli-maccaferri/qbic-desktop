# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mcserver_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MCServer_Widget(object):
    def setupUi(self, MCServer_Widget):
        if not MCServer_Widget.objectName():
            MCServer_Widget.setObjectName(u"MCServer_Widget")
        MCServer_Widget.resize(270, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MCServer_Widget.sizePolicy().hasHeightForWidth())
        MCServer_Widget.setSizePolicy(sizePolicy)
        MCServer_Widget.setMinimumSize(QSize(270, 310))
        MCServer_Widget.setMaximumSize(QSize(270, 400))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush2 = QBrush(QColor(239, 242, 244, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(111, 115, 116, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(149, 153, 155, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush5 = QBrush(QColor(255, 255, 220, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(223, 230, 233, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        MCServer_Widget.setPalette(palette)
        MCServer_Widget.setAutoFillBackground(False)
        MCServer_Widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 20px;\n"
"	border: 3px solid #ececec;\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color:#ececec;\n"
"}")
        self.verticalLayout = QVBoxLayout(MCServer_Widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.picture_layout = QHBoxLayout()
        self.picture_layout.setObjectName(u"picture_layout")
        self.picture_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.picture_layout.setContentsMargins(10, 10, 10, -1)
        self.picture_left_spacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.picture_layout.addItem(self.picture_left_spacer)

        self.picture_label = QLabel(MCServer_Widget)
        self.picture_label.setObjectName(u"picture_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.picture_label.sizePolicy().hasHeightForWidth())
        self.picture_label.setSizePolicy(sizePolicy1)
        self.picture_label.setMinimumSize(QSize(100, 100))
        self.picture_label.setMaximumSize(QSize(100, 100))
        self.picture_label.setStyleSheet(u"padding: 0px;\n"
"border: 1px solid grey;\n"
"border-radius: 0px;")
        self.picture_label.setFrameShape(QFrame.Box)
        self.picture_label.setFrameShadow(QFrame.Plain)
        self.picture_label.setLineWidth(1)
        self.picture_label.setTextFormat(Qt.RichText)
        self.picture_label.setPixmap(QPixmap(u"assets/default_server_icon.png"))
        self.picture_label.setScaledContents(True)
        self.picture_label.setWordWrap(False)

        self.picture_layout.addWidget(self.picture_label)

        self.picture_right_spacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.picture_layout.addItem(self.picture_right_spacer)


        self.verticalLayout.addLayout(self.picture_layout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, -1, 10, 10)
        self.name_info_label = QLabel(MCServer_Widget)
        self.name_info_label.setObjectName(u"name_info_label")
        self.name_info_label.setMinimumSize(QSize(0, 49))
        font = QFont()
        font.setPointSize(12)
        self.name_info_label.setFont(font)
        self.name_info_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;\n"
"margin: 15px 0px 15px 0px;")
        self.name_info_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.name_info_label)

        self.version_text_label = QLabel(MCServer_Widget)
        self.version_text_label.setObjectName(u"version_text_label")
        self.version_text_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.version_text_label)

        self.version_info_label = QLabel(MCServer_Widget)
        self.version_info_label.setObjectName(u"version_info_label")
        self.version_info_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")
        self.version_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.version_info_label)

        self.status_text_label = QLabel(MCServer_Widget)
        self.status_text_label.setObjectName(u"status_text_label")
        self.status_text_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.status_text_label)

        self.status_info_label = QLabel(MCServer_Widget)
        self.status_info_label.setObjectName(u"status_info_label")
        self.status_info_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")
        self.status_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.status_info_label)

        self.player_count_text_label = QLabel(MCServer_Widget)
        self.player_count_text_label.setObjectName(u"player_count_text_label")
        self.player_count_text_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.player_count_text_label)

        self.player_count_info_label = QLabel(MCServer_Widget)
        self.player_count_info_label.setObjectName(u"player_count_info_label")
        self.player_count_info_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")
        self.player_count_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.player_count_info_label)

        self.manage_button = QPushButton(MCServer_Widget)
        self.manage_button.setObjectName(u"manage_button")
        self.manage_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.manage_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75, 52, 212);\n"
"	color: rgb(250, 250, 250);\n"
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

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.manage_button)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.horizontalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(MCServer_Widget)

        QMetaObject.connectSlotsByName(MCServer_Widget)
    # setupUi

    def retranslateUi(self, MCServer_Widget):
        MCServer_Widget.setWindowTitle(QCoreApplication.translate("MCServer_Widget", u"Minecraft Server Widget", None))
        self.name_info_label.setText(QCoreApplication.translate("MCServer_Widget", u"*server name*", None))
        self.version_text_label.setText(QCoreApplication.translate("MCServer_Widget", u"Version: ", None))
        self.version_info_label.setText(QCoreApplication.translate("MCServer_Widget", u"?", None))
        self.status_text_label.setText(QCoreApplication.translate("MCServer_Widget", u"Status: ", None))
        self.status_info_label.setText(QCoreApplication.translate("MCServer_Widget", u"?", None))
        self.player_count_text_label.setText(QCoreApplication.translate("MCServer_Widget", u"Players online: ", None))
        self.player_count_info_label.setText(QCoreApplication.translate("MCServer_Widget", u"?/?", None))
        self.manage_button.setText(QCoreApplication.translate("MCServer_Widget", u"Manage", None))
    # retranslateUi

