#!/usr/bin/python
# -*- coding: utf-8 -*-


import concurrent.futures
import subprocess
import sys
import validators.url
import threading
import urllib.request
from typing import Optional

from lib.utils import *

from PySide6.QtGui import QAction, QCursor, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLayout,\
    QSizePolicy, QSpacerItem, QMenu, QDialogButtonBox
from PySide6 import QtCore

from lib.ui.ui_login import Ui_LoginWindow
from lib.ui.ui_mcservers import Ui_MCServers_Window
from lib.ui.ui_mcserver_widget import Ui_MCServer_Widget
from lib.ui.ui_qbicserver_widget import Ui_QbicServer_Widget
from lib.ui.ui_create import Ui_CreateWindow
from lib.ui.ui_delete import Ui_DeleteDialog
from lib.ui.flowlayout import FlowLayout

if os.name == 'nt':
    import ctypes

    appid = 'lugli-maccaferri.qbic-desktop.1.0.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)


class LoginWindow(QMainWindow):
    def __init__(self, ui):
        super(LoginWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)

    def show_error(self, msg):
        self.ui.error_label.setVisible(False)
        self.ui.error_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.ui.error_label.setText(msg)
        self.ui.error_label.setVisible(True)
        self.ui.connect_button.setDisabled(False)

    def load_to_login_form(self, address, username, password=None):
        if address:
            self.ui.serveraddress_field.setText(address)
        if username:
            self.ui.username_field.setText(username)
        if password:
            self.ui.username_field.setText(password)

    def closeEvent(self, event):
        global infoloader
        if infoloader is not None:
            infoloader.set()
        event.accept()


class QbicServersWindow(QMainWindow):
    def __init__(self, ui):
        super(QbicServersWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        global infoloader
        if infoloader is not None:
            infoloader.set()
        event.accept()


class MCServersWindow(QMainWindow):
    def __init__(self, ui, name):
        super(MCServersWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)
        self.name = name
        self.menu: Optional[QMenu] = None

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        create_action = QAction('Create new server', self)
        create_action.triggered.connect(load_create_mcserver_ui)
        self.menu.addAction(create_action)
        self.menu.popup(QCursor.pos())

    def closeEvent(self, event):
        remove_from_infoload_executor_queue(self.name)
        if not info_loaders_queue:
            global infoloader
            if infoloader is not None:
                infoloader.set()
        window.show()
        event.accept()


class CreateMCServerWindow(QMainWindow):
    def __init__(self, ui):
        super(CreateMCServerWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)

    def show_error(self, msg):
        self.ui.error_label.setVisible(False)
        self.ui.error_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.ui.error_label.setText(msg)
        self.ui.error_label.setVisible(True)
        self.ui.create_button.setDisabled(False)


class MCServerWidget(QWidget, Ui_MCServer_Widget):
    def __init__(self, name, sid, parent=None):
        super(MCServerWidget, self).__init__(parent)
        self.setupUi(self)

        self.name = name
        self.id = sid
        self.menu: Optional[QMenu] = None
        self.icon_set = False

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        create_action = QAction('Delete server', self)
        create_action.triggered.connect(
            lambda name=self.name, sid=self.id: self.open_delete_dialog(name, sid)
        )
        self.menu.setStyleSheet(u"QMenu {\n"
                                "	background-color: none;\n"
                                "	padding: 5px;\n"
                                "	border: 0px;\n"
                                "	border-radius: 0px;\n"
                                "}\n"
                                "QWidget:hover {\n"
                                "	background-color: none;\n"
                                "}\n"
                                "QAction {\n"
                                "   \n"
                                "}")
        self.menu.addAction(create_action)
        self.menu.popup(QCursor.pos())

    def open_delete_dialog(self, name, sid):
        d = DeleteDialog(name, sid)
        d.exec()

    def load_icon_from_url(self, url):
        self.icon_set = True
        try:
            data = urllib.request.urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.picture_label.setPixmap(pixmap)
        except Exception as e:
            print("Error while loading server icon from url \"" + url + "\"")
            print("\t" + str(e))


class QbicServerWidget(QWidget, Ui_QbicServer_Widget):
    def __init__(self, parent=None):
        super(QbicServerWidget, self).__init__(parent)
        self.setupUi(self)


class DeleteDialog(QDialog, Ui_DeleteDialog):
    def __init__(self, name, sid):
        QDialog.__init__(self)
        self.setupUi(self)

        self.sid = sid

        self.label.setText("Do you really want to delete the minecraft server "
                           + name + " from the Qbic server " + current_qbic_name + "?")
        self.buttonBox.button(QDialogButtonBox.Yes).setStyleSheet("QPushButton {\n"
                                                                  " background: rgb(255, 99, 71);\n"
                                                                  "}\n"
                                                                  "QPushButton:disabled {\n"
                                                                  "	background-color: 	rgb(178,34,34);\n"
                                                                  "	color: #cecece;\n"
                                                                  "}\n"
                                                                  "QPushButton:pressed {\n"
                                                                  "	background-color: 	rgb(178,34,34);\n"
                                                                  "	color: #cecece;\n"
                                                                  "}\n")
        self.buttonBox.accepted.connect(self.on_delete_click)
        self.buttonBox.rejected.connect(self.close)

    def on_delete_click(self):
        try:
            tokenized_get_post_request(False, current_qbic_host, "/server/" + self.sid, None, token, True)
        except Exception as e:
            print("Error: " + str(e))
            return

        # t = threading.Timer(5.0, load_mcservers_ui, (None, current_qbic_name, current_qbic_host))
        # t.start()


class JFlowLayout(FlowLayout):
    # flow layout, similar to an HTML `<DIV>`
    # this is our "wrapper" to the `FlowLayout` sample Qt code we have implemented
    # we use it in place of where we used to use a `QHBoxLayout`
    # in order to make few outside-world changes, and revert to `QHBoxLayout`if we ever want to,
    # there are a couple of methods here which are available on a `QBoxLayout` but not on a `QLayout`
    # for which we provide a "lite-equivalent" which will suffice for our purposes

    def addLayout(self, layout: QLayout, stretch: int = 0):
        # "equivalent" of `QBoxLayout.addLayout()`
        # we want to add sub-layouts (e.g. a `QVBoxLayout` holding a label above a widget)
        # there is some dispute as to how to do this/whether it is supported by `FlowLayout`
        # see my https://forum.qt.io/topic/104653/how-to-do-a-no-break-qhboxlayout
        # there is a suggestion that we should not add a sub-layout but rather enclose it in a `QWidget`
        # but since it seems to be working as I've done it below I'm elaving it at that for now...

        # suprisingly to me, we do not need to add the layout via `addChildLayout()`, that seems to make no difference
        # self.addChildLayout(layout)
        # all that seems to be reuqired is to add it onto the list via `addItem()`
        self.addItem(layout)

    def addStretch(self, stretch: int = 0):
        # "equivalent" of `QBoxLayout.addStretch()`
        # we can't do stretches, we just arbitrarily put in a "spacer" to give a bit of a gap
        w = stretch * 20
        spacerItem = QSpacerItem(w, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.addItem(spacerItem)


def add_to_infoload_executor_queue(data):
    global info_loaders_queue

    for item in data:

        name = item[0]

        if name not in info_loaders_queue.keys():
            info_loaders_queue[name] = []

        if item not in info_loaders_queue[name]:
            info_loaders_queue[name].append(item)


def remove_from_infoload_executor_queue(name):
    global info_loaders_queue

    info_loaders_queue.pop(name, None)


def infoloader_f(il):
    global info_loaders_queue
    for name in info_loaders_queue.keys():
        try:
            for data in info_loaders_queue[name]:
                info_loaders.submit(load_mc_server_info, *data)
        except Exception as e:
            print(str(e))

    if not il.is_set():
        threading.Timer(5, infoloader_f, [il]).start()


def load_mc_server_info(name, host, sid):
    route = "/server/info/" + sid

    try:
        data = get_post_request(True, host, route)

        if data["success"]:
            qbic_windows[name].ui.server_widgets[sid].status_info_label.setText("Running")
            qbic_windows[name].ui.server_widgets[sid].status_info_label.setStyleSheet(u"color: rgb(0, 100, 0);\n"
                                                                                      "background-color: "
                                                                                      "rgba(255, 255, 255, 0);\n"
                                                                                      "padding: 0px;\n"
                                                                                      "border: 0px;\n"
                                                                                      "border-radius: 0px;")
        else:
            raise Exception("500")

        qbic_windows[name].ui.server_widgets[sid].version_info_label.setText(data["version"])
        qbic_windows[name].ui.server_widgets[sid].player_count_info_label.setText(str(data["online_players"])
                                                                                 + "/" + str(data["max_players"]))

        try:
            if not qbic_windows[name].ui.server_widgets[sid].icon_set:
                qbic_windows[name].ui.server_widgets[sid].load_icon_from_url(current_qbic_host.rstrip("/")
                                                                             + "/" + data["server_icon"].lstrip("/"))
        except Exception:
            return

    except Exception as e:
        if "500" in str(e):
            qbic_windows[name].ui.server_widgets[sid].version_info_label.setText("-")
            qbic_windows[name].ui.server_widgets[sid].player_count_info_label.setText("-")
            qbic_windows[name].ui.server_widgets[sid].status_info_label.setText("Offline")
            qbic_windows[name].ui.server_widgets[sid].status_info_label.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                                                                      "background-color: "
                                                                                      "rgba(255, 255, 255, 0);\n"
                                                                                      "padding: 0px;\n"
                                                                                      "border: 0px;\n"
                                                                                      "border-radius: 0px;")
            return

        print("Error while loading info for the MC server with id \"" + sid + "\"")
        print("\t" + str(e))


def on_connect_click():
    window.ui.connect_button.setDisabled(True)
    window.ui.error_label.setVisible(False)

    window.ui.error_label.setText("Connecting...")
    window.ui.error_label.setStyleSheet(u"color: rgb(255, 204, 0);")
    window.ui.error_label.setVisible(True)

    address = window.ui.serveraddress_field.text().strip()
    username = window.ui.username_field.text().strip()
    password = window.ui.password_field.text().strip()

    if not address or not username or not password:
        window.show_error("Error: One or more fields are empty")
        return

    if not address.startswith("https://") and not address.startswith("http://"):
        address = "https://" + address

    if not validators.url(address):
        window.show_error("Error: Invalid server address")
        return

    global token
    try:
        token = login_connect(address, username, password)
        global server_address
        server_address = address
    except Exception as e:
        window.show_error("Error: " + str(e))
        return

    if token is None:
        window.show_error("Error: Unknown error")
        return

    password = None

    global qbic_servers
    qbic_servers = get_post_request(True, server_address, "/nodes")

    if qbic_servers is not None:
        try:
            qbic_servers = qbic_servers["nodes"]
        except KeyError:
            qbic_servers = None

    if qbic_servers is None:
        window.show_error("Error: Failed to retrieve connected qbic nodes")
        return

    add_to_recent(server_address, username, recent_filename)

    load_qbicservers_ui()


def on_create_click():
    create_mcserver_window.ui.create_button.setDisabled(True)
    create_mcserver_window.ui.error_label.setVisible(False)

    create_mcserver_window.ui.error_label.setText("Creating...")
    create_mcserver_window.ui.error_label.setStyleSheet(u"color: rgb(255, 204, 0);")
    create_mcserver_window.ui.error_label.setVisible(True)

    name = create_mcserver_window.ui.name_field.text().strip()
    server_port = int(create_mcserver_window.ui.server_port_field.text().strip())
    query_port = int(create_mcserver_window.ui.query_port_field.text().strip())
    rcon_port = int(create_mcserver_window.ui.rcon_port_field.text().strip())
    max_ram = create_mcserver_window.ui.max_ram_field.text().strip()
    min_ram = create_mcserver_window.ui.min_ram_field.text().strip()
    jar_path = create_mcserver_window.ui.jar_path_field.text().strip()

    if not name or not server_port or not query_port or not rcon_port or not max_ram or not min_ram or not jar_path:
        create_mcserver_window.show_error("Error: One or more fields are empty")
        return

    if server_port not in range(0, 65535) or query_port not in range(0, 65535) or rcon_port not in range(0, 65535):
        create_mcserver_window.show_error("Error: One or more ports are invalid")
        return

    if server_port == query_port or query_port == rcon_port or server_port == rcon_port:
        create_mcserver_window.show_error("Error: All ports must be different")
        return

    data = {
        "name": name,
        "query-port": query_port,
        "server-port": server_port,
        "rcon-port": rcon_port,
        "xmx": max_ram,
        "xms": min_ram,
        "jar_path": jar_path
    }

    try:
        r = tokenized_get_post_request(False, current_qbic_host, "/server/create", data, token)
    except Exception as e:
        create_mcserver_window.show_error("Error: " + str(e))
        return

    try:
        if r["success"]:
            create_mcserver_window.ui.create_button.setEnabled(False)
            create_mcserver_window.ui.error_label.setStyleSheet(u"color: rgb(0, 100, 0);\n")
            create_mcserver_window.ui.error_label.setText("Server created successfully\n "
                                                          "Close and reopen the qbic server window to see it...")
            # t = threading.Timer(10.0, load_mcservers_ui, (None, current_qbic_name, current_qbic_host))
            # t.start()
        else:
            create_mcserver_window.ui.create_button.setEnabled(True)
            create_mcserver_window.ui.error_label.setText("Server creation failed")

        create_mcserver_window.ui.error_label.setVisible(True)

    except Exception as e:
        create_mcserver_window.show_error("Error: " + str(e))


def load_login_ui():
    global window
    window = LoginWindow(Ui_LoginWindow)

    window.ui.error_label.setVisible(False)
    window.ui.connect_button.clicked.connect(on_connect_click)

    lines = []

    if os.path.exists(recent_filename):
        with open(recent_filename) as f:
            lines = f.readlines()

    i = 0
    for line in lines:
        if not line.strip():
            continue

        address = line.split(' ')[0]
        user = line.split(' ')[1]

        line = address + user

        window.ui.actions = {}
        if address and user:
            window.ui.actions[line] = QAction(window)
            window.ui.actions[line].setObjectName(address + " - " + user)
            window.ui.actions[line].setText(address + " - " + user)
            window.ui.actions[line].triggered.connect(
                lambda ad=address, us=user: window.load_to_login_form(ad, us)
            )
            window.ui.menuRecent.addAction(window.ui.actions[line])
            i += 1

    window.show()


def load_qbicservers_ui():
    global window
    window = QbicServersWindow(Ui_MCServers_Window)

    window.ui.flowLayout = JFlowLayout(window.ui.scrollAreaWidgetContents)
    window.ui.flowLayout.setObjectName(u"flowLayout")
    window.ui.scrollArea.setWidget(window.ui.scrollAreaWidgetContents)

    window.ui.server_widgets = {}
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    for node in qbic_servers:
        name = node["name"]
        host = node["host"]

        tmp = name

        i = 0
        while tmp in window.ui.server_widgets.keys():
            i += 1
            tmp = name + " (" + str(i) + ")"

        name = tmp

        window.ui.server_widgets[name] = QbicServerWidget()
        window.ui.server_widgets[name].setAttribute(QtCore.Qt.WA_StyledBackground)
        window.ui.server_widgets[name].setObjectName(u"server_widget_" + name)
        window.ui.server_widgets[name].name_info_label.setText(name)
        window.ui.server_widgets[name].host_info_label.setText(host)
        window.ui.server_widgets[name].mcservers_info_label.setText("?")
        window.ui.server_widgets[name].open_button.clicked.connect(
            lambda x="", n=name, h=host: load_mcservers_ui(x, n, h)
        )
        window.ui.server_widgets[name].open_button.setEnabled(False)
        window.ui.flowLayout.addWidget(window.ui.server_widgets[name])

        label = window.ui.server_widgets[name].mcservers_info_label
        button = window.ui.server_widgets[name].open_button
        executor.submit(load_underlying_mc_servers_number, label, host, button)

    window.show()


def load_mcservers_ui(x, name, host):
    global qbic_windows

    if name in qbic_windows.keys():
        if qbic_windows[name].isVisible():
            qbic_windows[name].show()
            window.setWindowState(window.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
            qbic_windows[name].raise_()
            qbic_windows[name].activateWindow()
            return

    qbic_windows[name] = MCServersWindow(Ui_MCServers_Window, name)
    qbic_windows[name].setObjectName("MC Servers of \"" + name + "\" (" + host + ")")
    qbic_windows[name].setWindowTitle("MC Servers of \"" + name + "\" (" + host + ")")

    qbic_windows[name].ui.flowLayout = JFlowLayout(qbic_windows[name].ui.scrollAreaWidgetContents)
    qbic_windows[name].ui.flowLayout.setObjectName(u"flowLayout")
    qbic_windows[name].ui.scrollArea.setWidget(qbic_windows[name].ui.scrollAreaWidgetContents)

    route = "/server/list"
    try:
        servers = get_post_request(True, host, route)["servers"]
    except Exception as e:
        print(str(e))
        return

    info_loaders_data = []

    qbic_windows[name].ui.server_widgets = {}
    for server in servers:
        server_id = server["id"]
        server_name = server["name"]
        qbic_windows[name].ui.server_widgets[server_id] = MCServerWidget(server_name, server_id)
        qbic_windows[name].ui.server_widgets[server_id].setObjectName(u"server_widget_" + server_id)

        qbic_windows[name].ui.server_widgets[server_id].setAttribute(QtCore.Qt.WA_StyledBackground)

        qbic_windows[name].ui.server_widgets[server_id].name_info_label.setText(server_name)
        qbic_windows[name].ui.server_widgets[server_id].version_info_label.setText("?")
        qbic_windows[name].ui.server_widgets[server_id].status_info_label.setText("?")
        qbic_windows[name].ui.server_widgets[server_id].player_count_info_label.setText("?")

        qbic_windows[name].ui.server_widgets[server_id].manage_button.clicked.connect(
            lambda n=server_name, h=host, s=server_id: load_mcserver_management_ui(n, h, s)
        )

        qbic_windows[name].ui.flowLayout.addWidget(qbic_windows[name].ui.server_widgets[server_id])

        info_loaders_data.append((name, host, server_id))

    global current_qbic_host, current_qbic_name
    current_qbic_host = host
    current_qbic_name = name

    window.hide()
    qbic_windows[name].show()

    add_to_infoload_executor_queue(info_loaders_data)

    global infoloader
    if infoloader is None:
        infoloader = threading.Event()
        infoloader_f(infoloader)
    if infoloader.is_set():
        infoloader.clear()
        infoloader_f(infoloader)


def load_create_mcserver_ui():
    global create_mcserver_window

    create_mcserver_window = CreateMCServerWindow(Ui_CreateWindow)

    create_mcserver_window.ui.error_label.setVisible(False)
    create_mcserver_window.ui.create_button.clicked.connect(on_create_click)

    create_mcserver_window.show()


def load_delete_mcserver_ui(sid):
    global create_mcserver_window

    create_mcserver_window = CreateMCServerWindow(Ui_CreateWindow)

    create_mcserver_window.ui.error_label.setVisible(False)
    create_mcserver_window.ui.create_button.clicked.connect(on_create_click)

    create_mcserver_window.show()


def load_mcserver_management_ui(name, host, sid):
    global server_management_processes
    server_management_processes[name + "-" + sid] = subprocess.Popen('python lib/server_management.py '
                                                                     + host + ' ' + sid + ' '
                                                                     + token + ' \"' + name + '\"', shell=True)


if __name__ == "__main__":
    recent_filename = "data/recent.list"

    window: Optional[LoginWindow] = None
    create_mcserver_window: Optional[CreateMCServerWindow] = None
    #delete_mcserver_window: Optional[DeleteMCServerWindow] = None
    qbic_windows = {}
    mcserves_management_windows = {}

    server_management_processes = {}

    server_address: Optional[str] = None
    token: Optional[str] = None

    qbic_servers: Optional[list] = None
    current_qbic_host: Optional[str] = None
    current_qbic_name: Optional[str] = None

    infoloader: Optional[threading.Event] = None
    info_loaders = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    info_loaders_queue = {}

    app = QApplication(sys.argv)

    load_login_ui()

    sys.exit(app.exec())
