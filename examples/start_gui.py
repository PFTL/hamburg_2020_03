import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from PyQt5.QtWidgets import QApplication

from model.experiment import Experiment
from view.main_window import MainWindow


experiment = Experiment()
experiment.load_config('experiment.yml')
experiment.initialize()

app = QApplication([])
window = MainWindow(experiment)
window.show()
app.exec()

experiment.finalize()