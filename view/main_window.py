import os
import threading
import pyqtgraph as pg

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, experiment=None):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(base_dir, 'main_window.ui')
        uic.loadUi(ui_file, self)

        self.experiment = experiment

        self.plot_widget = pg.PlotWidget()
        self.plot = self.plot_widget.plot([0], [0])
        layout = self.centralwidget.layout()
        layout.addWidget(self.plot_widget)

        self.start_button.clicked.connect(self.experiment.start_scan)
        self.stop_button.clicked.connect(self.experiment.stop_scan)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(30)

    def update_plot(self):
        self.plot.setData(self.experiment.scan_range, self.experiment.scan_data)




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

