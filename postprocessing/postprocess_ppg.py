ppg = open("/Users/geun/github/ppg-sleep-stage/data/ppg.txt", "w")
with open("/Users/geun/github/ppg-sleep-stage/data/data.txt") as f:
    while True:
        line = f.readline()[-8:].rstrip()
        if not line: break
        ppg.write(line + "\n")

ppg.close()
