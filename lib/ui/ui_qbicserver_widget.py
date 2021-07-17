# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qbicserver_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_QbicServer_Widget(object):
    def setupUi(self, QbicServer_Widget):
        if not QbicServer_Widget.objectName():
            QbicServer_Widget.setObjectName(u"QbicServer_Widget")
        QbicServer_Widget.resize(270, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QbicServer_Widget.sizePolicy().hasHeightForWidth())
        QbicServer_Widget.setSizePolicy(sizePolicy)
        QbicServer_Widget.setMinimumSize(QSize(270, 200))
        QbicServer_Widget.setMaximumSize(QSize(270, 200))
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
        QbicServer_Widget.setPalette(palette)
        QbicServer_Widget.setAutoFillBackground(False)
        QbicServer_Widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 20px;\n"
"	border: 3px solid #ececec;\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color:#ececec;\n"
"}")
        self.verticalLayout = QVBoxLayout(QbicServer_Widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.name_info_label = QLabel(QbicServer_Widget)
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

        self.host_text_label = QLabel(QbicServer_Widget)
        self.host_text_label.setObjectName(u"host_text_label")
        self.host_text_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.host_text_label)

        self.host_info_label = QLabel(QbicServer_Widget)
        self.host_info_label.setObjectName(u"host_info_label")
        self.host_info_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")
        self.host_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.host_info_label)

        self.mcservers_text_label = QLabel(QbicServer_Widget)
        self.mcservers_text_label.setObjectName(u"mcservers_text_label")
        self.mcservers_text_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.mcservers_text_label)

        self.mcservers_info_label = QLabel(QbicServer_Widget)
        self.mcservers_info_label.setObjectName(u"mcservers_info_label")
        self.mcservers_info_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding: 0px;\n"
"border: 0px;\n"
"border-radius: 0px;")
        self.mcservers_info_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mcservers_info_label)

        self.label_button_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.label_button_spacer)

        self.open_button = QPushButton(QbicServer_Widget)
        self.open_button.setObjectName(u"open_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy1)
        self.open_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_button.setMouseTracking(True)
        self.open_button.setFocusPolicy(Qt.StrongFocus)
        self.open_button.setStyleSheet(u"QPushButton {\n"
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

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.open_button)

        self.bottom_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(6, QFormLayout.SpanningRole, self.bottom_spacer)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.horizontalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(QbicServer_Widget)

        QMetaObject.connectSlotsByName(QbicServer_Widget)
    # setupUi

    def retranslateUi(self, QbicServer_Widget):
        QbicServer_Widget.setWindowTitle(QCoreApplication.translate("QbicServer_Widget", u"Qbic Server Widget", None))
        self.name_info_label.setText(QCoreApplication.translate("QbicServer_Widget", u"*server name*", None))
        self.host_text_label.setText(QCoreApplication.translate("QbicServer_Widget", u"Host:", None))
        self.host_info_label.setText(QCoreApplication.translate("QbicServer_Widget", u"?", None))
        self.mcservers_text_label.setText(QCoreApplication.translate("QbicServer_Widget", u"MC servers:", None))
        self.mcservers_info_label.setText(QCoreApplication.translate("QbicServer_Widget", u"?", None))
        self.open_button.setText(QCoreApplication.translate("QbicServer_Widget", u"Open", None))
    # retranslateUi

