from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
   
def test_check_basket_button_exists(browser):
    
    browser.get(link)
    browser.implicitly_wait(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), f"Button missing"
   
