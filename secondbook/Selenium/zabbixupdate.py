import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from conf import login, password
driver = webdriver.Chrome(executable_path='C:\\zabbixpy\\chromedriver.exe')

try:
    driver.get('https://.com/zabbix')
    time.sleep(5)
    username = driver.find_element_by_name("name")
    username.clear()
    username.send_keys(f"{login}")

    time.sleep(5)
    passwodr = driver.find_element_by_name("password")
    passwodr.clear()
    passwodr.send_keys(f"{password}")
    time.sleep(1)
    passwodr.send_keys(Keys.ENTER)
    time.sleep(10)


except Exception as error:
    print(error)

try:
    driver.get("https://m324")
    time.sleep(3)
    pressupdate = driver.find_element_by_name("update")
    time.sleep(5)
    pressupdate.send_keys(Keys.ENTER)
    time.sleep(5)
except Exception as host_error:
    print(host_error)

finally:
    driver.close()
    driver.quit()

