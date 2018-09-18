import xlrd
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from viaReservation.test_genericFunctions import generic

class test_flightReservationclass:
    @staticmethod
    def flight_reservation(driver, logger, TCName, sheet1, flight_source, flight_destination):
        source_locator=(By.XPATH, "//*[@id='source']")
        destination_locator=(By.XPATH, "//*[@id='destination']")
        source_drpdwn_locator= "//*[@class='ui-menu-item']//following::*[@class='name'][1]"
        destination_drpn_locator="//*[@class='ui-menu-item']//following::*[@class='name'][2]"
        journey_date_locator="//div[@class='searchbox  recentSearch searchBoxHome']//following::div[@class='container']//following::div[@class='content']//following::form[@class='flightSearchForm']//following::div[@class='panel']//following::div[@id='round-trip-panel']//following::div[@class='element']//following::div[@id='depart-cal']//following::div[@data-month='9']//following::div[@class='vc-month-box']//following::div[@class='vc-row'][5]//following::div[@data-date='29']"
        person_locator=(By.XPATH, "//div[@class='plus']")
        searchFlight_locator=(By.XPATH, "//*[@id='search-flight-btn']")
        arrow_locator="/html/body/div[4]/div[3]/div/form/div[4]/div[1]/div[4]/div[1]/div[4]/div[1]/span[3]"
        
        try:
            flightSrc=generic.fetchValueFromExcel(sheet1, TCName, flight_source)
            flightDest=generic.fetchValueFromExcel(sheet1, TCName, flight_destination)
        
            source=driver.find_element(*source_locator)
            source.send_keys(flightSrc)
            source_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, source_drpdwn_locator)))
            source_element.click()
        
            destination=driver.find_element(*destination_locator)
            destination.send_keys(flightDest)
            dest_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, destination_drpn_locator)))
            dest_element.click()
            '''source.send_keys(Keys.ARROW_DOWN)
            source.send_keys(Keys.ENTER)'''
        
        
            arrow = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, arrow_locator)))
            arrow.click()
        
            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, journey_date_locator)))
            element.click()
        
            driver.find_element(*person_locator).click()
            driver.find_element(*searchFlight_locator).click()
            time.sleep(20)
            generic.captureScreenshot(driver, TCName )
            logger.error("list of flights load is successful") 
            
        except Exception as e:
            logger.error("list of flights load is unsuccessful")   
            raise e 
