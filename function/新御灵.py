# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/14 19:05
@Author  : Felix
@FileName: 新御灵.py
@Software: PyCharm
"""
import time
import random
import pyautogui as pyg
import numpy as np
from colorama import Fore

"""首先寻找开始按钮"""


x,y =1786,531

# 为了防封，设置点击间隔为随机间隔
seconds = [a for a in np.arange(1, 2, 0.1)]
# 下面开始计数刷(先手动设置好邀请谁，小动物等等,打开到组队准备界面)
for i in range(1, 10000):
    # 首先点击开始
    pyg.click(x=x, y=y)

    # 平移到队友号窗口
    pyg.moveTo(824, 490)
    pyg.doubleClick(interval=2)
    time.sleep(130)


    # 然后移回队长窗口
    pyg.tripleClick(x=x, y=y, interval=2)
    pyg.doubleClick(824,490,interval=2)
    print(Fore.CYAN + '目前已刷', end='')
    print(Fore.RED+str(i), end='')
    print(Fore.CYAN + '次')
 
