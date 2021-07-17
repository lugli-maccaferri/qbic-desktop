# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DeleteDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Deleting server")
        Dialog.resize(306, 119)
        Dialog.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"assets/icon/600x600.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile('assets/icon/16x16.png', QSize(16, 16))
        icon.addFile('assets/icon/24x24.png', QSize(24, 24))
        icon.addFile('assets/icon/32x32.png', QSize(32, 32))
        icon.addFile('assets/icon/48x48.png', QSize(48, 48))
        icon.addFile('assets/icon/256x256.png', QSize(256, 256))
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75, 52, 212);\n"
"	color: rgb(254, 254, 254);\n"
"	border-style: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
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
"}\n")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Deleting mc server", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Do you really want to delete the minecraft server *minecraft_server_name* from the Qbic server *qbic_server_name*?", None))
    # retranslateUi

