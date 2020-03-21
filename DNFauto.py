import image_analysis
import cv2
#import multiprocessing as mp
import time
import numpy as np
import keybd




def Person_Orientation():  #定位人物坐标
        persom = image_analysis.analysis(1)
        return (persom.analysis())

def stone_Orientation():
        stone = image_analysis.analysis(2)
        break_flage = 1
        while break_flage !=2:
                s = stone.analysis_double()
                print(s)
                if s != []:
                        break_flage = Person_move(Person_Orientation(),s[0])
def Person_move(rw,mb):
        rw = np.array(rw)
        mb = np.array(mb)
        xx = 0-(rw[0]-mb[0])
        yy = 0-(rw[1]-mb[1])
        print(xx,yy)
        p1 = 0
        p2 = 0
        if -56<= xx <=60:
                print("X就绪")
                p1=1
        elif xx>0:
                keybd.key_press(0x27)
                #右
        elif xx<0:
                keybd.key_press(0x25)
                #左
        if -7<= yy <=7:
                print('y就绪')
                p2=1
        elif yy<0:
                keybd.key_press(0x26)
                #上
        elif yy>0:
                keybd.key_press(0x28)
                #下
        if p1+p2==2:
               return 2
if __name__ == "__main__":
    #q = mp.Queue()
    #p1 = mp.Process(target=Person_Orientation,)
    #p1.start()
    #p1.join()
    stone_Orientation()
    #print(Person_Orientation())
