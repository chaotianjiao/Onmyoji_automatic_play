# -*- coding: utf-8 -*-
# Author: Felix
# Date  : 2019-07-29 11:55
from basic_function import basic
from icecream import ic
if __name__ == '__main__':
    for i in range(1, 1000):
        basic(use_time=60, path='./resource/御灵按钮.png')
        ic(i)
