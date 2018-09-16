from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from yatraReservation.test_genericFunctions import generic
import autoit
import time
class gmailtestclass:
    @staticmethod
    def gmail_005(driver, logger, sheet1, TCName):
        Id_locator=(By.XPATH,"//*[@id='identifierId']" )
        nextBtn1_locator=(By.XPATH, "//span[text()='Next']")
        password_locator="//input[@class='whsOnd zHQkBf']"
        nextBtn2_locator=(By.XPATH, "//span[@class='RveJvd snByac']")
        compose_locator="//div[@class='T-I J-J5-Ji T-I-KE L3']"
        to_locator="//*[@id=':b3']"
        sub_locator="//*[@id=':al']"
        attachment_locator=(By.XPATH, "//div[@class='a1 aaA aMZ']")
        send_locator=(By.XPATH, "//div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
        googleAccount_locator=(By.XPATH, "//span[@class='gb_9a gbii']")
        signout_locator="//*[@id='gb_71']"
        
        try:
            emailId=generic.fetchValueFromExcel(sheet1, TCName, "emailId")
            driver.find_element(*Id_locator).send_keys(emailId)
            driver.find_element(*nextBtn1_locator).click()
            time.sleep(10)
            password=WebDriverWait(driver,50).until(
                EC.presence_of_element_located((By.XPATH, password_locator))
                )
            pswd=generic.fetchValueFromExcel(sheet1, TCName, "password")
            password.send_keys(pswd)
            driver.find_element(*nextBtn2_locator).click()
            compose=WebDriverWait(driver,50).until(
                EC.presence_of_element_located((By.XPATH, compose_locator))
                )
            compose.click()
            time.sleep(10)
            
            recipient=generic.fetchValueFromExcel(sheet1, TCName, "recipient")
            subject=generic.fetchValueFromExcel(sheet1, TCName, "subject")
            to=WebDriverWait(driver,50).until(
                EC.presence_of_element_located((By.XPATH,to_locator ))
                )
            to.send_keys(recipient)
        
            sub=WebDriverWait(driver,50).until(
                EC.presence_of_element_located((By.XPATH,sub_locator ))
                )
            sub.send_keys(subject)
        
            driver.find_element(*attachment_locator).click()
        
        
            autoit.win_active("File Upload")
            autoit.control_send("File Upload","Edit1",r"C:\Users\ACER\Desktop\download.jpg")
            
            autoit.control_send("File Upload","Edit1","{ENTER}")
        
            time.sleep(20)
            '''driver.find_element_by_xpath("//*[@id=':b3']").send_keys("timsi.kumari02@gmail.com")
            driver.find_element_by_xpath("//*[@id=':al']").send_keys("Test_mail")'''
            driver.find_element(*send_locator).click()
        
            driver.find_element(* googleAccount_locator).click()
        
            signout=WebDriverWait(driver,50).until(
                EC.presence_of_element_located((By.XPATH, signout_locator))
                )
            signout.click()
            logger.info("attachment made and mail sent")
            
        except Exception as ex:
            logger.error("exception raised is: ", ex)    
            raise ex    
