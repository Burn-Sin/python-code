
# coding=utf-8

from appium import webdriver

import time, os

class news:

    def __init__(self):

        desired_caps = {}

        desired_caps['noReset'] = 'True'

        # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = '6.0.1'

        desired_caps['deviceName'] = '"cd42ca3d7d73'

        # desired_caps['platformVersion'] = '4.4.2'

        # desired_caps['deviceName'] = '127.0.0.1:62001'

        desired_caps['appPackage'] = 'com.expflow.reading'

        desired_caps['appWaitActivity'] = 'com.expflow.reading.activity.SplashActivity'

        desired_caps['appActivity'] = 'com.expflow.reading.activity.SplashActivity'

        # desired_caps['app'] = PATH(r"C:\Users\zhou\Downloads\com.jifen.qukan_3.9.6.000.0110.1453_liqucn.com.apk")

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
        


    # driver.find_elements_by_xpath("//*[@resource-id='com.jifen.qukan:id/aas']")[1].click()

    # guanggao=driver.find_element_by_id('com.jifen.qukan:id/aen')

    def huoqunews(self):
        znl = self.driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        znl.click()
        time.sleep(2)
        # 获取新闻
        news = []
        news = self.driver.find_elements_by_id('com.expflow.reading:id/layout_item_news')
        for xw in news:
            print('发现新闻:',xw)
            self.clicknews(xw)
        time.sleep(1)
        self.swipeUp(5000)
    
    
    
    def clicknews(self,ns):
        ns.click()
        try:
            hb = self.driver.find_element_by_id('com.expflow.reading:id/rv_read_progress')
        except:
            try:
                quit2 = self.driver.find_element_by_id('com.expflow.reading:id/iv_close')
            except:
                pass
            else:
                quit2.click()
        else:        
            for __ in range(4):
                    time.sleep(4)
                    self.swipeUp(3000)
            time.sleep(1)
            try:
                quit2 = self.driver.find_element_by_id('com.expflow.reading:id/iv_close')
            except:
                pass
            else:
                quit2.click()
    
    
    
    def quit(self):
        self.driver.quit()


    
    def swipeUp(self, t=500):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5 # x坐标
        y1 = l['height'] * 0.75 # 起始y坐标
        y2 = l['height'] * 0.25 # 终点y坐标
        try:
            self.driver.swipe(x1, y1, x1, y2, t)
        except:
            pass

if __name__ == '__main__':
    news1 = news()
    while True:
        news1.huoqunews()
    #news1.quit()