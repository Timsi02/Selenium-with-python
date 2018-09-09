# home page having class as test_signInClass and method as signInprocess:

```python
class test_signInClass:
    @staticmethod
    def signInprocess(driver):
        
        email_locator = (By.XPATH, "//*[@id='loginIdText']")
        password_locator= (By.XPATH, "//*[@id='passwordText']")
        signInBtn_locator=(By.XPATH, "//*[@id='loginValidate']")
           
           emailBox=driver.find_element(*email_locator)
           emailBox.send_keys("emailid@abc.com")  
           
            passwordBox=driver.find_element(*password_locator)
            passwordBox.send_keys("password")
            
            driver.implicitly_wait(20)
            driver.find_element(*signInBtn_locator).click()

```
