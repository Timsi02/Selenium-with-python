import pytest
import xlrd
import logbook
from selenium import webdriver
from viaReservation.homePage import test_homePage
from viaReservation.test_gmail_home import gmailtestclass
from viaReservation.genericFunctions import generic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from shutil import copyfile
import time

dest='test'
def setup_module(module):
    #Fetch the current time from the method - getCurrentTime() form the module - viaReservation.genericFunctions
    TS=generic.getCurrentTime()
    #To make a folder with timestramp
    exePath=".\\Execution_status\\"+"Execution_"+TS+"\\"
    
    y=os.mkdir(exePath)
    print ("directory created")
    
    #There can be several testing environments 
    env="stage"
    'env="support"'
    'env="prod"'
    if(env=="stage"):
        source=".\\Test_data\\viaData_stage.xlsx"
        dest=exePath+"viaData_stage_execution.xlsx"
        copyfile(source, dest)    #viaData_stage_execution.xlsx file created which is a copy of viaData_stage.xlsx
     
    if(env=="support"):
        source=".\\Test_data\\viaData_stage.xlsx"
        dest=exePath+"viaData_support_execution.xlsx"
        copyfile(source, dest)    #viaData_support_execution.xlsx file created which is a copy of viaData_support.xlsx   
        
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
    #Pytest creates report file in location: reportSrc by default. So, to move the report to a specific folder, follow the steps below
    reportSrc=".\\Report.html" #default location
    
    reportDest=".\\Report\\"+"HTMLReport_"+TS+".html" #desired location
    copyfile(reportSrc,reportDest) #Report file copied from reportSrc to reportDest(From default to desired)
    

class Test_via(object):
    
    def setup_method(self, method):
        pass
    
    def teardown_method(self, method):
        pass
    
    #Marker to be used in conftest file to distinguish from other tests
    @pytest.mark.signIn_textBoxTest  
    #Marker defined to Skip the test conditionally
    #Refer the method generic.checkExecutionFlag(sheet0, TCName):
    #If the execution flag is set to 'No' in the excel corresponding to the test case "001_signIn_textBoxTest", this test will be skipped from the execution
    @pytest.mark.skipif(generic.checkExecutionFlag('via_driver', "001_signIn_textBoxTest")=='No', reason="functionality is not ready")
    def test_signIn(self,driverLaunch):
        sheet0="via_driver"
        sheet1='signInPage'
        TCName='001_signIn_textBoxTest'
        
        try:
            #Refer the method generic.logCreation(), used to create log files
            logger=generic.logCreation()
            driverLaunch.get("https://www.via.com")
            #Page object model implementation. Flow directed to test_homePage.signIn_001(driver, logger, TCName, sheet1, emailid, password) in the module homePage.py
            test_homePage.signIn_001(driverLaunch, logger, TCName, sheet1, "emailid", "password")
            #Logging the information
            logger.info('User signed in successfully')
            #Refer the method generic.setValueToExcel(sheet0, TCName , columnName, cellValue): 
            generic.setValueToExcel(sheet0, TCName, "Execution_Result", "Pass")
        except Exception as e:
            
            logger.error("User unable to sign in with error: ", e)
            #Refer the method generic.setValueToExcel(sheet0, TCName , columnName, cellValue): 
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
