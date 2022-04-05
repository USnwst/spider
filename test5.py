import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def main():


    options = webdriver.ChromeOptions()

    #mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    #options.add_experimental_option('mobileEmulation',mobileEmulation)

    driver = webdriver.Chrome("D:\python\pachong\chromedriver.exe")

    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")


    js = 'window.open("http://www.baidu.com")'
    driver.execute_script(js)

    print(driver.current_url)

    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)


    time.sleep(10)
    driver.quit()
    pass


if __name__ == '__main__':
    main()