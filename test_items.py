from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_button(browser):
    browser.get(link)
    add_button = browser.find_elements(By.XPATH, '//form[@id="add_to_basket_form"]/button')
    assert len(add_button) > 0, "add button doesn't found"
