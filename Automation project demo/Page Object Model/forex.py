from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
class test_forexclass:
    @staticmethod
    def forex(driver, logger):
        forexBtn_locator=(By.XPATH,"//*[@id='Forex']")
        buyForexBtn_locator=(By.XPATH, "//a[text()='Buy Forex']") 
        city_locator=(By.XPATH,"//a[text()='Bangalore']")
        hoverEl_locator=(By.XPATH, "//a[text()='English']")
        
        try:
            driver.find_element(*forexBtn_locator).click()
            window_before=driver.window_handles[0]
            logger.info ("window_before is:",window_before)
            driver.find_element(*buyForexBtn_locator).click()
            time.sleep(30)
            window_after=driver.window_handles[1]   
            logger.info ("window_after is :", window_after)
            driver.switch_to_window(window_after)
        
            location=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//a[text()='Bangalore']"))
                )
            location.click()
            hover_element=driver.find_element(*hoverEl_locator)
            hover = ActionChains(driver).move_to_element(hover_element)
            hover.perform()
            time.sleep(2)
            language=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/form/div[6]/div/div[3]/div[2]/ul[1]/li[2]/div/ul/li[1]"))
                )
            language.click()
            time.sleep(30)
            
            selectService=Select(driver.find_element_by_class("sel-service"))
            selectService.select_by_index(1)
            time.sleep(5)
            driver.switch_to_window(window_before)
            logger.info("window navigation and hover is successful")
            
        except Exception as ec:
            logger.error("exception raised is: ", ec)    
        
