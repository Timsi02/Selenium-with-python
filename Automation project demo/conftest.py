import pytest
from selenium import webdriver
from yatraReservation.test_genericFunctions import generic

@pytest.fixture
def driverLaunch():
    '''driver=webdriver.Firefox(executable_path=r'C:\\Users\\ACER\\Desktop\\Selenium\\geckodriver-v0.19.1-win64\\geckodriver.exe')'''
    driver=webdriver.Firefox(executable_path=r'.\\Resource\\geckodriver.exe')
    return driver

@pytest.fixture
def logger():
    logger=generic.logCreation()
    return logger
    
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    print("type is: ",type(item))
    print ("item is: ", item)
    pytest_html = item.config.pluginmanager.getplugin('html')
    print ("pytest_html is: ", pytest_html)
    outcome = yield
    print ("outcome is: ", outcome)
    report = outcome.get_result()
    print ("report is :", report)
    extra = getattr(report, 'extra', [])
    print ("extra is: ", extra)
    
    if report.when == 'call' and "signIn_textBoxTest" in item.keywords:
        print ("in if condition")
        
        
        extra.append(pytest_html.extras.image(".\\Result\\"+"'001_signIn_textBoxTest'"+".png"))
        
        extra.append(pytest_html.extras.text("signIn_textBoxTest "))
        extra.append(pytest_html.extras.url('http://www.via.com'))
        extra.append(pytest_html.extras.html('<p>signIn_textBoxTest </p>'))
    report.extra = extra
    print ("report.extra is: report.extra")
    
    if report.when == 'call' and "help_iframeTest" in item.keywords:
        print ("in if condition")
        # always add url to report
        r'''
        extra.append(pytest_html.extras.image(r'C:\Users\ACER\Desktop\Python scripts\pytesthome1.png'))
        extra.append(pytest_html.extras.image(".\\Result\\003_help_iframeTest.png"))
        '''
        extra.append(pytest_html.extras.text("check_text"))
        extra.append(pytest_html.extras.url('http://www.google.com'))
        extra.append(pytest_html.extras.html('<p>some html</p>'))
        
    if report.when == 'call' and "forex_hoverTest" in item.keywords:
        
        extra.append(pytest_html.extras.text("forex_hoverTest"))
        extra.append(pytest_html.extras.url('http://www.google.com'))
        extra.append(pytest_html.extras.html('<p>forex_hoverTes- html</p>'))    
        
        
    if report.when == 'call' and "gmail_AutoIT_AttachmentTest" in item.keywords:
        
        extra.append(pytest_html.extras.text("gmail_AutoIT_AttachmentTest"))
        extra.append(pytest_html.extras.url('http://www.google.com'))
        extra.append(pytest_html.extras.html('<p>attachment test</p>')) 
        
    if report.when == 'call' and "policies_scrollPageTest" in item.keywords:
        
        extra.append(pytest_html.extras.text("policies_scrollPageTest"))
        extra.append(pytest_html.extras.url('http://www.google.com'))
        extra.append(pytest_html.extras.html('<p>attachment test</p>')) 
        
    if report.when == 'call' and "flightcheck" in item.keywords:
        
        extra.append(pytest_html.extras.text("policies_scrollPageTest"))
        extra.append(pytest_html.extras.url('http://www.via.com'))
        extra.append(pytest_html.extras.html('<p>flightcheck</p>'))         
            
        print ("extra after append is: ", extra)
        xfail = hasattr(report, 'wasxfail')
        print ("xfail is: ", xfail)
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
        print ("report.extra is: report.extra")
