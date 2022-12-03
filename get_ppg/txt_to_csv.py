import biosppy
import pyhrv.tools as tools
import pyhrv.time_domain as td
from scipy.signal import argrelextrema
import pyhrv.frequency_domain as fd
import numpy as np
import sys
import pandas as pd


def hrv_analysis(ppg):
    # np.set_printoptions(threshold=sys.maxsize)    # print all numpy
    '''
    Reference : https://github.com/PIA-Group/BioSPPy/blob/master/biosppy/signals/ppg.py
    output
    args = (ts, filtered, onsets, ts_hr, hr)
    names = ('ts', 'filtered', 'onsets', 'heart_rate_ts', 'heart_rate')
    '''
    # [1:3] ==> filtered, onsets, heart_rate_ts
    PPG_signal, _ = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=False)[1:3]
    # [4] ==> heart rate
    heart_rate_ts = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=False)[3]
    heart_rate = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=False)[4]
    print("heart_rate.mean() :", heart_rate.mean())
    print("heart_rate :", heart_rate)
    print("heart_rate.shape :", heart_rate.shape)
    
    for order in range(1, 300):
        print("order :", order)
        PPG_peaks = argrelextrema(PPG_signal, np.greater, order=order)
        PPG_peaks_sq = np.squeeze(PPG_peaks)
        real_time = PPG_peaks_sq * 0.009433962
        PPG_nni = tools.nn_intervals(real_time)

        print("PPG_nni.shape :", PPG_nni.shape)
        print("heart_rate.shape :", heart_rate.shape)
        if PPG_nni.shape[0] <= heart_rate.shape[0]:
            print(order)
            break


    f = open("40min_data/geun/geun_HR.txt", "w")
    for i in range(heart_rate.shape[0]):
        f.write(str(heart_rate[i]) + '\n')

    return heart_rate, PPG_nni, heart_rate_ts


if __name__=="__main__":
    # ppg = np.loadtxt("40min_data/geun/geun_ppg_split.txt")
    ppg = np.loadtxt("40min_data/geun/geun_ppg_split.txt")
    heart_rate, nni, heart_rate_ts = hrv_analysis(ppg)
    print(heart_rate)

    # file = pd.read_csv('40min_data/geun/geun_HR.txt')
    # new_csv_file = file.to_csv("40min_data/geun/geun_HR.csv")
    df = pd.DataFrame(heart_rate_ts, columns = ['HR_time'])
    df['RR-interval'] = pd.Series(nni)
    df['heart_rate'] = heart_rate
    # df = df.fillna('N/A')
    df.to_csv("40min_data/geun/geun_HR.csv", index = False)