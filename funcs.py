from shutil import move
import keyboard
import time
import random

#x esquerdo: 50.0 direito: 34.0
#y esquerdo: -33.0
#z esquerdo: -3.4000000953674316
def mover(x):
    lmove = ["a", "d"]
    if x >= 48.0:
        mover = "a"
        keyboard.press(mover)
    elif x <= 35:
        mover = "d"
        keyboard.press(mover)
    else:
        mover = random.choice(lmove)
        keyboard.press(mover)
    tmp = random.uniform(0.2,0.3)
    time.sleep(tmp)
    keyboard.release(mover)


