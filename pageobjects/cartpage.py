from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class Cartpage:

    quantity_dropdown_selector = '[name="quantity"]'
    prompt_selector = '.a-dropdown-prompt'

    def __init__(self, driver: wd.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def change_quantity(self, desired_quantity):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.quantity_dropdown_selector)))
        Select(self.driver.find_element(
            By.CSS_SELECTOR, self.quantity_dropdown_selector)).select_by_visible_text(desired_quantity)

    def get_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.prompt_selector).text
