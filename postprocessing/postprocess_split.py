def postprocess_ppg(raw_path, ppg_path):
    ppg = open(ppg_path, "w")

    with open(raw_path) as f:
        while True:
            line = f.readline()[-8:].rstrip()
            if not line: break
            ppg.write(line + "\n")

    ppg.close()

def postprocess_time(raw_path, time_path):
    ppg_time = open(time_path, "w")

    with open(raw_path) as f:
        while True:
            line = f.readline()[:26].rstrip()
            if not line: break
            ppg_time.write(line + "\n")

    ppg_time.close()


if __name__=="__main__":
    raw_path = "../40min_data/yong/yong_ppg.txt"
    ppg_path = "../40min_data/yong/yong_ppg_split.txt"
    time_path = "../40min_data/yong/yong_time_split.txt"
    postprocess_ppg(raw_path, ppg_path)
    postprocess_time(raw_path, time_path)