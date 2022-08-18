from re import X
import keyboard
import time
from pymem import *
from funcs import *
import cv2
import pyautogui
import mouse
from threading import Thread
#declaração imgs cv2
fly = cv2.imread("imgs/fly.png")
fly_w, flw_h, flwidk = fly.shape[::-1]
gible = cv2.imread("imgs/gible.png")
gible_w, gible_h, gibleidk = gible.shape[::-1]
fugir = cv2.imread("imgs/Run.png")
fugir_w, fugir_h, fugiridk = fugir.shape[::-1]
corR = cv2.imread("imgs/corR.png")
corR_w, corR_h, corRidk = corR.shape[::-1]
#inicialização pymem
pm = pymem.Pymem("PokeOne.exe")
GameAssembly = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

#metodo de obter offsets
def GetPtrAddr(base,offsets):
    addr = pm.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_int(addr + i)
    return addr + offsets[-1]

time.sleep(2)
while True:
    #le o endereco retornado do getptraddr
    addr = GetPtrAddr(GameAssembly + 0x00EA94D0,[0x5C,0x0,0x10,0x5C,0x54])
    x = pm.read_float(addr)
    y = pm.read_float(addr+8)
    z = pm.read_float(addr+4)
    #VERIFICA SE O MACACO DO ADM FILHA DA PUTA PUXOU!
    if y != -33.0 or z != -3.4000000953674316 or x > 50 or x < 34:
        print("ADM NA ZONA!!!!")
        break
    #move o boneco...
    mover(x)
    #verifica se entrei em combate!
    xp, yp, w, h = 838, 55, 29, 29
    pyautogui.screenshot("imgs/tempimg.png", (xp, yp, w, h))
    printao = cv2.imread("imgs/tempimg.png")
    fly2 = cv2.matchTemplate(printao,fly,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(fly2) 
    print(max_val)
    if max_val <= 0.75:
        xp, yp, w, h = 909, 961, 33, 27
        print("entrou em luta!")
        while True:
            time.sleep(0.5)
            pyautogui.screenshot("imgs/tempimg.png", (xp, yp, w, h))
            img = cv2.imread("imgs/tempimg.png")
            corR2 = cv2.matchTemplate(img,corR,cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corR2)
            print(max_val)
            if max_val >= 0.95:
                break
        xp, yp, w, h = 32, 12, 29, 12
        pyautogui.screenshot("imgs/tempimg.png", (xp, yp, w, h))
        img = cv2.imread("imgs/tempimg.png")
        gible2 = cv2.matchTemplate(img,gible,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gible2) 
        print(max_val)
        if max_val >= 0.75:
            break
        else:
            mouse.move(1097,1034)
            mouse.click()
            time.sleep(3)
