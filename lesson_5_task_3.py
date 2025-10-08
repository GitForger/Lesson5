from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть браузер FireFox
driver = webdriver.Firefox()

try:
    # Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Небольшая пауза для загрузки страницы
    time.sleep(2)
    
    # Найти поле ввода по типу (более точный локатор)
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    
    # Ввести в поле текст "Sky"
    input_field.send_keys("Sky")
    
    # Небольшая пауза для наглядности
    time.sleep(1)
    
    # Очистить поле методом clear()
    input_field.clear()
    
    # Небольшая пауза для наглядности
    time.sleep(1)
    
    # Ввести в поле текст "Pro"
    input_field.send_keys("Pro")
    
    # Небольшая пауза чтобы увидеть результат
    time.sleep(2)
    
    print("Скрипт успешно выполнен!")
    
finally:
    # Закрыть браузер
    driver.quit()
