# Author:feng.yuzhang
import time
import random
import pyautogui as pyg
import numpy as np
from colorama import Fore
# 双号自动挂机防封魂土脚本
"""首先寻找开始按钮"""
# x,y = None, None
# try:
#     # 队长窗口最好放在左上，方便找到
#     x, y = pyg.locateCenterOnScreen('魂土.png')
# except TypeError:
#     location = pyg.prompt(text='输入开始按钮坐标,以逗号分隔',title='开始按钮未找到')
#     # 拆分坐标
#     x, y = (location.split(','))
#     x = int(x)
#     # y = int(y)

x,y =1865,520

# 为了防封，设置点击间隔为随机间隔
seconds = [a for a in np.arange(1, 2, 0.1)]
# 下面开始计数刷(先手动设置好邀请谁，小动物等等,打开到组队准备界面)
for i in range(1, 10000):
    # 首先点击开始
    pyg.click(x=x, y=y)
    # 等待刷完一轮时间
    time.sleep(46)
    # 开始点击
    pyg.doubleClick(interval=random.choice(seconds))
    # 平移到队友号窗口
    pyg.moveTo(669, 432)
    pyg.tripleClick(interval=2)
    pyg.doubleClick(interval=2)
    # 然后移回队长窗口
    pyg.tripleClick(x=x, y=y, interval=2)
    print(Fore.CYAN + '目前已刷', end='')
    print(Fore.RED+str(i), end='')
    print(Fore.CYAN + '次')


