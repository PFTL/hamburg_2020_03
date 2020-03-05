import threading
from time import sleep

from model.experiment import Experiment


experiment = Experiment()
experiment.load_config('experiment.yml')
experiment.initialize()
t = threading.Thread(target=experiment.start_scan)
t.start()
while t.is_alive():
    print(experiment.i)
    sleep(1)
    experiment.keep_running = False


experiment.save_data()