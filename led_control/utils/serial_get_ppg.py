import serial   # pyserial for UART(Serial) communication
import time     # for computing elapsed time
import datetime # for saving milliseconds
import numpy as np
import sys

from .analyze_ppg import analyze_ppg
from .send_led import send_led


def serial_get_ppg(args, py_serial, start_time, LED):
    sec_to_min = args.second // 60
    one_minute = [min for min in range(1, sec_to_min+1)]
    before_heart_rate = 0
    before_PPG_nni = 0

    ppg_five_minute = []
    minute = 5

    f = open("{}.txt".format(args.path_ppg), "w")

    while True:
        print("elapsed time : {0:0.4f}".format(time.time() - start_time), end='\r')

        # 설정한 시간(args.second)가 지나면 ppg 저장 종료
        if time.time() - start_time > args.second:
            f.close()
            sys.exit()

        # 시리얼 통신이 가능할 경우, 데이터 불러오기
        if py_serial.readable():
            ppg = py_serial.readline()
            ppg = str(ppg).lstrip("b'")
            # 소수 5번째 자리까지 읽기 (7 ==> 한 자리 정수 + 소수점 + 소수 5번째 자리)
            ppg = ppg[:7]
            # 현재시각(ms 단위) 저장하기 위해 datetime 사용
            curr_time = datetime.datetime.now()
            curr_time = curr_time.strftime("%Y-%m-%d %H:%M:%S.%f")
            # 5초가 지난 후부터 값 저장 (데이터 소실 방지)
            if time.time() - start_time > 5:
                f.write(curr_time + ', ' + ppg + '\n')
                ppg_five_minute.append(float(ppg))

            # 1분마다 5분 동안의 데이터에 대한 PPG 분석
            # 5분이 경과한 후부터 PPG 분석
            if (int(time.time() - start_time) >= 60 * minute) and minute in one_minute:
                print("\n\nminute :", minute, end='\n')
                one_minute.remove(minute)

                #TODO
                # Postprocess(split) ppg and time from the text file

                if minute > 5:
                    # 106 : sample rate
                    # 1분당 106개의 ppg 데이터가 저장되므로 이를 제거하여 5분동안의 데이터만 사용
                    # ppg_five_minute = ppg_five_minute[106*60-1:]
                    ppg_five_minute = ppg_five_minute[79*60-1:]

                heart_rate_ts, PPG_nni, heart_rate = analyze_ppg(np.array(ppg_five_minute), minute)
                result_txt = open("{}.txt".format(args.path_result), "a")

                print("Heart rate elapsed time : {}, RR-interval : {}, Heart rate : {}".format(heart_rate_ts, PPG_nni, heart_rate))

                result_txt.write(str(curr_time) + ' ' + str(minute) + ' ' + str(heart_rate_ts) + ' ' + str(PPG_nni) + ' ' + str(heart_rate) + "\n")

                # 이전 BPM보다 1%씩 감소할 경우, LED 조명 감소
                if (heart_rate <= before_heart_rate * 0.99) or (PPG_nni >= before_PPG_nni * 1.01):
                    print("Change light")
                    LED -= 1
                    if LED <= 0:
                        LED = 0
                    send_led(py_serial, LED)

                before_heart_rate = heart_rate
                before_PPG_nni = PPG_nni

                minute += 1
    return