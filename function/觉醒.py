# Author:feng.yuzhang
import time
import random
import pyautogui as pyg
from colorama import Fore

x,y =1856,491

# 为了防封，设置点击间隔为随机间隔

# 下面开始计数刷(先手动设置好邀请谁，小动物等等,打开到组队准备界面)
for i in range(1, 10000):
    # 首先点击开始
    pyg.click(x=x, y=y)
    # 等待刷完一轮时间
    time.sleep(12)
    # 开始点击
    pyg.doubleClick(interval=1)
    # 平移到队友号窗口
    pyg.moveTo(682, 409)
    pyg.tripleClick(interval=1.5)
    pyg.doubleClick(interval=2)
    # 然后移回队长窗口
    pyg.doubleClick(x=x, y=y, interval=2)
    print(Fore.CYAN + '目前已刷', end='')
    print(Fore.RED+str(i), end='')
    print(Fore.CYAN + '次')


