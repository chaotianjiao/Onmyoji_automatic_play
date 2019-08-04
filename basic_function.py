# -*- coding: utf-8 -*-
# Author: Felix
# Date  : 2019-07-29 12:11
import pyautogui as pyg
import time
import random


# 首次启动时，获取用户的单次刷御魂/灵/贪嗔痴用时
def get_use_time():
    use_time = pyg.prompt(text='请输入完成一轮任务所需的时间', title='时间设定')
    try:
        use_time = int(use_time)
    except NameError:
        pyg.alert(title='请输入正确的时间!!!')
        get_use_time()
    return use_time


def basic(x,y, use_time):
    # 找到按钮的位置

    # 点击开始刷
    pyg.doubleClick(x, y)
    # 依据个人实力，设置刷一轮御魂的时间，建议比完成时间多5~8秒
    time.sleep(use_time)
    # 刷完模仿手动点击，防止被网易封
    interval = random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    # 结束界面，进入新一轮
    pyg.click(clicks=4, interval=0.8+interval)
    return None
