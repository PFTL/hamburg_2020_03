import serial
import time
import threading


dev = serial.Serial('/dev/ttyACM0')
time.sleep(1)

def get_idn():
    time.sleep(.2)
    dev.write(b'IDN\n')
    print(dev.readline())

t1 = threading.Thread(target=get_idn)
t2 = threading.Thread(target=get_idn)

t1.start()
t2.start()

t1.join()
t2.join()