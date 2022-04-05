import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def web():
    options = webdriver.ChromeOptions()

    # mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # options.add_experimental_option('mobileEmulation',mobileEmulation)

    driver = webdriver.Chrome("D:\python\pachong\chromedriver.exe", options=options)

    driver.implicitly_wait(10)

    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")





    time.sleep(10)
    driver.quit()

    pass

def main():
    try:
        web()
    except:
        print("页面太慢啦")

    pass

if __name__ == '__main__':
    main()
