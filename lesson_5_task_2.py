from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_dynamic_id():
    """Тест для клика на кнопку с динамическим ID"""
    
    # Настройка Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    try:
        # Инициализация драйвера
        driver = webdriver.Chrome(options=chrome_options)
        
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        
        # Ожидание загрузки страницы
        time.sleep(2)
        
        # Поиск и клик на синюю кнопку
        # Используем XPath который ищет кнопку по классу и тексту, игнорируя динамический ID
        blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
        blue_button.click()
        
        print("✅ Успешно: Кнопка с динамическим ID была нажата")
        
        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        
    finally:
        # Закрытие браузера
        if 'driver' in locals():
            driver.quit()
            print("✅ Браузер закрыт")

if __name__ == "__main__":
    test_dynamic_id()