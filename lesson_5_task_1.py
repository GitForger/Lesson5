from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_blue_button():
    """
    Тестирование клика по синей кнопке на странице Class Attribute
    """
    try:
        # Настройка Chrome WebDriver
        driver = webdriver.Chrome()
        
        # Открыть страницу
        print("Открываем страницу...")
        driver.get("http://uitestingplayground.com/classattr")
        
        # Ждем загрузки страницы
        wait = WebDriverWait(driver, 10)
        
        # Находим синюю кнопку по классу (обычно это кнопка с классом 'btn-primary')
        # На этой странице синяя кнопка имеет класс 'btn-primary'
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        
        # Кликаем на синюю кнопку
        print("Кликаем на синюю кнопку...")
        blue_button.click()
        
        # Обрабатываем alert (если появится)
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            print(f"Alert текст: {alert.text}")
            alert.accept()
            print("Alert принят")
        except:
            print("Alert не появился")
        
        # Небольшая пауза для визуального наблюдения
        time.sleep(2)
        
        print("Тест успешно завершен!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        


if __name__ == "__main__":
    test_blue_button()
