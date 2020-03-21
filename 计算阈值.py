import cv2
import numpy as np
import jietu

img_gray = jietu.window_capture()
template = cv2.imread('mario_coin.PNG', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

L = 0


R = 1
count = 0
while count < 20:
    threshold = (L+R)/2
    count += 1
    loc = np.where(res >= threshold)
    if len(loc[0]) > 1:
        L += (R-L) /2
    elif len(loc[0]) == 1:
        pt = loc[::-1]
        print('目标区域的左上角坐标:',pt[0],pt[1])
        print('次数:',count)
        print('阀值',threshold)
        break
    elif len(loc[0]) < 1:
        R -= (R-L) / 2


cv2.rectangle(img_gray,pt,(pt[0]+w,pt[1]+h),(34,139,34),2)

cv2.imshow("img_template",template)
cv2.imshow("processed",img_gray)

cv2.waitKey(0)