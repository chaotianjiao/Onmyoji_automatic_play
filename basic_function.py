# -*- coding: utf-8 -*-
# Author: Felix
# Date  : 2019-07-29 12:11
import pyautogui as pyg
import time
import random


def basic(X, Y, use_time):

    pyg.doubleClick(X, Y)
    # 依据个人实力，设置刷一轮御魂的时间，建议比完成时间多8~10秒
    time.sleep(use_time)
    # 模仿手动点击，防止被网易封
    interval = random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    # 结束界面，进入新一轮
    pyg.click(clicks=4, interval=0.8+interval)
    return None
