import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    basket = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert basket.text, "Añadir al carrito"
    print(basket.text)