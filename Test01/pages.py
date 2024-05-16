# pom页面对象模型
from webdriver_helper import get_webdriver
from Base import Base
from selenium.webdriver.common.keys import Keys

class IndexPage(Base):
    url = "https://music.163.com/"
    search_in = get_webdriver().find_element(by='xpath', value='//*[@id="srch"]')

    def search(self,wd):
        self.search_in.send_keys(wd)
        self.search_in.send_keys(Keys.ENTER)



if __name__ == '__main__':
    base = Base("chrome")
    base.geturl(IndexPage.url)
    IndexPage.search("一路")
