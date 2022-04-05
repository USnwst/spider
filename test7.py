from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions

def main():

    options = webdriver.ChromeOptions()

    #mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    #options.add_experimental_option('mobileEmulation',mobileEmulation)
    #options.add_experimental_option('w3c',False)

    driver = webdriver.Chrome("D:\python\pachong\chromedriver.exe",options=options)

    driver.get("http://4399dmw.com/donghua/")
    time.sleep(5)

    sell1 = driver.find_element_by_xpath("//input[@id='j-input']")
    driver.execute_script("arguments[0].value='';",sell1)


    time.sleep(7)
    driver.quit()
    pass

if __name__ == '__main__':
    main()