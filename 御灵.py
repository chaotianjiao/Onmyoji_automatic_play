# -*- coding: utf-8 -*-
# Author: Felix
# Date  : 2019-07-29 11:55
from icecream import ic
from basic_function import basic
import time
import pyautogui as pyg
X, Y = pyg.locateCenterOnScreen('resource/御灵按钮.png')


if __name__ == '__main__':
    # 可更改右边的数值设定要刷的次数
    for i in range(1, 1000):
        # 依据每个人御魂耗时不同，请自行设定use_time,建议比完成时间大8~10秒
        basic(X=X, Y=Y, use_time=60)
        # 显示已经刷了多少次
        ic(i)
