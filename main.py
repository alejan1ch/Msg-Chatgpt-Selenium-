from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import time
import threading
import subprocess
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
from login import Login
from messages import Message

# Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)
new_message = Message()


    

#Linkedin LogIn
new_login = Login(driver)

sleep(1)
# Navigate to job search page
url='https://www.linkedin.com/search/results/people/?keywords=recruiter&network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=13&profileLanguage=%5B%22es%22%5D&sid=cg2'
driver.get(url)

while True:
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        start_time = time.time()
        # Hacemos scroll hasta el final de la página
        while True:
            driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
            # Esperamos a que la página se cargue
            sleep(1)
            # Calculamos la nueva altura de la página y comparamos con la altura anterior
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                driver.execute_script("window.scroll({ top: 0, left: 0, behavior: 'smooth' });")
                sleep(1)
                break
            last_height = new_height
            # Salimos del bucle si han pasado 5 segundos
            if time.time() - start_time >= 5:
                driver.execute_script("window.scroll({ top: 0, left: 0, behavior: 'smooth' });")
                sleep(1)
                break
    finally:    
        recruiters = driver.find_elements(By.CLASS_NAME, 'reusable-search__result-container')
        print(len(recruiters))
        
        for i in range(0, len(recruiters)):
            try:
                button = recruiters[i].find_element(By.TAG_NAME, 'button')
                actions.move_to_element(button).click().perform()
                sleep(2)
                print(f"El botón existe.{i+1}")
                name = recruiters[i].find_element(By.CSS_SELECTOR, 'span[dir="ltr"] > span[aria-hidden="true"]').text.replace('"', '')
                info = recruiters[i].find_element(By.CLASS_NAME, 'entity-result__primary-subtitle.t-14.t-black.t-normal').text.replace('"', '')
                if " at " in info:
                    info = info.split('at')
                    position= info[0]
                    company= info[1]
                elif ' en ' in info:
                    info = info.split('en')
                    position= info[0]
                    company= info[1]
                else:
                  position = info  
                  company= ''
                print(f"{name}, {position}, {company}")
            except NoSuchElementException:
                print(f"El botón no existe.{i+1}")
            else:
                attach_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label*="Attach"]')
                actions.move_to_element(attach_btn).click().perform()
                sleep(2)
                subprocess.run(["C:/Users/alcrh/OneDrive - Instituto Tecnológico de Minatitlán/Escritorio/ALE/PYTHON/Day 71/uploadfile.exe"])
                sleep(1)
                
                try:
                    input_message = driver.find_element(By.CSS_SELECTOR, 'div.msg-form__contenteditable[role="textbox"]')
                    print('i can send')
                    actions.move_to_element(input_message).double_click().send_keys(Keys.ENTER).perform()
                    sleep(2)
                except NoSuchElementException:
                    print('No plaec to send')
                else:
                    msg = new_message.message(name, position, company)
                    actions.move_to_element(input_message).double_click().send_keys(msg).send_keys(Keys.ENTER).perform()
                    

                    # input_message.send_keys(Keys.ENTER)
                
                sleep(3)  
                close_btn = driver.find_element(By.CSS_SELECTOR, 'button[class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]')
                actions.move_to_element(close_btn).click().perform()    
                print('should be close')            
       
        next_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')  
        actions.move_to_element(next_btn).click().perform()

driver.quit()
