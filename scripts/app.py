import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def capturar_dados_clima():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver_path = os.path.join(os.getcwd(), 'drivers', 'msedgedriver.exe')
    driver = webdriver.Edge(service=Service(driver_path), options=options)

    driver.get('https://www.climatempo.com.br')

    try:
        temperatura_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "current-weather-temperature"))
        )
        while temperatura_element.text.strip() == "":
            temperatura_element = driver.find_element(By.ID, "current-weather-temperature")
        temperatura = temperatura_element.text

        umidade_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "current-weather-humidity"))
        )
        while umidade_element.text.strip() == "":
            umidade_element = driver.find_element(By.ID, "current-weather-humidity")
        umidade = umidade_element.text

    except Exception as e:
        print("Erro ao capturar dados:", e)
        temperatura = "N/A"
        umidade = "N/A"
    finally:
        driver.quit()

    return temperatura, umidade
