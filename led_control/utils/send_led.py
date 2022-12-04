import serial
import time


def send_led(py_serial, LED):
    # wait for opening serial port
    time.sleep(5)

    print("LED :", LED)

    py_serial.write(str(LED).encode())

    return


if __name__=="__main__":
    PORT = "/dev/cu.usbserial-1130"
    baudrate = 9600     # Baud rate (speed of communication)

    # open serial
    py_serial = serial.Serial(
        port=PORT,
        baudrate=baudrate
    )

    # initialize led max light
    LED = "3"

    send_led(py_serial, LED)