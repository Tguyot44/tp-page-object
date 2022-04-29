from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Productpage:

    add_to_cart_button_selector = "#add-to-cart-button"
    added_to_cart_confirmation_message_selector = "#sw-atc-details-single-container"

    def __init__(self, driver: wd.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, self.add_to_cart_button_selector)))
        self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart_button_selector).click()
        self.wait.until(expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR, self.added_to_cart_confirmation_message_selector
        )))
