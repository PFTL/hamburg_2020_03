import threading
import time

import numpy as np
import os
import yaml

from model.analog_daq import AnalogDaq

from model import ur


class Experiment:
    def __init__(self):
        self.scan_range = np.zeros(1)
        self.scan_data = np.zeros(1)
        self.config = {}
        self.is_running = False

    def initialize(self):
        self.daq = AnalogDaq(self.config['daq']['port'])
        self.daq.initialize()

    def load_config(self, filename):
        with open(filename, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

    def do_scan(self):
        start = ur(self.config['scan']['start']).m_as('V')
        stop = ur(self.config['scan']['stop']).m_as('V')
        num_steps = int(self.config['scan']['num_steps'])
        self.scan_range = np.linspace(start, stop, num_steps) * ur('V')
        self.scan_data = np.zeros(num_steps)
        self.i = 0
        self.keep_running = True
        self.is_running = True
        for volt in self.scan_range:
            volt = volt
            self.daq.set_voltage(self.config['scan']['channel_out'], volt)
            measured_voltage = self.daq.get_voltage(self.config['scan']['channel_in'])
            self.scan_data[self.i] = measured_voltage.m_as('V')
            self.i += 1
            if not self.keep_running:
                break
        self.is_running = False

    def start_scan(self):
        t = threading.Thread(target=self.do_scan)
        t.start()

    def stop_scan(self):
        self.keep_running = False

    def save_data(self):
        if not os.path.isdir(self.config['data']['folder']):
            os.makedirs(self.config['data']['folder'])
        saving_file = os.path.join(self.config['data']['folder'], self.config['data']['filename'])
        print('Saving data to', saving_file)
        np.save(saving_file, self.scan_data)

    def save_metadata(self):
        pass

    def plot_data(self):
        pass

    def finalize(self):
        print('Finalizing Experiment')
        self.keep_running = False
        while self.is_running:
            time.sleep(0.1)
        self.daq.finalize()



if __name__ == "__main__":
    experiment = Experiment()
    config_file = '../examples/experiment.yml'
    experiment.load_config(config_file)
    print(experiment.config)
    experiment.initialize()
    experiment.start_scan()