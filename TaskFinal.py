import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Seach_selenide(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')

    def test_Seach_selenide(self):
        # 1.Открытие страницы http://google.com/ncr
        self.drv.get('https://www.google.com/')
        assert 'Google' in self.drv.title

        # 2.Поиск слова “selenide”
        selenide = self.drv.find_element(By.NAME, "q")
        selenide.send_keys('Selenide')
        selenide.send_keys(Keys.RETURN)
        assert 'Selenide' in self.drv.title

        # 3.Провека, что первый результат – ссылка на сайт selenide.org.
        selenide_link = 'https://ru.selenide.org/'
        first_link = self.drv.find_element(By.XPATH, '//cite [@class="tjvcx GvPZzd cHaqb"]')
        first_link.click()
        first_link = self.drv.current_url
        assert selenide_link == first_link
        self.drv.back()

        # 4.Переход в раздел поиска изображений
        images = self.drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        images.click()
        time.sleep(1)


        # 5.Проверка, что первое изображение неким образом связано с сайтом selenide.org.
        first_image = self.drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]').get_attribute("href")
        assert "https://ru.selenide.org/" in first_image

        # 6.Вернуться в раздел поиска Все
        self.drv.back()
        time.sleep(2)


        # 7.Проверяем, что первый результат такой же, как и на шаге 3.
        first_link2 = self.drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a')
        first_link2.click()
        first_link2 = self.drv.current_url
        assert first_link == first_link2

        self.drv.back()

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()
