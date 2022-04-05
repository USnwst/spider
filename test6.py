import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def main():


    options = webdriver.ChromeOptions()

    #mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    #options.add_experimental_option('mobileEmulation',mobileEmulation)

    driver = webdriver.Chrome("D:\python\pachong\chromedriver.exe",options=options)

    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    time.sleep(1)
    driver.get("http://www.4399dmw.com/huoying/donghua/")

    time.sleep(3)

    driver.maximize_window()
    driver.back()
    driver.refresh()
    driver.forward()



    time.sleep(10)
    driver.quit()
    pass


if __name__ == '__main__':
    main()