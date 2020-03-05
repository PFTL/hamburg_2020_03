import numpy as np
import os
import yaml

from model.analog_daq import AnalogDaq

from model import ur

class Experiment:
    def initialize(self):
        self.daq = AnalogDaq(self.config['daq']['port'])
        self.daq.initialize()

    def load_config(self, filename):
        with open(filename, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

    def start_scan(self):
        start = ur(self.config['scan']['start']).m_as('V')
        stop = ur(self.config['scan']['stop']).m_as('V')
        num_steps = int(self.config['scan']['num_steps'])
        scan_range = np.linspace(start, stop, num_steps) * ur('V')
        self.scan_data = np.zeros(num_steps)
        self.i = 0
        self.keep_running = True
        for volt in scan_range:
            self.daq.set_voltage(self.config['scan']['channel_out'], volt)
            measured_voltage = self.daq.get_voltage(self.config['scan']['channel_in'])
            self.scan_data[self.i] = measured_voltage.m_as('V')
            self.i += 1
            if not self.keep_running:
                break

    def stop_scan(self):
        pass

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
        pass


if __name__ == "__main__":
    experiment = Experiment()
    config_file = '../examples/experiment.yml'
    experiment.load_config(config_file)
    print(experiment.config)
    experiment.initialize()
    experiment.start_scan()