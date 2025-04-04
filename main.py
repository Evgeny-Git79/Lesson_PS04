#from pydoc import browse
from re import search

from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import  By
#Библиотека с поиском элементов на сайте
import time
import random

browser = webdriver.Firefox()

browser.get("https://www.wikipedia.org/")
assert "Wikipedia" in browser.title
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")
print("Введите строку для поиска")
input_find_str = input()
search_box.send_keys(input_find_str)
time.sleep(5)
search_box.send_keys(Keys.RETURN)
time.sleep(5)



