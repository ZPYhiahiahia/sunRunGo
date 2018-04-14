import datetime
import time

def wait_for_0600():
    now_time = datetime.datetime.now()

    day = now_time.day + 1
    hour = 6
    while(now_time.day != day or now_time.hour != 6):
        print("等待开始...")
        time.sleep(2)
        now_time = datetime.datetime.now()


