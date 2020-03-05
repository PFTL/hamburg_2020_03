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