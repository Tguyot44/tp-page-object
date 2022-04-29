from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Bookpage:

    first_book_nouveautes_selector = '[cel_widget_id="handsfree-browse_OctopusNewReleaseAsin"] a[title]'

    def __init__(self, driver: wd.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def select_first_book_nouveautes(self):
        self.wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, self.first_book_nouveautes_selector)))
        self.driver.find_elements(By.CSS_SELECTOR, self.first_book_nouveautes_selector)[0].click()
