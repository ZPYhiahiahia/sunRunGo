########################################################################################################################
#   打开 fly-gps
#   favorite -> run ->  move to location
#   退出到桌面
#   打开微信
#   登录微信 : 我 > 设置 -> 下滑 -> 退出 -> 退出登录 -> 退出确认 -> 更多 -> 登录其他账号 -> 输入手机号 -> 下一步 -> 登录
#   打开阳光体育
#   设置 -> 注销登录 -> 确认注销 -> 微信登录 -> 等待
#   等待 -> 开始跑步 -> 等待 -> play
#   跑完并返回步骤1
#
########################################################################################################################
import wellDone as run
import os
import time
import cv2
import numpy as np
import wechat as w
import threading
import datetime
check = True
e = threading.Event()
def calculate(args):
    num = 0
    while (True):
        num += 1
        if (num >= 600):
            break
        time.sleep(1)
        print(num)
def run_thread(args):
    w.open_wechat()
    w.wechat_all(args[0],args[1])
    os.system('adb shell input keyevent 3')  # 返回主屏幕
    time.sleep(1)
    open_sunrun()
    check = run.do_one_run()
class MyThread(threading.Thread):
    def __init__(self,target,args):
        super(MyThread,self).__init__()
        self.target = target
        self.args = args
    def run(self):
        self.target(self.args)
def sun_run_go():
    run.adb_connect()
    open_flygps()
    for key, value in w.data.items():
        thread = MyThread(target=calculate, args=[])
        thread2 = MyThread(target=run_thread,args = [key,value])
        thread.start()
        thread2.start()
        while(thread.is_alive() == True and thread2.is_alive() == True):
            time.sleep(1)
# def get_user():
#     account = open("account.txt",'r')
#     password = open("password.txt",'r')
#     accountlines = account.readlines()
#     passwordlines = password.readlines()
#     userInfo = (accountlines , passwordlines)
#     # print(userInfo)
#     return userInfo

def get_cmd_string(x,y,z=0):
    cmd = 'adb shell input swipe '+ str(x) + ' ' +str(y) + ' '+ str(x) + ' ' + str(y) + ' ' + str(z)
    print(cmd)
    return cmd


def open_flygps():
    # os.system('adb ')
    os.system('adb shell am start -n com.fly.gps/com.fly.gps.MainActivity')
    time.sleep(8)
    os.system(get_cmd_string(774,300))#揭开纱幕
    time.sleep(1)
    os.system(get_cmd_string(774,300))#Favorites
    os.system(get_cmd_string(510,549))#1
    os.system(get_cmd_string(123,1086))#Run
    os.system(get_cmd_string(453,1056))#Move
    #os.system(get_cmd_string(384,1653))
    #os.system(get_cmd_string(92,796,1004,179))
    os.system("adb shell input swipe 92 796 1004 179")
    time.sleep(1)
def open_sunrun():
    # time.sleep(2)                            # 等待两秒
    # os.system('adb shell input keyevent 3')  # 回到桌面
    # time.sleep(0.5)
    # os.system('adb shell input keyevent 3')  # 回到桌面
    # os.system(get_cmd_string(158,365))       # 打开 sunrun
    # time.sleep(10)                           # 等待广告
    #

    os.system("adb shell am start -n com.aipao.hanmoveschool/com.aipao.hanmoveschool.activity.LoginActivity")
    # 点X号加确认
    #time.sleep(3)
   # os.system(get_cmd_string(891, 93))  # 关闭广告
    time.sleep(7)
    os.system(get_cmd_string(996, 1020))  # 点X
    time.sleep(1)
    os.system(get_cmd_string(768, 1107))  # 点击确认
    time.sleep(1)
    os.system(get_cmd_string(156, 1638))  # 结束跑步的小箭头
    time.sleep(1)
    os.system(get_cmd_string(900, 1677))  # 注销菜单
    os.system(get_cmd_string(540, 1400))  # 点击注销
    os.system(get_cmd_string(762, 1107))  # 点击确认
    # 登录过程 (因为软件有bug所以要回到桌面后重试)
    os.system(get_cmd_string(537, 1581))  # 微信登录
    time.sleep(7)  # 等待
    #os.system(get_cmd_string(516, 1206)) #不清楚用法
    os.system('adb shell input keyevent 3')  # home
    time.sleep(1)
    os.system("adb shell am start -n com.aipao.hanmoveschool/com.aipao.hanmoveschool.activity.LoginActivity")
    # os.system(get_cmd_string(744, 2720))  # 微信登录
    #os.system(get_cmd_string(891, 93))  # 关闭广告
    time.sleep(7)
    os.system(get_cmd_string(528, 1704))  # 开始跑步界面
    os.system(get_cmd_string(552, 1458))  # 开始跑步
    # os.system(get_cmd_string(732, 2546))
    run.wait_for_run_ready()  # 等待play亮起来
    time.sleep(1)
    os.system(get_cmd_string(555, 1512))  # 点击play
    time.sleep(1)

def kill_all_server():
    os.system('adb shell input keyevent 3')
    # os.system(get_cmd_string(786,1851))
    # os.system(get_cmd_string(540,1587))

# # userInfo = get_string()
# kill_all_server()
# open_flygps()
# open_sunrun()

sun_run_go()