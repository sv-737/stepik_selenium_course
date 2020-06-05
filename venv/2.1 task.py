from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import os
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    link = "http://suninjuly.github.io/get_attribute.html"
    link = "http://suninjuly.github.io/selects2.html"
    link = "http://SunInJuly.github.io/execute_script.html"
    link = "http://suninjuly.github.io/file_input.html"
    link = "http://suninjuly.github.io/alert_accept.html"
    link = "http://suninjuly.github.io/redirect_accept.html"
    link = "http://suninjuly.github.io/cats.html"
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link)

    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # picture = browser.find_element_by_css_selector("img")
    # x = picture.get_attribute("valuex")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # button.click()

    # in1 = browser.find_element_by_id("button")
    input1 = browser.find_element_by_id('book')
    input1.click()

    # input1 = browser.find_element_by_css_selector("button.trollface")
    # input1.click()
    #
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    #
    # # input1 = browser.find_element_by_css_selector("button.btn")
    # # input1.click()
    # #
    # # input2 = browser.switch_to.alert
    # # input2.accept()
    # #
    x_element = browser.find_element_by_css_selector('span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)
    input2 = browser.find_element_by_css_selector("input.form-control")
    input2.send_keys(y)

    # button.scrollIntoView(true);
    #
    # num1 = browser.find_element_by_css_selector("h2 .nowrap[id='num1']")
    # num2 = browser.find_element_by_css_selector("h2 .nowrap[id='num2']")
    # x = int(num1.text) + int(num2.text)
    # print(x)
    #
    #
    #
    # # Ваш код, который заполняет обязательные поля
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(str(x))
    # input1 = browser.find_element_by_css_selector("input[name='firstname']")
    # input1.send_keys("Вася")
    #
    # input2 = browser.find_element_by_css_selector("input[name='lastname']")
    # input2.send_keys('Васечкин')
    #
    # input3 = browser.find_element_by_css_selector("input[name='email']")
    # input3.send_keys('gjxnj')
    #
    # inputfile = browser.find_element_by_css_selector("input[type='file']")
    # inputfile.send_keys(file_path)

    # # input4 = browser.find_elemenlensk")t_by_id("country")
    # # input4.send_keys("Russia")
    #
    # # Отправляем заполненную форму
    button = browser.find_element_by_id('solve')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # check_box = browser.find_element_by_css_selector("#robotCheckbox")
    # check_box.click()
    # input3 = browser.find_element_by_css_selector("#robotsRule")
    # input3.click()
    button.click()
    #
    # # # Проверяем, что смогли зарегистрироваться
    # # # ждем загрузки страницы
    # # time.sleep(1)
    # #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()