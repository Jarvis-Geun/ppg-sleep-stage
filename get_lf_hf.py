import biosppy
import pyhrv.tools as tools
import pyhrv.time_domain as td
from scipy.signal import argrelextrema
import pyhrv.frequency_domain as fd
import numpy as np


def hrv_analysis(ppg):
    print("ppg.shape :", ppg.shape)
    print(ppg)
    PPG_signal, _ = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=True)[1:3]

    PPG_peaks = argrelextrema(PPG_signal, np.greater, order=30)
    PPG_peaks_sq = np.squeeze(PPG_peaks)
    PPG_rri = tools.nn_intervals(PPG_peaks_sq)
    real_time = PPG_peaks_sq * 0.009433962
    PPG_nni = tools.nn_intervals(real_time)

    rri_mean = np.mean(PPG_rri)
    nni_mean = np.mean(PPG_nni)

    print("rri_mean :", rri_mean)
    print("nni_mean :", nni_mean)

    print("PPG_rri :", PPG_rri)
    print("PPG_nni :", PPG_nni)

    # ar method
    PPG_ratio = fd.welch_psd(PPG_nni, show=True)
    LF, HF = PPG_ratio['fft_norm']
    # hr
    HR = td.hr_parameters(PPG_nni)
    # SDNN
    sdnn = td.sdnn(PPG_nni)

    return np.array([HR['hr_mean'], HR['hr_std'], sdnn['sdnn'], LF, HF, PPG_ratio['fft_ratio']])


if __name__=="__main__":
    ppg = np.loadtxt("ppg/geun_ppg.txt")
    result = hrv_analysis(ppg)
    print(result)