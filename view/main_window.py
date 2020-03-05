import os
import threading
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, experiment=None):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(base_dir, 'main_window.ui')
        uic.loadUi(ui_file, self)

        self.experiment = experiment

        self.start_button.clicked.connect(self.start_pressed)

    def start_pressed(self):
        print('Button pressed')
        t = threading.Thread(target=self.experiment.start_scan)
        t.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

