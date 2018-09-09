# Test case:

```python
import pytest
from viaReservation.homePage import test_signInClass
from selenium import webdriver
class Test_via(object):

    def test_signIn(self,driverLaunch):
            driver=webdriver.Firefox(executable_path=r'.\\Resource\\geckodriver.exe')
            driver.get("https://www.via.com")
            #calls the method signIn_001 in class test_signInClass
            test_signInClass.signInprocess(driverLaunch)
            driver.quit()
```
