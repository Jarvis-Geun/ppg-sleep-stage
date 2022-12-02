# First let's import
import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np

# ppg, timer = hp.load_exampledata(2)
ppg = np.loadtxt("ppg/sean_ppg_split.txt")
timer = np.loadtxt("ppg/sean_time_split.txt", dtype=np.str_)

# shape (-1, 2) ==> shape (-1, )
list_timer = []
for i in range(timer.shape[0]):
    added = timer[i, 0] + ' ' + timer[i, 1]
    list_timer.append(added)
timer = np.array(list_timer)

sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')

# normalize ppg
# ppg = ppg / np.std(ppg)

# scaling ppg
# ppg = hp.scale_sections(ppg, sample_rate=sample_rate, windowsize=2.5, lower=0, upper=800)
# ppg = hp.scale_data(ppg, lower=100, upper=300)
# ppg = hp.enhance_peaks(ppg, iterations=2)

print("sample_rate :", sample_rate)
print("ppg.shape :", ppg.shape)

# and visualise
plt.figure(figsize=(100, 4))
plt.plot(ppg)
plt.show()

# run the analysis
wd, m = hp.process(ppg, sample_rate=sample_rate)

# set large figure
# plt.figure(figsize=(100,4))

#call plotter
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

#plt.figure(figsize=(100, 4))
plt.plot(ppg)
plt.show()
