# Simple pytest script

pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories
```python
#test_pycheck.py
#class name must start with 'Test'
class TestClass(object):
    #method names must start with 'test'
    #methods can receive fixture objects by naming them as an input argument.  For each argument name, a fixture function with that name provides the fixture object 
    def test_one(self, checkFixture):
        x = checkFixture   #this contains the returned value from checkFixture function, i.e. 'this'
        assert 'h' in x
        
    def testtwo(self):
        x = "hello"
        assert hasattr(x, 'check')
```
