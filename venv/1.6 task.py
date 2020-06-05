from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# link = "https://mobsted.com"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR, "div.tn-elem__1873854781588424889456 .tn-atom")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()



# # link = "http://suninjuly.github.io/simple_form_find_task.html"   #шаг 4
# link = "http://suninjuly.github.io/find_link_text"      #шаг 5
# link = "http://suninjuly.github.io/find_xpath_form"     #шаг 8
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     #
#     # link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     # link.click()
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     # button = browser.find_element_by_css_selector("button.btn")
#     # button.click()
#
#     # шаг 8
#     button = browser.find_element_by_xpath("//div/button[text()='Submit']")
#     button.click()
#
#     # шаг 7
#     # browser = webdriver.Chrome()
#     # browser.get("http://suninjuly.github.io/huge_form.html")   #шаг 7
#     # elements = browser.find_elements_by_css_selector("[type='text']")
#     # for element in elements:
#     #    element.send_keys("Мо")
#     #
#     # button = browser.find_element_by_css_selector("button.btn")
#     # button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

try:
    link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block input.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block input.third")
    input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()