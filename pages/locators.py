from selenium.webdriver.common.by import By

class LinkLocators():
    EMAIL_LINK = 'https://mail.google.com/mail/u/0/h/1vy9nmddowzh/?&'

class EmailPageLocators():
    SEARCH_INPUT = (By.CSS_SELECTOR, '[title="Найти"]')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '[value="Поиск почты"]')
    ALL_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    BUTTON_DELETE = (By.CSS_SELECTOR, '[value="Удалить"]')
    CONTENT = (By.XPATH, '/html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody')


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '/html/body/header/div/div/div/a[2]')



