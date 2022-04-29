import time

from selenium import webdriver
from pageobjects import homepage, bookpage \
    , productpage, confirmationpage, cartpage


def test_amazon1():
    expected_quantity = "2"

    driver = webdriver.Chrome()
    driver.get("https://amazon.fr/")
    driver.maximize_window()

    hmpage = homepage.Homepage(driver)
    hmpage.closeCookie()
    hmpage.open_all_menu()
    hmpage.open_book_category()
    hmpage.open_all_books()

    bkpage = bookpage.Bookpage(driver)
    bkpage.select_first_book_nouveautes()

    pdpage = productpage.Productpage(driver)
    pdpage.add_to_cart()

    cfpage = confirmationpage.Confirmationpage(driver)
    cfpage.open_cart()

    crtpage = cartpage.Cartpage(driver)
    crtpage.change_quantity('2')
    current_quantity = crtpage.get_quantity()

    assert current_quantity == expected_quantity, "expected quantity does not match current quantity"
    driver.quit()
