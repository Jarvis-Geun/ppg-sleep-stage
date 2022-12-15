# First let's import
import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np


ppg = np.loadtxt("data/7/7_ppg.txt")
timer = np.loadtxt("data/7/7_time.txt", dtype=np.str_)

# shape (-1, 2) ==> shape (-1, )
list_timer = []
for i in range(timer.shape[0]):
    added = timer[i, 0] + ' ' + timer[i, 1]
    list_timer.append(added)
timer = np.array(list_timer)

sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')
print("sample_rate :", sample_rate)