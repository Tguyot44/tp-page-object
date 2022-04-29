from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Confirmationpage:

    cart_selector = '#nav-cart'
    checkout_selector = 'input[name="proceedToRetailCheckout"]'

    def __init__(self, driver: wd.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.wait.until(expected_conditions.element_to_be_clickable((
            By.CSS_SELECTOR, self.cart_selector
        )))
        self.driver.find_element(By.CSS_SELECTOR, self.cart_selector).click()
        self.wait.until(expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR, self.checkout_selector
        )))
