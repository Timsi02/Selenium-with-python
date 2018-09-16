from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from yatraReservation.test_genericFunctions import generic
class test_helpclass:
    @staticmethod
    def help(driver, logger, TCName):
        '''question_Locator=(By.XPATH, "//a[contains(text(),'How much Points (Via Cash) can I redeem for a booking?')]")'''
        
        '''TS=generic.getCurrentTime()
        exePath=".\\Screenshots\\"+"Execution_"+TS+"\\"+"screenshot_"'''
        try:
            driver.switch_to.frame("hs-support-frame")
          
            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'How much Points (Via Cash) can I redeem for a booking?')]")))
                 
            element.click()
            generic.captureScreenshot(driver, TCName )                                                                            
            driver.switch_to.default_content()
            logger.info("frame switched successfully")
        except Exception as e:
            logger.warn("frame switch unsuccessful, exception raised: ", e)
            raise e
                
