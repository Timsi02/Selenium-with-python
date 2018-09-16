from selenium import webdriver
import time
import win32com.client

driver=webdriver.Firefox(executable_path=r'C:\\Users\\ACER\\Desktop\\Selenium\\geckodriver-v0.19.1-win64\\geckodriver.exe')
driver.maximize_window()
driver.get('https://www.engprod-charter.net/')

shell = win32com.client.Dispatch("WScript.Shell")   
shell.Sendkeys("username")  
time.sleep(2)
shell.Sendkeys("{TAB}")
time.sleep(2)
shell.Sendkeys("password") 
time.sleep(2)
shell.Sendkeys("{ENTER}")
time.sleep(2)
