import xlrd
import time
from selenium.webdriver.common.by import  By
from viaReservation.genericFunctions import generic

class test_signInClass:
    @staticmethod
    def signInprocess(driver, logger, TCName, sheet1, emailid, password):
        
        email_locator = (By.XPATH, "//*[@id='loginIdText']")
        password_locator= (By.XPATH, "//*[@id='passwordText']")
        signInBtn_locator=(By.XPATH, "//*[@id='loginValidate']")
        
        try:
        
            emailBox=driver.find_element(*email_locator)
            #Flow directed to fetchValueFromExcel(sheet1, TCName, reqVal) to get the value of data - email id
            data_email=generic.fetchValueFromExcel(sheet1, TCName, emailid)
            emailBox.send_keys(data_email)
        
            passwordBox=driver.find_element(*password_locator)
            #Flow directed to fetchValueFromExcel(sheet1, TCName, reqVal) to get the value of data - password
            data_password=generic.fetchValueFromExcel(sheet1, TCName, password)
            driver.implicitly_wait(20)
            passwordBox.send_keys(data_password)
            #Flow directed t ocaptureScreenshot(driver, TCName ) to capture screenshot of the above step
            generic.captureScreenshot(driver, TCName )
            time.sleep(5)
            driver.find_element(*signInBtn_locator).click()
            logger.info("values entered successfully")
        
        
         
        except Exception as ec:
            logger.error("exception raised as : ", ec)
