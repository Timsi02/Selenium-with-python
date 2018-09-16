You can start to work on pytest Once you have installed pytest using the following command in your command line:
`pip install -U pytest`

[Create a simple test case in selenium using pytest](https://github.com/Timsi02/Selenium-with-python/blob/master/Simple%20pytest%20script/test_pycheck.py) with the help of [conftest.py](https://github.com/Timsi02/Selenium-with-python/blob/master/Simple%20pytest%20script/conftest.py)


## Run test cases:

pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories

From Eclipse:
 - Run as -> Python unit-test

From command line:
 - Pytest supports several ways to run and select tests from the command-line.
 Run tests in a module:  `pytest test_mod.py`
Run tests in a directory: `pytest testing/`
 - You can invoke testing through the Python interpreter from the command line:
        `python -m pytest [...]`
    This is almost equivalent to invoking the command line script pytest [...] directly, except that calling via python will also add the current directory to sys.path.
 
## Fixture Functions:

 - fixtures are defined for static data used by tests. This could be data as well as helpers of modules which will be passed to all tests.This data is accessed by all tests in the suite unless specified. 
 - Fixture functions provide a baseline to repeatedly execute the tests.
 - Fixture functions are registered by marking them with @pytest.fixture.
 - Test functions can receive fixture objects by naming them as an input argument. For each argument name, a fixture function with that name provides the fixture object. For e.g.

```python
@pytest.fixture
def checkFixture():
    return "this"

def test_one(self, checkFixture):
#checkFixture argument contains the returned value from checkFixture function, i.e. 'this'
x = checkFixture   
assert 'h' in x   
 ```   



`Conftest.py`

This plugin contain directory-specific hooks and fixtures(Explained below). 
Session and test running activities will invoke all hooks defined in conftest.py files closer to the root of the filesystem.
Example: Assume the following layout and content of files:
```python
a/conftest.py:
    def pytest_runtest_setup(item):
        # called for running each test in 'a' directory
        print ("setting up", item)

a/test_sub.py:
    def test_sub():
        pass

test_flat.py:
    def test_flat():
        pass
```        
When you run the tests:

py.test test_flat.py - >  will not show "setting up"
py.test a/test_sub.py - >  will show "setting up"
        

Some uses of conftest plugin:
- Fixture: If during implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file. You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins

- Hooks: Pytest implements all aspects of configuration, collection, running and reporting by calling well specified hooks. Hook functions are implemented by 'pytest_' prefix. Session and test running activities will invoke all hooks defined in conftest.py files closer to the root of the filesystem.
