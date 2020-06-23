from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class YandexSearch(unittest.TestCase):
    def setUp(self):
        self.chrome_driver_path = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.driver.get("https://yandex.ru/")
        self.driver.implicitly_wait(10)
        self.entry_win = self.driver.find_element(By.ID, 'text')
        self.entry_win.send_keys("Тензор")
        self.driver.implicitly_wait(10)
        self.suggest = self.driver.find_element(By.CLASS_NAME, "mini-suggest__popup-content")
        self.entry_win.send_keys(Keys.RETURN)

    def test_entry_win(self):

        self.assertTrue(self.suggest and self.entry_win)


unittest.main()
