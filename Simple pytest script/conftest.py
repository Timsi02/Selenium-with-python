#conftest.py
```python
import pytest
from lxml import html
import sys

#Fixture functions are registered by marking them with @pytest.fixture
@pytest.fixture
def checkFixture():
    return "this"
    
#Hook function to add information in environment section of html report
def pytest_configure(config):
    config._metadata['Environment'] = 'Stage'
    config._metadata['Round'] = '1'
    
#Hook function to add information in summary sec of html report
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.__fix_docstring("The project deals with--- Info about the project")]) 
    
#Hook function to add command line option
#parser.addoption - to add command line options
#parser.addini - to add ini file values
#Options can later be acced through config object
def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )
def pytest_collection_modifyitems(config, items):
    #to retrive the value of command line option  
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")  
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)  
            
#Hook function to add text and image in results section
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.text('to test extra'))
        extra.append(pytest_html.extras.image('D:\\test.png'))
        extra.append(pytest_html.extras.url('http://www.google.com'))
        
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra 
        
#Hook function to speedup tests
def pytest_load_initial_conftests(args):
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing

        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args 

##Hook function to add extra info in pytest run      
def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        return ["INFO1", "INFO2", "INFO3"]               
        
```
