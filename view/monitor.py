from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QPushButton, QWidget
from pyqtgraph import PlotWidget


class MonitorWindow(QMainWindow):
    def __init__(self, experiment=None):
        super().__init__()
        self.experiment = experiment

        self.layout = QHBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.plot_widget = PlotWidget()
        self.layout.addWidget(self.plot_widget)
        self.setCentralWidget(self.central_widget)

        self.plot = self.plot_widget.plot([0], [0])

        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.experiment.start_monitor)
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.experiment.stop_monitor)

        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(30)

    def update_plot(self):
        self.plot.setData(self.experiment.monitor_data)


if __name__ == "__main__":
    app = QApplication([])
    mon_windw = MonitorWindow()
    mon_windw.show()
    app.exec()