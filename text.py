
# coding=utf-8

from appium import webdriver

import time, os

 

class news:

    def setup():

        desired_caps = {}

        desired_caps['noReset'] = 'True'

        # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = '6.0.1'

        desired_caps['deviceName'] = '"cd42ca3d7d73'

        # desired_caps['platformVersion'] = '4.4.2'

        # desired_caps['deviceName'] = '127.0.0.1:62001'

        desired_caps['appPackage'] = 'com.jifen.qukan'

        desired_caps['appWaitActivity'] = 'com.jifen.qkbase.main.MainActivity'

        desired_caps['appActivity'] = 'com.jifen.qkbase.main.MainActivity'

        # desired_caps['app'] = PATH(r"C:\Users\zhou\Downloads\com.jifen.qukan_3.9.6.000.0110.1453_liqucn.com.apk")

        time.sleep(6)

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 阅读新闻

        time.sleep(4)

if __name__ == '__main__':

    setup()
