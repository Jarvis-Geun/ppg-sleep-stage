import biosppy
import pyhrv.tools as tools
import pyhrv.time_domain as td
from scipy.signal import argrelextrema
import pyhrv.frequency_domain as fd
import numpy as np
import argparse


def get_args_parser():
    parser = argparse.ArgumentParser('Set PPG analyzer', add_help=False)
    parser.add_argument('--bpm', default=None, type=int, help="Ground Truth BPM")

    return parser


def hrv_analysis(ppg, original_hr):
    # ppg = ppg[:6360]
    PPG_signal, _ = biosppy.signals.ppg.ppg(ppg, sampling_rate=106.8, show=False)[1:3]

    # np.greater 인자 ==> 극대값 찾기
    # np.less 인자 ==> 극소값 찾기
    # order ==> How many points on each side to use for the
    # comparison to consider comparator(n, n+x) to be True

    for order in range(1, 1000):
        PPG_peaks = argrelextrema(PPG_signal, np.greater, order=order)
        PPG_peaks_sq = np.squeeze(PPG_peaks)
        # real_time = PPG_peaks_sq * 0.009363295
        real_time = PPG_peaks_sq * 0.0093
        PPG_nni = tools.nn_intervals(real_time)
        # hr = tools.heart_rate(PPG_nni)
        HR = td.hr_parameters(PPG_nni)

        print(order)
        # if (hr.mean() >= original_hr - 1) and (hr.mean() <= original_hr + 1):
        if (HR['hr_mean'] >= original_hr - 1) and (HR['hr_mean'] <= original_hr + 1):
            print("order :", order)
            # print("heart rate :", hr.mean())
            print("heart rate :", HR['hr_mean'])
            break

    # ar method
    PPG_ratio = fd.welch_psd(PPG_nni, show=False)
    LF, HF = PPG_ratio['fft_norm']
    # hr
    # HR = td.hr_parameters(PPG_nni)
    # SDNN
    sdnn = td.sdnn(PPG_nni)

    # return np.array([HR['hr_mean'], HR['hr_std'], LF, HF, PPG_ratio['fft_ratio'], rri_mean, nni_mean])
    # return hr


if __name__=="__main__":
    parser = argparse.ArgumentParser('find order for heart rate', parents=[get_args_parser()])
    args = parser.parse_args()

    original_hr = args.bpm
    ppg = np.loadtxt("../5min_data/sbin/sbin_ppg.txt")
    bpm = hrv_analysis(ppg, original_hr)