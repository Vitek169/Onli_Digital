import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)

base_url = 'https://only.digital'

try:
    driver.get(base_url) #переходим по ссылке
    driver.maximize_window() #переводим в полноэкракнный режим

    scroll = driver.find_element(By.XPATH, '//*[@id="__next"]/div[5]/main/div[2]/div') # переменная ползунка
    action.click_and_hold(scroll).move_by_offset(0, 850).release().perform() # зажимаем и спускаем вниз ползунок
    tel = driver.find_element(By.XPATH,'//a[@href="tel:+74957409979"]') # переменная элемента футера № телефона
    """переменная элемента футера Вконтакте"""
    vk = driver.find_element(By.XPATH,'//*[@id="__next"]/div[5]/main/div[1]/footer/div[1]/div[2]/div[2]/div/div[2]/a/span')
    """переменная для элемента футера телкграм"""
    telegram = driver.find_element(By.XPATH, '//*[@id="__next"]/div[5]/main/div[1]/footer/div[1]/div[2]/div[2]/div/div[3]/a/span')
    time.sleep(10) # явное ожидание для перемотки сайта


    print(f'Элементы футера найдены! \n{tel.text}, \n{vk.text}, \n{telegram.text}.\nТест закончен!')






finally:
    # закрываем браузер после всех манипуляций
    driver.quit()
