# -*- coding: utf-8 -*-
# Author: Felix
# Date  : 2019-07-31 14:44
from icecream import ic
from basic_function import basic,get_use_time
import pyautogui as pyg
import random
X,Y = pyg.locateCenterOnScreen('../resource/贪嗔痴按钮.png')
use_time = get_use_time()
if __name__ == '__main__':
    # 可更改右边的数值设定要刷的次数
    for i in range(1, 1000):
        basic(x=X, y=Y, use_time=use_time + 8)
        increment = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])
        pyg.click(clicks=2, interval=increment + 0.8)

        # 显示已经刷了多少次
        ic(i)
