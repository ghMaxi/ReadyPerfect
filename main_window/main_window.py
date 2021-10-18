import sys
import files
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, ui_path):
        app = QApplication(sys.argv)
        QMainWindow.__init__(self)
        uic.loadUi(ui_path, self)
        self.show()  # Show the GUI
        sys.exit(app.exec())


if __name__ == '__main__':
    MainWindow(f'{files.designs}main_window.ui')
