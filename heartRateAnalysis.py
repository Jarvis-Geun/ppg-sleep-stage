#First let's import
import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np

ppg, timer = hp.load_exampledata(2)
#ppg = np.loadtxt("/Users/geun/github/ppg-sleep-stage/data/ppg.txt")
#timer = np.loadtxt("/Users/geun/github/ppg-sleep-stage/data/time.txt", dtype=str)

# scaling ppg
#ppg = hp.scale_sections(ppg, sample_rate=100, windowsize=2.5, lower=0, upper=800)
ppg = hp.scale_data(ppg, lower=0, upper=600)
ppg = hp.enhance_peaks(ppg, iterations=2)

print("type(timer) :", type(timer[-1]))
print("timer[-1] :", timer[-1])
sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')
print("sample_rate :", sample_rate)

#and visualise
plt.figure(figsize=(100, 4))
plt.plot(ppg)
plt.show()

#run the analysis
wd, m = hp.process(ppg, sample_rate = 100)

#set large figure
#plt.figure(figsize=(100,4))

#call plotter
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

plt.figure(figsize=(100, 4))
plt.plot(ppg)
plt.show()
