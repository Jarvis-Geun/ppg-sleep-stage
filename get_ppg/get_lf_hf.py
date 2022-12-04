import biosppy
import pyhrv.tools as tools
import pyhrv.time_domain as td
from scipy.signal import argrelextrema
import pyhrv.frequency_domain as fd
import numpy as np
import sys


def hrv_analysis(ppg):
    # np.set_printoptions(threshold=sys.maxsize)    # print all numpy
    '''
    Reference : https://github.com/PIA-Group/BioSPPy/blob/master/biosppy/signals/ppg.py
    output
    args = (ts, filtered, onsets, ts_hr, hr)
    names = ('ts', 'filtered', 'onsets', 'heart_rate_ts', 'heart_rate')
    '''
    # [1:3] ==> filtered, onsets, heart_rate_ts
    PPG_signal, _ = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=True)[1:3]
    # [4] ==> heart rate
    heart_rate = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=False)[4]
    print("heart_rate.mean() :", heart_rate.mean())
    print("heart_rate :", heart_rate)
    print("heart_rate.shape :", heart_rate.shape)

    # PPG_peaks = argrelextrema(PPG_signal, np.greater, order=28)
    # PPG_peaks_sq = np.squeeze(PPG_peaks)
    # PPG_rri = tools.nn_intervals(PPG_peaks_sq)
    # real_time = PPG_peaks_sq * 0.009433962
    # PPG_nni = tools.nn_intervals(real_time)

    # rri_mean = np.mean(PPG_rri)
    # nni_mean = np.mean(PPG_nni)

    # print("rri_mean :", rri_mean)
    # print("nni_mean :", nni_mean)

    # print("PPG_rri :", PPG_rri)
    # print("PPG_nni :", PPG_nni)

    # ar method
    # PPG_ratio = fd.welch_psd(PPG_nni, show=True)
    # LF, HF = PPG_ratio['fft_norm']

    # # hr
    # HR = td.hr_parameters(PPG_nni)
    # HR = tools.heart_rate(PPG_nni)

    # # SDNN
    # sdnn = td.sdnn(PPG_nni)

    # return np.array([HR['hr_mean'], HR['hr_std'], sdnn['sdnn'], LF, HF, PPG_ratio['fft_ratio']])
    return heart_rate


if __name__=="__main__":
    # ppg = np.loadtxt("40min_data/jiu/jiu_ppg_split.txt")
    ppg = np.loadtxt("40min_data/hju/hju_ppg_split.txt")
    result = hrv_analysis(ppg)
    print(result)