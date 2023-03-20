from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

drv = webdriver.Chrome('chromedriver.exe')
drv.get('https://www.google.com/ncr')
assert 'Google' in drv.title
elm = drv.find_element(By.NAME, "q")
elm.send_keys('Python')
elm.send_keys(Keys.RETURN)

print(drv.title)
assert 'No results found' not in drv.page_source
drv.close()
