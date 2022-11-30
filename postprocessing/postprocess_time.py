ppg_time = open("/Users/geun/github/ppg-sleep-stage/ppg/geun_time.txt", "w")

with open('/Users/geun/github/ppg-sleep-stage/ppg/geun.txt') as f:
    while True:
        line = f.readline()[:26].rstrip()
        if not line: break
        ppg_time.write(line + "\n")

ppg_time.close()
