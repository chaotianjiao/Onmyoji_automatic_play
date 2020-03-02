# Author:feng.yuzhang
# Time:2020/3/2 16:43
# Project:Onmyoji_automatic_play
import pyautogui as pyg
import time
from icecream import ic
# 第一个号的按钮位置
for i in range(1000):
    x1, y1 = 0, 0
    pyg.click(x=x1, y=y1)
    # 第二个号的按钮位置
    x2, y2 = 0, 0
    pyg.moveTo(x2, y2, duration=1)
    pyg.click()
    time.sleep(100)
    ic("目前已刷{}次".format(i))


