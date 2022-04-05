import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def main():


    options = webdriver.ChromeOptions()

    mobileEmulation = {'driverName': 'iPhone 6/7/8'}
    options.add_experimental_option('mobileEmulation',mobileEmulation)

    driver = webdriver.Chrome("D:\python\pachong\chromedriver.exe")



    driver.get("http://www.4399dmw.com/donghua/")

    ret = driver.find_element_by_xpath("//div[@class='lst-item']/a/div/p").text
    print(ret)

    time.sleep(10)
    driver.quit()
    pass

if __name__ == '__main__':
    main()