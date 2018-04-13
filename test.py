# import json
# with open('test.txt','r') as f:
#     data = json.load(f)
# print(data['1'])
import threading
import time
#
#         print(num)
#     check = False
# # class Thread(threading.Thread):
# #     def __init__(self,action):
# #         self.action = action
# #         threading.Thread.__init__(self)
# #     def run(self):
# #         self.action(self)
# #     def stop(self):
e = threading.Event()
class Thread(threading.Thread):
    def run(self):
        num = 0
        while (True):
            num += 1
            if (num >= 10):
                break
            time.sleep(1)
            print(num)
thread = Thread()
thread.start()
time.sleep(11)
print(thread.is_alive())
