#coding=utf-8
'''博客园---虫师
http://fnng.cnblogs.com 76
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fvod.kuaibo.com%2F%3Fly%3Ddefault")
#登录系统
driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()
sleep(2)
#获取所有分页的数量，并打印
total_pages=len(driver.find_element_by_tag_name("select").find_elements_by_tag_name("option"))
print "total page is %s" %(total_pages)
sleep(3)
#再次获取所分页，并执行循环翻页操作
pages=driver.find_element_by_tag_name("select").find_elements_by_tag_name("option")
for page in pages:
    page.click()
    sleep(2)
sleep(3)

driver.quit()
