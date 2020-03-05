from controller.simple_daq import Device

from model import ur

class AnalogDaq:
    def __init__(self, port):
        self.port = port
        self.driver = None

    def initialize(self):
        self.driver = Device(self.port)

    def set_voltage(self, channel, voltage):
        voltage_bits = voltage/ur('3.3V')*4095
        voltage_bits = int(voltage_bits.m_as(''))
        self.driver.set_analog_output(channel, voltage_bits)

    def get_voltage(self, channel):
        voltage_bits = self.driver.get_analog_input(channel)
        voltage = voltage_bits * ur('3.3V')/1023
        return voltage

    def finalize(self):
        self.set_voltage(0, ur('0V'))
        self.driver.close()


if __name__ == "__main__":
    daq = AnalogDaq('/dev/ttyACM0')
    daq.initialize()
    voltage = ur('3.V')
    daq.set_voltage(0, voltage)
    input_volts = daq.get_voltage(0)
    print(input_volts)
    daq.finalize()