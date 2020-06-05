from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import unittest

class TestAbs(unittest.TestCase):
    def test1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            # link = "http://suninjuly.github.io/registration2.html"
            # link = "http://suninjuly.github.io/math.html"
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
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Bug blockker")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

        def test1(self):
            try:
                link = "http://suninjuly.github.io/registration1.html"
                # link = "http://suninjuly.github.io/registration2.html"
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
                self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Bug blockker")

            finally:
                # ожидание чтобы визуально оценить результаты прохождения скрипта
                time.sleep(5)
                # закрываем браузер после всех манипуляций
                browser.quit()

    def test2(self):
        try:
            # link = "http://suninjuly.github.io/registration1.html"
            link = "http://suninjuly.github.io/registration2.html"
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
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Bug blockker")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    # test1()
        # test_abs2()
    unittest.main()