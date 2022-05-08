from .base_page import BasePage
from .locators import EmailPageLocators


class EmailPage(BasePage):
    def find_message_from_sender(self, sender):
        self.browser.find_element(*EmailPageLocators.SEARCH_INPUT).send_keys(sender)
        self.browser.find_element(*EmailPageLocators.BUTTON_SEARCH).click()


    def select_and_delete_all_messages(self):
        checkboxes = self.browser.find_elements(*EmailPageLocators.ALL_CHECKBOX)
        for checkbox in checkboxes:
            checkbox.click()
        self.browser.find_element(*EmailPageLocators.BUTTON_DELETE).click()





