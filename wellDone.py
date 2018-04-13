import cv2
import numpy as np
import math
import os
import time
import datetime
# 点数跑够但是距离不够的情况
# 终点在画面外 没有红色 没有目标的情况
# 没有线 只有点的时候 跑向(0,0)


#上方距离HSV 355 73 70
#红线    HSV 0 100 100
#蓝线    HSV 240 100 100
#起点蓝色标志 HSV 223 87 97
# 下一个标志的黄色数字 HSV 60 100 100

def run_ready(img):
    top = int(img.shape[0] * 0.70)
    bottom = int(img.shape[0] * 0.85)
    region = img[top:bottom]
    hsv_img = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    color_lower = np.int32([20, 200, 230])
    color_upper = np.int32([50, 232, 260])
    color_mask = cv2.inRange(hsv_img, color_lower, color_upper)  # 得到一个提取出需要的东西的黑白图片
    # cv2.imshow("region" , color_mask)
    contours = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]  # 得到轮廓
    # print(len(contours))
    return len(contours)

def wait_for_run_ready():
    img = getScreenshot()
    while not run_ready(img):
        time.sleep(2)
        img = getScreenshot()


def find_self(img): #画出()并返回当前位置坐标
    top = int(img.shape[0] * 0.3)
    bottom = int(img.shape[0] * 0.7)
    region = img[top:bottom]
    # cv2.imshow("region",region)
    hsv_img = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv_img",hsv_img);
    color_lower = np.int32([100, 229, 229])
    color_upper = np.int32([120, 347, 255])
    color_mask = cv2.inRange(hsv_img, color_lower, color_upper)  # 得到一个提取出需要的东西的黑白图片
    contours = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]  # 得到轮廓
    # cv2.imshow("contours",contours)
    # cv2.imshow("color_mask",color_mask)
    center_coord = (0,0)
    if len(contours) > 0:  # 轮廓数大于0
        max_contour = max(contours, key=cv2.contourArea)
        max_contour = cv2.convexHull(max_contour)
        rect = cv2.boundingRect(max_contour)
        x, y, w, h = rect
        center_coord = (x + int(w / 2), y + h + top - 20)
        cv2.circle(img, center_coord, 5, (0, 255, 0), -1)
        # cv2.imshow("color_mask",img)
    if center_coord == (0,0):
        print("cant find myself")
        return False
    return center_coord #返回当前位置坐标
    # cv2.imshow("img",img)

def fine_line(img):
    top = int(img.shape[0] * 0.2)
    bottom = int(img.shape[0] * 0.8)
    region = img[top:bottom]
    # cv2.imshow("region",region)
    hsv_img = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv_img",hsv_img)
    # 色彩阈值
    color_lower = np.int32([0, 224, 224])
    color_upper = np.int32([5, 255, 255])
    color_mask = cv2.inRange(hsv_img, color_lower, color_upper)  # 得到一个提取出需要的东西的黑白图片
    # 描点:
    # cv2.imshow("color_mask",color_mask)
    contours = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]  # 得到轮廓

    min = 99999999
    max = -1
    low_x = low_y = high_y = high_x = 0
    if(len(contours) > 0):
        for contour in contours:
            sorted_top = sorted(contour, key=lambda contour: contour[0][1])
            # print(sorted_top)
            # sorted_top.reverse()
            # print(sorted_top)
            # print((sorted_top[0][0][0] ,sorted_top[0][0][1]+top))
            # i = i+1
            # cv2.circle(img, (sorted_top[0][0][0], sorted_top[0][0][1] + top), i, (0, 255, 0), -1)
            if sorted_top[0][0][1] < min:
                min - sorted_top[0][0][1]
                high_x = sorted_top[0][0][0]
                high_y = sorted_top[0][0][1]
            sorted_top.reverse()
            if sorted_top[0][0][1] > max:
                max = sorted_top[0][0][1]
                low_x = sorted_top[0][0][0]
                low_y = sorted_top[0][0][1]
    else:
        color_lower = np.int32([120, 234, 234])
        color_upper = np.int32([122, 255, 255])
        color_mask = cv2.inRange(hsv_img, color_lower, color_upper)  # 得到一个提取出需要的东西的黑白图片
        contours = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]  # 得到轮廓
        for contour in contours:
            sorted_top = sorted(contour, key=lambda contour: contour[0][1])
            # print(sorted_top)
            # sorted_top.reverse()
            # print(sorted_top)
            # print((sorted_top[0][0][0] ,sorted_top[0][0][1]+top))
            # i = i+1
            # cv2.circle(img, (sorted_top[0][0][0], sorted_top[0][0][1] + top), i, (0, 255, 0), -1)
            if sorted_top[0][0][1] < min:
                min - sorted_top[0][0][1]
                high_x = sorted_top[0][0][0]
                high_y = sorted_top[0][0][1]
            sorted_top.reverse()
            if sorted_top[0][0][1] > max:
                max = sorted_top[0][0][1]
                low_x = sorted_top[0][0][0]
                low_y = sorted_top[0][0][1]
    # print((high_x,high_y+top),(low_x,low_y+top))

    # cv2.circle(img,(int(high_x),int(high_y)+top), 5, (0, 255, 0), -1)
    # cv2.circle(img,(int(low_x),int(low_y)+top), 5, (0, 255, 0), -1)
    now = find_self(img)
    if(now == False):
        print("cant find line")
        return False
    if (now[0] - low_x) * (now[0] - low_x) + (now[1] - low_y - top) * (now[1] - low_y - top) > (now[0] - high_x) * (now[0] - high_x) + (now[1] - high_y - top) * (now[1] - high_y - top):
        dire = (low_x,low_y+top)
    else:
        dire = (high_x,high_y+top)
    cv2.circle(img,dire, 5, (0, 255, 0), -1)
    # cv2.imshow("img",img)
    line = (now,dire)
    return line

def find_angle(img):
    line = fine_line(img)
    if(line == False):
        print("cant find line")
        return False
    now,dire = line
    x0,y0=now #起点
    x1,y1=dire #终点
    a = x1 - x0
    b = y1 - y0
    c = math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0))
    cosa = a / c
    sina = b / c
    return (sina , cosa)

# #flygps 217,1855
# 195,1865 r=150

def find_coor(img):
    #fly-gps操作摇杆坐标
    centerpoint = (160,1200)
    r = 120

    angle = find_angle(img)
    if(angle == False):
        print("cant find angle")
        return False
    press_x = centerpoint[0] + r * angle[1]
    press_y = centerpoint[1] + r * angle[0]
    cv2.circle(img, (int(press_x) , int(press_y)), 5, (255, 255, 0), -1)
    # cv2.imshow("img",img)
    cv2.imwrite('1.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return (press_x , press_y)

def press_point(a):
    x,y=a
    commond = 'adb shell input swipe %d %d %d %d %d' % (x,y,x,y,300)
    # commond = 'adb shell input swipe %d %d %d %d %d' % (x,y,x,y,1000)
    # print(commond)
    os.system(commond)

def getScreenshot():
   # os.system('adb shell input swipe 736 1728 736 1728')
    os.system('adb shell screencap -p /sdcard/run.png')
    os.system('adb pull /sdcard/run.png .')
    img = cv2.imread("run.png")
    return img

def map_control():
    os.system('adb shell input swipe 1212 2724 1212 2724')

def adb_connect():
    os.system('adb devices')
    time.sleep(3)

def do_one_run():
    # map_control()
    # adb_connect()
    time.sleep(4)
    # beginh = datetime.datetime.now().hour
    # beginm = datetime.datetime.now().minute
    # begins = datetime.datetime.now().second
    # sum = beginh*3600+beginm*60+begins+450
    while 1:
        img = getScreenshot()
        # img = cv2.imread("run.png")
        # map_control()
        try:
            os.system('adb shell input swipe 541 1109 541 1109')
            pressPoint = find_coor(img)
            if(pressPoint == False):
                break
            # print(type(pressPoint))
            press_point(pressPoint)
            time.sleep(0)
        except UnboundLocalError:
            break
        # end = datetime.datetime.now()
        # print(end)
        # if (end.hour*3600+end.minute*60+end.second >= sum):
        #     break
    return False
def light_phone():
    os.system('adb shell input keyevent 224')

def close_phone():
    os.system('adb shell input keyevent 223')

def unlock_phone():
    os.system('adb shell input swipe 500 1500 700 23001')





# img = cv2.resize(img , (360,540))
# try:
#     find_coor(img)
# except UnboundLocalError:
#     print("UnboundLocalError")
# getScreenshot();
# press_point((1,2))
# do_one_run()
# img = cv2.imread("wait2.png")
# img = cv2.resize(img , (720, 1080) )
# wait_for_run_ready(img)
# cv2.waitKey(0)