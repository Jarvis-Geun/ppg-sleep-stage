# ppg = open("/Users/geun/github/ppg-sleep-stage/data/geun_1129_ppg.txt", "w")
ppg = open("/Users/geun/github/ppg-sleep-stage/ppg/geun_ppg.txt", "w")
# with open("/Users/geun/github/ppg-sleep-stage/data/geun_1129.txt") as f:
with open("/Users/geun/github/ppg-sleep-stage/ppg/geun.txt") as f:
    while True:
        line = f.readline()[-8:].rstrip()
        if not line: break
        ppg.write(line + "\n")

ppg.close()
