import pyautogui as pyg
from icecream import ic
import time
import random
X, Y = pyg.locateCenterOnScreen('omoji.png')
def omoji_auto():
    # ic(X, Y)
    pyg.doubleClick(X, Y)
    time.sleep(48)
    pyg.moveRel(None, -5)
    interval = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])
    pyg.click(clicks=3, interval=0.5+interval)
    time.sleep(3)


for i in range(0, 1000):
    omoji_auto()
    ic(i)



