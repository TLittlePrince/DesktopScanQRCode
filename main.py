import sys
import webbrowser

import pyperclip
from PIL import ImageGrab, BmpImagePlugin
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from pyzbar import pyzbar

import jumpWindow


def scan_qr_code(image):
    data = pyzbar.decode(image)
    return data[0].data.decode('utf-8')


def get_clipboard_image():
    try:
        img = ImageGrab.grabclipboard()
    except OSError:
        img = None
    return img


class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = jumpWindow.Ui_Form()
        self.ui.setupUi(self)
        self.url = ''
        self.img = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.main_loop)
        self.timer.setInterval(2000)
        self.timer.start()
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.move_window_to_right_down)
        self.timer2.start(300)

    def move_window_to_right_down(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(screen.width() - size.width(), screen.height() - size.height() - 70)

    @pyqtSlot()
    def on_copy_button_clicked(self):
        pyperclip.copy(self.url)

    @pyqtSlot()
    def on_jump_button_clicked(self):
        webbrowser.open(self.url, new=2)

    @pyqtSlot()
    def on_close_button_clicked(self):
        self.resize(565, 118)
        self.setHidden(True)
        # self.close()
        # sys.exit(app.exec_())

    def main_loop(self):
        img = get_clipboard_image()
        if img is None or type(img) == BmpImagePlugin.DibImageFile:
            print('\rno image', end='')
        elif not img == self.img:
            self.img = img
            url = scan_qr_code(img)
            if url:
                self.resize(565, 118)
                self.url = url
                print(f'\n{self.url}')
                self.ui.content_label.setText(self.url)
                self.move_window_to_right_down()
                self.show()
                # timer = QTimer(self)
                # timer.timeout.connect(self.on_close_button_clicked)
                # timer.start(5000)
            else:
                print('\rno data', end='')
        else:
            print('\rno new image', end='')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Widget()
    win.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    # win.show()
    sys.exit(app.exec_())
