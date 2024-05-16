from selenium import webdriver
from webdriver_helper import get_webdriver
from selenium.webdriver.common.keys import Keys
#注意安装  pip install webdriver_helper==1.0.1  其他收费
driver = get_webdriver("chrome")     #获取浏览器驱动
#driver.get("https://www.baidu.com")   #控制浏览器
#driver.get_screenshot_as_file("a.png")  #截图保存
#driver.maximize_window()
#driver.get_screenshot_as_file("b.png")  #窗口最大化

driver.get("https://music.163.com/")
#print("当前网址：",driver.current_url)
#print("当前标题：",driver.title)
#    <input type="text" name="srch" id="srch" class="txt j-flag" value="" style="opacity: 1;">

#el_1=driver.find_element(by='id',value='srch')  #根据属性进行定位
#el_2=driver.find_element(by="name",value="srch")
#el_3=driver.find_element(by="tag name",value="input")
#print(el_1)
#print(el_2)
#print(el_3)

#el=driver.find_element(by="link text",value="发现音乐")
#print(el)  #根据文本进行定位

#el1=driver.find_element(by="css selector",value="#g-topbar > div.m-top > div > ul > li.fst > span > a")  #定位CSS选择器匹配的元素
#el2=driver.find_element(by="xpath",value='//*[@id="g-topbar"]/div[1]/div/ul/li[1]/span/a')  #定位XPath表达式匹配的元素
#print(el1)
#print(el2)

#el1=driver.find_element(by="css selector",value='')
#<a href="/discover/playlist/?cat=%E7%94%B5%E5%AD%90" class="s-fc3">电子</a>
#el1=driver.find_element(by="link text",value="电子")  #根据文本定位不行
#el2=driver.find_element(by="class name",value="s-fc3")  #根据属性定位可以
#el3=driver.find_element(by="css selector",value="#discover-module > div.g-mn1 > div > div > div:nth-child(1) > div > div > a:nth-child(9)")#根据css选择器定位，不行
#el4=driver.find_element(by="xpath",value='//*[@id="discover-module"]/div[1]/div/div/div[1]/div/div/a[5]') #根据xpath表达式定位，不行
#el5=driver.find_element(by="xpath",value='//*[@id="g_nav2"]/div/ul/li[5]/a')
#<a href="/discover/playlist/" class="tit f-ff2 f-tdn" id="recommend_title">热门推荐</a>
#print(el1)
#print(el2)
#print(el4)

el1=driver.find_element(by='xpath',value='//*[@id="srch"]')
el1.send_keys("一路生花")
el1.send_keys(Keys.ENTER)
driver.implicitly_wait(9)
#driver.find_element(by="xpath",value='//*[@id="auto-id-XePyJ4zPPxFeunZL"]/div/div/div[1]/div[2]/div/div/a').click()

#//*[@id="auto-id-lzCATKDScWixonmW"]/div/div/div[1]/div[2]/div/div/a/b/span
#//*[@id="auto-id-lzCATKDScWixonmW"]/div/div/div[2]/div[2]/div/div/a/b/span
#//*[@id="auto-id-lzCATKDScWixonmW"]/div/div/div[3]/div[2]/div/div/a/b/span
#改写成：//*[@id="auto-id-lzCATKDScWixonmW"]/div/div/div/div[2]/div/div/a/b/span
#<a data-type="1" href="javascript:void(0)" class="z-slt"><em>单曲</em></a>
#<a hidefocus="true" data-type="100" href="javascript:void(0)" class="z-slt"><em>歌手</em></a>

driver.find_element(by='xpath',value='//em[text()="歌手"]/parent::a').click()

#el_list=driver.find_elements(by='xpath',value='//*[@id="auto-id-lzCATKDScWixonmW"]/div/div/div/div[2]/div/div/a/b/span')
#print(el_list)



input()
driver.quit()  #退出浏览器