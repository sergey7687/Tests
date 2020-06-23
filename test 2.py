from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class ImagesSearch(unittest.TestCase):
    def setUp(self):
        self.path = 'C:\Program Files (x86)\chromedriver.exe'

        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://yandex.ru")

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.entry_win = self.driver.find_element(By.CSS_SELECTOR, "[data-id='images']")
        self.entry_win.click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.picture_win = self.driver.find_element(By.CSS_SELECTOR, '#main > div > div > div:nth-child(1) > '
                                                                     'div:nth-child(1) > div > a')
        self.picture_win.click()

        self.driver.implicitly_wait(10)
        self.picture = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.cl-viewer > div.cl-viewer__layout "
                                                                 "> div > div.cl-viewer-content > div > "
                                                                 "div.cl-viewer-image > div > div > div > img")

        self.pick_arrow_right = self.driver.find_element(By.CSS_SELECTOR,
                                                         "#root > div > div.cl-viewer > div.cl-viewer-navigate > div")
        self.pick_arrow_right.click()

        self.driver.implicitly_wait(10)
        self.pick_arrow_left = self.driver.find_element(By.CSS_SELECTOR,
                                                        "#root > div > div.cl-viewer > div.cl-viewer-navigate > "
                                                        "div.cl-viewer-navigate__item.cl-viewer-navigate__item_left")
        self.pick_arrow_left.click()

    def test_images(self):
        self.assertTrue(self.entry_win)

    def test_picture_appear(self):
        self.assertTrue(self.picture and self.pick_arrow_left and self.pick_arrow_right)


unittest.main()