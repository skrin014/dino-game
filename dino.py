import pyautogui
import cv2
import numpy as np
import time

while True:
 im = pyautogui.screenshot('img.png',region=(300,410,70,100))
 num = np.sum(im)
 print(num)
 if num < 5140000:
     pyautogui.press('space')
   
