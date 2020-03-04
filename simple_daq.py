import serial
import time


class Device:
    def __init__(self, port, line_termination='\n', encoding='ascii'):
        self.rsc = serial.Serial(port)
        self.line_termination = line_termination
        self.encoding = encoding
        time.sleep(1)

    def query(self, message):
        message = message + self.line_termination
        self.rsc.write(message.encode(self.encoding))
        ans = self.rsc.readline()
        ans = ans.decode(self.encoding).strip()
        return ans

    def idn(self):
        return self.query('IDN')

    def set_output(self, channel, output_value):
        message = 'OUT:CH{}:{}'.format(channel, output_value)
        self.query(message)

    def read_input(self, channel):
        message = 'IN:CH{}'.format(channel)
        ans = self.query(message)
        ans = int(ans)
        return ans


if __name__ == '__main__':
    dev = Device('/dev/ttyACM0')
    print(dev.idn())

    voltages = [i for i in range(3300) if i%100 == 0]
    currents = []

    for v in voltages:
        v_bits = int(v/3300*4095)
        dev.set_output(0, v_bits)
        ans = dev.read_input(0)
        ans = ans*3.3/1023
        print(ans/220)
        currents.append(ans/220)
