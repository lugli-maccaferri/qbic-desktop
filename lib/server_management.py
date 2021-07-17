#!/usr/bin/python
# -*- coding: utf-8 -*-

import concurrent.futures
import sys
import threading
import base64
import asyncio
import websockets
import time
from typing import Optional

from utils import *

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
from ui.ui_mcservermanagement import Ui_MCServerManagementWindow
from ui.ui_serverfiles import Ui_ServerFilesWindow
from ui.ui_fileedit import Ui_FileEditWindow

import ctypes

appid = 'lugli-maccaferri.qbic-desktop.1.0.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)


class MainWindow(QMainWindow):
    def __init__(self, ui):
        super(MainWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)

        self.ui.send_command_input.installEventFilter(self)

        self.console_signal = ConsoleSignal()
        self.console_signal.replace_sig.connect(self.set_console_box_text)
        self.console_signal.append_sig.connect(self.append_console_box_text)

        self.players_signal = PlayersSignal()
        self.players_signal.replace_sig.connect(self.set_players_box_text)
        self.players_signal.append_sig.connect(self.append_players_box_text)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.send_command_input:
            if event.key() == QtCore.Qt.Key_Return and self.ui.send_command_input.hasFocus():
                self.ui.send_command_button.click()
        return super().eventFilter(obj, event)

    def set_console_box_text(self, s):
        self.ui.set_console_box_text(s)

    def append_console_box_text(self, s):
        self.ui.append_console_box_text(s)

    def set_players_box_text(self, s):
        self.ui.set_players_box_text(s)

    def append_players_box_text(self, s):
        self.ui.append_players_box_text(s)

    def closeEvent(self, event):
        global infoloader
        if infoloader is not None:
            infoloader.set()
        event.accept()


class ServerFilesWindow(QMainWindow):
    def __init__(self, ui):
        super(ServerFilesWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        global current_path
        current_path = None
        window.show()
        event.accept()


class FileEditWindow(QMainWindow):
    def __init__(self, ui):
        super(FileEditWindow, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        files_window.show()
        event.accept()


class ConsoleSignal(QtCore.QObject):
    replace_sig = QtCore.Signal(str)
    append_sig = QtCore.Signal(str)


class PlayersSignal(QtCore.QObject):
    replace_sig = QtCore.Signal(str)
    append_sig = QtCore.Signal(str)


def start_server():
    window.ui.error_label.setVisible(False)
    try:
        window.ui.start_server_button.setDisabled(True)
        tokenized_get_post_request(False, host, "/server/start/" + sid, {}, token)
    except Exception as e:
        window.ui.error_label.setText(str(e))
        window.ui.error_label.setVisible(True)


def stop_server():
    window.ui.error_label.setVisible(False)
    try:
        window.ui.stop_server_button.setDisabled(True)
        tokenized_get_post_request(False, host, "/server/stop/" + sid, {}, token)
    except Exception as e:
        window.ui.error_label.setText(str(e))
        window.ui.error_label.setVisible(True)


def send_command():
    window.ui.error_label.setVisible(False)
    command = window.ui.send_command_input.text().strip()

    if not command:
        return

    res = None
    try:
        res = tokenized_get_post_request(False, host, "/server/send-command/" + sid, {"command": command}, token)
        window.ui.send_command_input.setText("")
    except Exception as e:
        window.ui.error_label.setText(str(e))
        window.ui.error_label.setVisible(True)

    res = res["command_response"].strip()
    if res:
        window.console_signal.append_sig.emit(res)


def load_mc_server_info(h, s):

    route = "/server/info/" + s

    try:
        data = get_post_request(True, h, route, {})

        if data["success"]:
            window.ui.status_info_label.setText("Running")
            window.ui.status_info_label.setStyleSheet(u"color: rgb(0, 100, 0);\n")

            window.ui.start_server_button.setDisabled(True)
            window.ui.stop_server_button.setDisabled(False)
            window.ui.send_command_button.setDisabled(False)
            window.ui.send_command_input.setDisabled(False)

        else:
            raise Exception("500")

        window.ui.version_info_label.setText(data["version"])
        window.ui.motd_info_label.setText(data["motd"])
        window.ui.player_count_info_label.setText(str(data["online_players"]) + "/" + str(data["max_players"]))

        window.players_signal.replace_sig.emit("")
        for player in sorted(data["players"]):
            window.players_signal.append_sig.emit("- " + player)

    except Exception as e:
        if "500" in str(e):
            window.ui.version_info_label.setText("-")
            window.ui.motd_info_label.setText("-")
            window.ui.player_count_info_label.setText("-")
            window.ui.status_info_label.setText("Offline")
            window.ui.status_info_label.setStyleSheet(u"color: rgb(255, 0, 0);\n")

            window.ui.stop_server_button.setDisabled(True)
            window.ui.start_server_button.setDisabled(False)
            window.ui.send_command_button.setDisabled(True)
            window.ui.send_command_input.setDisabled(True)

            window.players_signal.replace_sig.emit("")

            global first_check
            if first_check:
                window.console_signal.replace_sig.emit("Server offline")
                first_check = False

            return

        print("Error while loading info for the MC server with id \"" + sid + "\"")
        print("\t" + str(e))


def infoloader_f(il):

    if not il.is_set():
        try:
            infoloader_executor.submit(load_mc_server_info, host, sid)
        except Exception as e:
            print(str(e))

        threading.Timer(5, infoloader_f, [il]).start()


async def console_stream_printer():
    uri = host.replace("https://", "wss://").replace("http://", "ws://").rstrip("/")
    uri += "/console-stream"

    async with websockets.connect(uri) as websocket:

        await websocket.send("hello:" + token)
        try:
            message = await websocket.recv()
        except Exception as e:
            window.console_signal.replace_sig.emit("Error reading console stream (" + str(e) + ")")
            return

        msg = "".join(map(str, list(message)))
        if msg != "200":
            window.console_signal.replace_sig.emit("Error reading console stream")
            return

        time.sleep(1)

        await websocket.send("read:" + sid)
        try:
            message = await websocket.recv()
        except Exception as e:
            window.console_signal.replace_sig.emit("Error reading console stream (" + str(e) + ")")
            return

        msg = "".join(map(str, list(message)))
        if msg != "200":
            window.console_signal.replace_sig.emit("Error reading console stream")
            return

        window.console_signal.append_sig.emit("Connected to server console stream\n")

        while True:
            try:
                message = await websocket.recv()
            except Exception as e:
                window.console_signal.replace_sig.emit("Error reading console stream (" + str(e) + ")")
                return
            if "RCON" not in message:
                window.console_signal.append_sig.emit(message)


def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(console_stream_printer())


def load_management_ui():
    global window
    window = MainWindow(Ui_MCServerManagementWindow)

    window.ui.error_label.setVisible(False)
    window.ui.server_name_label.setText(name)
    window.setWindowTitle(name + " control panel")

    global infoloader
    if infoloader is None:
        infoloader = threading.Event()
        infoloader_f(infoloader)
    if infoloader.is_set():
        infoloader.clear()
        infoloader_f(infoloader)

    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop,))
    t.start()

    window.ui.start_server_button.clicked.connect(start_server)
    window.ui.stop_server_button.clicked.connect(stop_server)
    window.ui.send_command_button.clicked.connect(send_command)
    window.ui.send_command_button.setDefault(True)
    window.ui.send_command_button.autoDefault()

    window.ui.server_files_button.clicked.connect(load_server_files_ui)

    window.show()


def load_server_files_ui(first=True, path=""):
    window.ui.error_label.setVisible(False)

    global current_path
    if current_path is None:
        current_path = ""

    current_path = current_path.strip()
    path = path.strip()

    if current_path != "":
        if current_path.startswith("/"):
            current_path = current_path[1:]
        if not current_path.endswith("/"):
            current_path += "/"

    if path != "":
        if path.startswith("/"):
            path = path[1:]
        if not path.endswith("/"):
            path += "/"

    if path == "./":
        path = ""
    if path == "../":
        if current_path == "":
            return
        path = ""
        if "/" in current_path.rstrip("/"):
            current_path = current_path.rstrip("/").split("/", 1)[0]
        else:
            current_path = ""

    global files_window

    if first or (current_path + path) == "":
        try:
            res = tokenized_get_post_request(True, host, "/server/files/" + sid, {}, token)
        except Exception as e:
            window.ui.error_label.setText(str(e))
            window.ui.error_label.setVisible(True)
            return
    else:
        try:
            encoded_path = str(base64.b64encode((current_path + path).encode("utf-8")), "utf-8")
            res = tokenized_get_post_request(True, host, "/server/files/" + sid + "/" + encoded_path, {}, token)
        except Exception as e:
            files_window.ui.error_label.setText(str(e))
            files_window.ui.error_label.setVisible(True)
            return

    if not res["is_directory"]:
        load_file_edit_ui(current_path, path, res["content"])
        return

    current_path = current_path + path

    files_window = ServerFilesWindow(Ui_ServerFilesWindow)

    files_window.ui.error_label.setVisible(False)
    files_window.ui.title_label.setText(name + "'s files")
    files_window.setWindowTitle("Browsing " + name + "'s files")

    if current_path == "":
        files_window.ui.current_path_label.setText("/")
        files_window.ui.back_button.setEnabled(False)
    else:
        files_window.ui.current_path_label.setText("/" + current_path.strip("/") + "/")
        files_window.ui.back_button.clicked.connect(
            lambda: load_server_files_ui(False, "../..")
        )

    files_window.ui.add_file(".", load_server_files_ui)
    files_window.ui.add_file("..", load_server_files_ui)

    for f in sorted(res["content"]):
        files_window.ui.add_file(f, load_server_files_ui)

    files_window.ui.reload_files()

    window.hide()
    files_window.show()


def load_file_edit_ui(path, filename, content):
    global edit_window
    edit_window = FileEditWindow(Ui_FileEditWindow)

    filename = filename.rstrip("/")

    edit_window.ui.path = path
    edit_window.ui.filename = filename

    edit_window.ui.error_label.setVisible(False)
    edit_window.ui.title_label.setText(filename)
    edit_window.setWindowTitle("Editing file " + filename)

    edit_window.ui.current_path_label.setText("/" + path + filename)
    edit_window.ui.back_button.clicked.connect(edit_window.close)

    edit_window.ui.textEdit.setText(content)

    edit_window.ui.textEdit.textChanged.connect(edit_window.ui.on_text_changed)

    edit_window.ui.pushButton.clicked.connect(save_edited_file)

    files_window.hide()
    edit_window.show()


def save_edited_file():
    global edit_window
    if not edit_window.isVisible():
        return

    edit_window.ui.pushButton.setEnabled(False)

    data = {
        "file-contents": edit_window.ui.textEdit.toPlainText()
    }

    path = edit_window.ui.path.strip()
    filename = edit_window.ui.filename.strip()

    if path != "":
        if path.startswith("/"):
            path = path[1:]
        if not path.endswith("/"):
            path += "/"

    if filename != "":
        if filename.startswith("/"):
            filename = filename[1:]
        if filename.endswith("/"):
            filename += "/"

    try:
        encoded_path = str(base64.b64encode((path + filename).encode("utf-8")), "utf-8")
        tokenized_get_post_request(False, host, "/server/files/edit/" + sid + "/" + encoded_path, data, token)
    except Exception as e:
        edit_window.ui.error_label.setText(str(e))
        edit_window.ui.error_label.setVisible(True)
        return

    edit_window.ui.on_file_saved()


if __name__ == "__main__":
    window: Optional[MainWindow] = None
    files_window: Optional[ServerFilesWindow] = None
    edit_window: Optional[FileEditWindow] = None

    infoloader: Optional[threading.Event] = None
    infoloader_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    host: Optional[str] = sys.argv[1]
    sid: Optional[str] = sys.argv[2]
    token: Optional[str] = sys.argv[3]
    name: Optional[str] = sys.argv[4]

    current_path: Optional[str] = None

    first_check = True

    app = QApplication(sys.argv)

    load_management_ui()

    sys.exit(app.exec())
