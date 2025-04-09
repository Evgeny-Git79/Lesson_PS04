from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import  By
import time

browser = webdriver.Firefox()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")
print("Введите строку для поиска")
input_find_str = input()
search_box.send_keys(input_find_str)
time.sleep(5)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

while True:
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    for paragraph in paragraphs:
        print("----------------------------------")
        print(paragraph.text)
        print("Для выхода из списка параграфов нажмите 1, для продолжения нажмите enter")
        input_find_str = input()
        if input_find_str == "1":
            break

    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            print("----------------------------------")
            print("Статья", element.find_element(By.TAG_NAME, "a").get_attribute("title"))
            print("Для перехода по статье введите 1, для следующей статьи нажмите enter")
            input_find_str = input()
            if input_find_str == "1":
                link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                browser.get(link)
                break





