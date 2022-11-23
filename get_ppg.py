import serial
import time
import datetime


def ppg(py_serial, path, name, len_time, start_time):
    f = open("{}/{}.txt".format(path, name), "w")

    i = 0
    while True:
        print("elapsed time :", time.time() - start_time)
        if time.time() - start_time > len_time:
            f.close()
            break
        if py_serial.readable():
            ppg = py_serial.readline()
            ppg = str(ppg).lstrip("b'")
            ppg = ppg[:7]
            ppg = ppg + '\n'
            curr_time = datetime.datetime.now()
            curr_time = curr_time.strftime("%Y-%m-%d %H:%M:%S.%f")
            f.write(curr_time + ', ' + ppg)
        i += 1

if __name__=="__main__":
    py_serial = serial.Serial(
        port='/dev/cu.usbserial-130',
        # Baud rate (speed of communication)
        baudrate=9600,
    )
    path = "/Users/geun/github/ppg-sleep-stage/data/"
    name = "data"
    len_time = 120
    start_time = time.time()

    ppg(py_serial, path, name, len_time, start_time)
