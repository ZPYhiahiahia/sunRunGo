import datetime
import time

def wait_for_0600():
    now_time = datetime.datetime.now()

    day = now_time.day + 1
    hour = 6
    while(now_time.day != day and now_time.hour != 6):
            time.sleep(360)
            now_time = datetime.datetime.now()
            print("等待开始...")

