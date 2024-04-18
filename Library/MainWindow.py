from PyQt5.uic import loadUi
from Library.comset import read_settings, write_settings
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QCheckBox
from Library.timer import timer
from Library.SignalEmitter import redrawSignal
from Library.windowSizes import set_label_size, resize_window

class WidgetMain(QMainWindow):
    def __init__(self, path):

        self.settings = read_settings('display_settings')
        super(WidgetMain, self).__init__()
        loadUi(path, self)
        height = self.settings['windowheight']
        width = self.settings['windowwidth']
        self.resize(width, height)
        set_label_size(self, 'Mainwindow')

    # fontsize = read_settings('display_settings')['fontsize']


    def closeEvent(self, event):
        w = self.width()
        h = self.height()
        self.settings = read_settings('display_settings')
        self.settings['windowheight'] = h
        self.settings['windowwidth'] = w
        write_settings(self.settings, 'display_settings')
        super().closeEvent(event)


