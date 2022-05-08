import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    print("\nstart chrome browser for test..")
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--user-data-dir=C:\\Users\\Anastasiia\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument('--profile-directory=Default')
    browser = webdriver.Chrome(options=options)
    browser.execute_script('''window.open();''')
    browser.switch_to.window(browser.window_handles[-1])

    yield browser
    print("\nquit browser..")
    browser.quit()


