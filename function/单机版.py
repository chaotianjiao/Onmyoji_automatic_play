import pyautogui as pyg
import time


x,y=790,420
for i in range(1000):
    pyg.moveTo(x,y)
    pyg.click()
    time.sleep(23)
    pyg.tripleClick(interval=2)
    time.sleep(4)
    pyg.doubleClick(interval=2)
    print(i)