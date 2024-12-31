import time
from pages.product import ProductPage
from pages.homepage import Homepage

def test_open_s6(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')

def test_monitors(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_product_count(2)