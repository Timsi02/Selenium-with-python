```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from yatraReservation.signInPage import test_signInClass
from yatraReservation.flightReservationPage import test_flightReservationclass
from yatraReservation.help import test_helpclass
from yatraReservation.forex import test_forexclass
from selenium.webdriver.support.select import Select
from yatraReservation.genericFunctions import generic
class test_homePage:
    
    
    
    @staticmethod
    def signIn_001(driver, logger, TCName, sheet1, emailid, password):
        signInBtn_locator=(By.XPATH,"//*[@id='SignIn']/div")
        driver.find_element(*signInBtn_locator).click()
        
        try:
            test_signInClass.signInprocess(driver, logger, TCName, sheet1, emailid, password)
            logger.info("signin details entered")
        except Exception as ex:
            logger.error("unable to enter sign in details :", ex)  
            
            
        
    @staticmethod
    def flight_002(driver, logger, TCName, sheet1, flight_source, flight_destination):
        flightTab_locator=(By.XPATH, "//*[@id='Flights']")
        
        try:
            driver.find_element(*flightTab_locator).click()
            test_flightReservationclass.flight_reservation(driver, logger, TCName, sheet1, flight_source, flight_destination)
            logger.info("flighy reservation page navigation is successful")
            
        except Exception as e:
            logger.error("excepton raised is: ", e)  
            raise e  
      
    
        
    @staticmethod
    def help_003(driver, logger, TCName):
        helpBtn_locator=(By.XPATH, "//*[@id='helpShiftFaq']")
        
        try:
            driver.find_element(*helpBtn_locator).click()
            logger.info("element found")
        except Exception as e:
            logger.warn("element not found, exeception raised: ", e)    
        test_helpclass.help(driver, logger, TCName) 
        
        

    @staticmethod
    def forex_004(driver, TCName, logger):
        try:
            test_forexclass.forex(driver, logger)
            logger.info("moving to forexclass")
        except Exception as ex:
            logger.error("exception raised is: ", ex)    
        
    @staticmethod
    def policies_006(driver, logger, TCName):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            generic.captureScreenshot(driver, TCName )
            driver.find_element_by_xpath("/html/body/div[12]/div[4]/div/div/div[1]/div[4]/ul/li[3]/a").click()
            logger.info("policy page opened")   
        except Exception as e: 
            logger.error("exception raised is: ", e)
            raise e   
   ```         
            
            
