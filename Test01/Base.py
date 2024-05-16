# 封装公共方法
from webdriver_helper import get_webdriver


class Base:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = get_webdriver("chrome")
        elif browser == "firefox":
            self.driver = get_webdriver("firefox")
        elif browser == "ie":
            self.driver = get_webdriver("ie")
        else:
            assert "请输入正确的浏览器！！！"

    def geturl(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
