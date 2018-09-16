```python
import pytest
import xlrd
import logbook
from selenium import webdriver
from yatraReservation.homePage import test_homePage
from yatraReservation.test_gmail_home import gmailtestclass
from yatraReservation.genericFunctions import generic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from shutil import copyfile
import time

dest='test'
def setup_module(module):
    
    TS=generic.getCurrentTime()
    #To make a folder with timestramp
    exePath=".\\Execution_status\\"+"Execution_"+TS+"\\"
    
    y=os.mkdir(exePath)
    print ("directory created")
    
    env="stage"
    
    if(env=="stage"):
        source=".\\Test_data\\viaData_stage.xlsx"
        dest=exePath+"viaData_stage_execution.xlsx"
        copyfile(source, dest)    #viaData_stage_execution.xlsx file created which is a copy of iaData_stage.xlsx
        'genericOb=generic(dest)'
    generic.getdestination(exePath) 
    
    if(env=="prod"):
        source=".\\Test_data\\viaData_stage.xlsx"
        dest=exePath+"viaData_prod_execution.xlsx"
        copyfile(source, dest)
        'genericOb=generic(dest)'
    generic.getdestination(exePath)   
    
    
  
def teardown_module(module): 
    
    TS=generic.getCurrentTime()
    #Pytest creates report file in location: reportSrc by default. 
    reportSrc=".\\Report.html"
    
    reportDest=".\\Report\\"+"HTMLReport_"+TS+".html"
    copyfile(reportSrc,reportDest) #Report file copied from reportSrc to reportDest
    

class Test_yatra(object):
    
    def setup_method(self, method):
        pass
    
    def teardown_method(self, method):
        pass
    
    
    @pytest.mark.signIn_textBoxTest  #Marker to be used in conftest file to distinguish from other tests
    #Marker defined to Skip the test conditionlly
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "001_signIn_textBoxTest")=='No', reason="functionality is not ready")
    def test_signIn(self,driverLaunch):
        sheet0="via_driver"
        sheet1='signInPage'
        TCName='001_signIn_textBoxTest'
        
        try:
            logger=generic.logCreation()
            driverLaunch.get("https://www.via.com")
            test_homePage.signIn_001(driverLaunch, logger, TCName, sheet1, "emailid", "password")
            logger.info('User signed in successfully')
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Pass")
        except Exception as e:
            
            logger.error("User unable to sign in with error: ", e)
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Fail")
            raise e 
    
    
    @pytest.mark.flightcheck
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "002_flightSearch")=='No', reason="functionality is not ready")    
    def test_flightcheck(self, driverLaunch):
        TCName='002_flightSearch'
        sheet0='via_driver'
        sheet1='flightPg'

        
        try:
            logger=generic.logCreation()
            driverLaunch.get("https://in.via.com/")
            test_homePage.flight_002(driverLaunch, logger, TCName, sheet1, "flight_source", "flight_destination")
            logger.info('Flight search is successful')   
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Pass")
            
        except Exception as e:
            print ("exception raised is: ", e)
            logger.error("light search failed, error raised is: ", e)
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Fail") 
              
    
    @pytest.mark.help_iframeTest
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "003_help_iframeTest")=='No', reason="functionality is not ready")
    def test_help(self, driverLaunch):
        sheet0='via_driver'
        TCName="003_help_iframeTest"
        
        try:
            logger=generic.logCreation()
            driverLaunch.get("https://in.via.com/")
            test_homePage.help_003(driverLaunch, logger, TCName)
            'print ("Test case- 003_help_iframeTest is successful")'
            logger.info("Test case- 003_help_iframeTest is successful")
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Pass")
            
        except Exception as e:
            logger.error("Test case - 003_help_iframeTest is failed, exception raises is: ", e)
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Fail")
            raise e
    
    
    @pytest.mark.forex_hoverTest
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "004_forex_hover_multipleWindowTest")=='No', reason="functionality is not ready")
    def test_forex(self, driverLaunch):
        sheet0='via_driver'
        TCName="004_forex_hover_multipleWindowTest"
        try:
            logger=generic.logCreation()
            driverLaunch.get("https://in.via.com/")
            test_homePage.forex_004(driverLaunch, TCName, logger)
            logger.info("004_forex_hoverTest is successful")    
        
        except Exception as e:
            logger.error("004_forex_hoverTest failed, error found is :", e)
            raise e
    
    
    @pytest.mark.gmail_AutoIT_AttachmentTest
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "005_gmail_AutoIT_AttachmentTest")=='No', reason="functionality not ready")
    def test_mail(self, driverLaunch):
        
        sheet1='gmail_home'
        sheet0='via_driver'
        TCName="005_gmail_AutoIT_AttachmentTest"
        
        
        
        try:
            logger=generic.logCreation()
            driverLaunch.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            gmailtestclass.gmail_005(driverLaunch, logger, sheet1, TCName)
            logger.info("TC- 005_gmail_AutoIT_AttachmentTest is successful") 
            
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Pass")
            
        except Exception as e:
            
            logger.error("exception raised is: ", e)  
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Fail")
            
            raise e  
    
   
      
    @pytest.mark.policies_scrollPageTest
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "006_policies_scrollPageTest")=='No', reason="functionality not ready")   
    def test_policies(self, driverLaunch):
        sheet0='via_driver'
        TCName="006_policies_scrollPageTest"
        
        try:
            logger=generic.logCreation()
            driverLaunch.get("https://in.via.com/")
            
            time.sleep(10)
            test_homePage.policies_006(driverLaunch, logger, TCName) 
            logger.info("TC- 006_policies_scrollPageTest is successful") 
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Pass")
         
        except Exception as e:
            
            logger.error("exception raised is: ", e)  
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Fail")
            
            raise e 
```
