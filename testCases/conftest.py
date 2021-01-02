from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path='C:\\Users\\Ayushree\\PycharmProjects\\chromedriver.exe')
        driver.maximize_window()
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path='C:\\Users\\Ayushree\\PycharmProjects\\geckodriver.exe')
        driver.maximize_window()
    else:
        # driver=webdriver.ie()
        driver = webdriver.Chrome(executable_path='C:\\Users\\Ayushree\\PycharmProjects\\chromedriver.exe')

    return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


###############Pytest HTML Report###########################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ayushree'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

