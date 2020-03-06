import os
import threading
import pyqtgraph as pg

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from model import ur


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

        self.start_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.experiment.stop_scan)
        self.save_button.clicked.connect(self.experiment.save)
        self.actionSave.triggered.connect(self.experiment.save)

        self.start_line.setText(self.experiment.config['scan']['start'])
        self.stop_line.setText(self.experiment.config['scan']['stop'])
        self.num_steps_line.setText(str(self.experiment.config['scan']['num_steps']))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.timeout.connect(self.update_gui)
        self.timer.start(30)

    def update_gui(self):
        start = self.start_line.text()
        stop = self.stop_line.text()

        if ur(start) > ur('3.3V') or ur(stop) > ur('3.3V') or self.experiment.is_running:
            self.start_button.setEnabled(False)

        if ur(start) <= ur('3.3V') and ur(stop) <= ur('3.3V') and not self.experiment.is_running:
            self.start_button.setEnabled(True)

    def update_plot(self):
        self.plot.setData(self.experiment.scan_range, self.experiment.scan_data)

    def start_scan(self):
        start = self.start_line.text()
        stop = self.stop_line.text()
        num_steps = int(self.num_steps_line.text())

        self.experiment.config['scan'].update(
            {'start': start,
             'stop': stop,
             'num_steps': num_steps}
        )

    # self.experiment.config['scan']['start'] = start
    # self.experiment.config['scan']['stop'] = stop
    # self.experiment.config['scan']['num_steps'] = num_steps

        self.experiment.start_scan()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

