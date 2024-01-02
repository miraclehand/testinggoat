from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
                "You can't have an empty list item"
        ))

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
                "You can't have an empty list item"
        ))

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

        #self.fail('finish this test!')
