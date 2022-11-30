import biosppy
import heartpy as hp
from scipy.signal import argrelextrema
import numpy as np

import pyhrv.tools as tools
import pyhrv.time_domain as td
import pyhrv.frequency_domain as fd


def analyze_ppg(ppg_per_minute):
    # sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')
    sample_rate = 106.8
    
    PPG_signal, _ = biosppy.signals.ppg.ppg(ppg_per_minute, sampling_rate=sample_rate, show=False)[1:3]

    PPG_peaks = argrelextrema(PPG_signal, np.greater, order=30)
    PPG_peaks_sq = np.squeeze(PPG_peaks)
    real_time = PPG_peaks_sq * 0.009433962

    PPG_rri = tools.nn_intervals(PPG_peaks_sq)
    PPG_nni = tools.nn_intervals(real_time)

    rri_mean = np.mean(PPG_rri)
    nni_mean = np.mean(PPG_nni)

    # ar method
    PPG_ratio = fd.welch_psd(PPG_nni, show=False)
    LF, HF = PPG_ratio['fft_norm']
    # hr
    HR = td.hr_parameters(PPG_nni)
    # SDNN
    sdnn = td.sdnn(PPG_nni)

    # return np.array([HR['hr_mean'], HR['hr_std'], sdnn['sdnn'], LF, HF, PPG_ratio['fft_ratio']])
    return list([HR['hr_mean'], LF, HF, PPG_ratio['fft_ratio'], rri_mean, nni_mean])