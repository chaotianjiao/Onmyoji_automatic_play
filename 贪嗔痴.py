# -*- coding: utf-8 -*-
# Author: Felix
# Date  : 2019-07-31 14:44
from icecream import ic
from basic_function import basic,get_use_time
import pyautogui as pyg
import random

use_time = get_use_time()
if __name__ == '__main__':
    # 可更改右边的数值设定要刷的次数
    for i in range(1, 1000):
        try:
            # 这里贪嗔痴的按钮跟御魂是一样的，所以共用一个
            basic(path='resource/御魂按钮.png', use_time=use_time + 5)
        except TypeError:
            # 多点几次跳到有挑战按钮的界面
            increment = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])
            pyg.click(clicks=3, interval=1 + increment)
            continue
        # 显示已经刷了多少次
        ic(i)
