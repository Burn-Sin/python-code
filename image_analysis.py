import cv2
import numpy as np
import jietu



a = cv2.imread('renwu.png',0)  #人物
b = cv2.imread('coin.png',0)  #钱币





n1 = []
def jisuan(tex,w,h):
    n1 = tex[0] + w//2
    n2 = tex[1] + h
    n3 = n1,n2
    return n3
class analysis:
    def __init__(self,template):
        self.template = template
    def analysis(self):
        if self.template==1:
            template = a
        elif self.template==2:
            template = b
        h, w = template.shape[:2]  # rows->h, cols->w
        gray = jietu.window_capture()
        # 相关系数匹配方法：cv2.TM_CCOEFF
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        left_top = max_loc  # 左上角
        #right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角

        #cv2.rectangle(img, left_top, right_bottom, (0,0,255), 2)  # 画出矩形位置
        #cv2.imshow('123',img)
        #cv2.waitKey(0)
        self.r = jisuan((left_top) ,w ,h)
        return self.r
    def analysis_double(self):
        if self.template==1:
            template = a
        elif self.template==2:
            template = b
        img_gray = jietu.window_capture()
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res > threshold)
        self.r2 = []
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            self.r2.append(jisuan(pt,w,h))
        return self.r2
        #cv2.imshow('123',img_gray)
        #cv2.waitKey(0)

#analysis(2).analysis_double()