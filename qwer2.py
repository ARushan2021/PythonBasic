from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drv = webdriver.Chrome('chromedriver.exe')
drv.get('https://www.google.com/search?q=selenide')
assert 'selenide' in drv.title
selenide_link = 'https://ru.selenide.org/'
time.sleep(2)

first_link = drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/cite')
first_link.click()
first_link = drv.current_url

if first_link == selenide_link:
    print('первая проверка прошла')
    print(first_link)
else:
    print('первая не проверка прошла')
    print(first_link)

drv.back()

image = drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
image.click()
first_image = drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]/span')
first_image.click()
drv.switch_to.window(drv.window_handles[1])
first_image1 = drv.current_url

if first_image1 == selenide_link:
    print('вторая проверка прошла')
    print(first_image1)
else:
    print('вторая не проверка прошла')
    print(first_image1)

drv.close()
drv.switch_to.window(drv.window_handles[0])
drv.back()

if first_image1 == first_link:
    print('третья проверка прошла')
    print(first_image1, ' = ', first_link)
else:
    print('третья не проверка прошла')
    print(print(first_image1, ' не равно ', first_link))

assert 'No results found' not in drv.page_source