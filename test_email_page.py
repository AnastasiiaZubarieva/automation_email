import pytest
from .pages.email_page import EmailPage
from .pages.locators import LinkLocators, EmailPageLocators



senders = [
    ("Книгарня 'Є'"),
    ('Ivan at Notion'),
    ('Света из Contented'),
    ('Atlassian'),
    ('Contented')
]

@pytest.mark.parametrize('sender', senders)
def test_delete_all_messages(browser, sender):
    page = EmailPage(browser, LinkLocators.EMAIL_LINK)
    page.open()
    page.find_message_from_sender(sender)
    page.select_and_delete_all_messages()
    page.is_not_element_present(*EmailPageLocators.CONTENT)






