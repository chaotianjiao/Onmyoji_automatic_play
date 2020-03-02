# -*- coding: utf-8 -*-
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        # 获得坐标
        x, y = pyautogui.position()
        # 显示坐标，调整占位宽度，这里是四位
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # 显示坐标
        print(positionStr, end='')
        # 删除以前坐标，并更新新坐标
        print('\b' * len(positionStr), end='', flush=False)
except KeyboardInterrupt:
    print('\n')





