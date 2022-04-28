from selenium import webdriver
from pageobjects import homepage

def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://amazon.fr/")
    driver.maximize_window()
    hmpage = homepage.Homepage(driver)
    hmpage.closeCookie()
    hmpage.open_all_menu()
    hmpage.open_book_category()
    hmpage.open_all_books()
    driver.quit()