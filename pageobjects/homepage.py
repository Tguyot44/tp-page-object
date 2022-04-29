from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Homepage:

    hamburguer_menu_selector = "#nav-hamburger-menu"
    side_menu_selector = "#hmenu-canvas"
    livres_menu_selector = "a[data-menu-id='10']"
    tous_les_livres_selector = "ul.hmenu-visible li:nth-of-type(3)"
    cookie_button_selector = "#sp-cc-accept"

    def __init__(self, driver: wd.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver,3)

    def open_all_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.hamburguer_menu_selector)))
        self.driver.find_element(By.CSS_SELECTOR, self.hamburguer_menu_selector).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.side_menu_selector)))

    def open_book_category(self):
        self.driver.find_element(By.CSS_SELECTOR, self.livres_menu_selector).click()
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.livres_menu_selector)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.tous_les_livres_selector)))

    def open_all_books(self):
       self.driver.find_element(By.CSS_SELECTOR, self.tous_les_livres_selector).click()

    def closeCookie(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cookie_button_selector).click()