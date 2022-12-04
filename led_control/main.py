import serial   # pyserial for UART(Serial) communication
import time     # for computing elapsed time
import datetime # for saving milliseconds
import argparse # get argument info (ex. second, name, path, etc)

from utils.serial_get_ppg import serial_get_ppg     # Get PPG data using pyserial
from utils.send_led import send_led


# get argument using argparse
# argument : second, path_ppg, path_result
def get_args_parser():
    parser = argparse.ArgumentParser('Set PPG analyzer', add_help=False)
    parser.add_argument('--second', default=None, type=int, help="second of run-time")
    parser.add_argument('--path_ppg', default=None, type=str, help="path where to save ppg")
    parser.add_argument('--path_result', default=None, type=str, help="path where to save result")

    return parser


# per minute : RR-interval, NN-interval, LF, HF, LF/HF (ratio)
# per second : heart rate (BPM)

def main(args):
    PORT = "/dev/cu.usbmodem11201"
    baudrate = 9600     # Baud rate (speed of communication)
    # open serial
    py_serial = serial.Serial(
        port=PORT,
        baudrate=baudrate
    )

    # initialize led max light
    LED = 3
    send_led(py_serial, LED)

    start_time = time.time()
    # Save PPG data to text file
    serial_get_ppg(args, py_serial, start_time, LED)

    # TODO
    # Visualize PPG in real time

    return 


if __name__=="__main__":
    parser = argparse.ArgumentParser('Analyze PPG', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)