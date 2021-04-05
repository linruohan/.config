from selenium import webdriver


options = webdriver.ChromeOptions()

options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')

driver = webdriver.Chrome(chrome_options = options)

driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

page = driver.find_elements_by_class_name("sf-edu-wenku-id-div_class_1 div_class_1 rtcscontent")

driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去

driver.find_element_by_class_name("fold-arrow-lower").click()
