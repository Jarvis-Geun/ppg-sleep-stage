import biosppy
import pyhrv.tools as tools
import pyhrv.time_domain as td
from scipy.signal import argrelextrema
import pyhrv.frequency_domain as fd
import numpy as np
import sys
import pandas as pd


def analyze_ppg(ppg, minute):
    # np.set_printoptions(threshold=sys.maxsize)    # print all numpy
    '''
    Reference : https://github.com/PIA-Group/BioSPPy/blob/master/biosppy/signals/ppg.py
    output
    args = (ts, filtered, onsets, ts_hr, hr)
    names = ('ts', 'filtered', 'onsets', 'heart_rate_ts', 'heart_rate')
    '''
    sampling_rate = 79.5319
    # [1:3] ==> filtered, onsets, heart_rate_ts
    PPG_signal, _ = biosppy.signals.ppg.ppg(ppg, sampling_rate=sampling_rate, show=False)[1:3]
    # [4] ==> heart rate
    heart_rate_ts = biosppy.signals.ppg.ppg(ppg, sampling_rate=sampling_rate, show=False)[3]
    heart_rate = biosppy.signals.ppg.ppg(ppg, sampling_rate=sampling_rate, show=False)[4]
    
    for order in range(1, 300):
        print("order :", order)
        PPG_peaks = argrelextrema(PPG_signal, np.greater, order=order)
        PPG_peaks_sq = np.squeeze(PPG_peaks)
        # real_time = PPG_peaks_sq * 0.009433962
        real_time = PPG_peaks_sq * 0.012573571107945
        PPG_nni = tools.nn_intervals(real_time)

        if PPG_nni.shape[0] <= heart_rate.shape[0]:
            print(order)
            break

    ########## 변경할 것 !!! ##########
    f = open("../data/1/1_HR_{}.txt".format(minute), "w")
    for i in range(heart_rate.shape[0]):
        f.write(str(heart_rate[i]) + '\n')

    return heart_rate_ts, PPG_nni, heart_rate


if __name__=="__main__":
    ppg = np.loadtxt("../data/jiu123/jiu123_ppg.txt")
    minute = 5

    for minute in range(5, 41):
        heart_rate_ts, nni, heart_rate = analyze_ppg(ppg, minute)
        print("minute : {}, heart rate : {}".format(minute, heart_rate.mean()))

    # Save PPG analysis result to CSV format
    df = pd.DataFrame(heart_rate_ts, columns = ['HR_time'])
    df['RR-interval'] = pd.Series(nni)
    df['heart_rate'] = heart_rate
    df = df.fillna('N/A')
    df.to_csv("../data/jiu123/jiu123.csv", index = False)