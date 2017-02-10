from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #She goes to check out home page
        self.browser.get('http://localhost:8000')

        #She notices page title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #She types "Buy peacock feathers" into text box (for fly fishing)
        inputbox.send_keys("Buy peacock feathers")

        #When she hits "Enter", the page updates and "1: Buy peacock feathers is an item on to-do list
        inputbox.send_keys(Keys.ENTER)

        #import time
        #time.sleep(10)

        table = self.browser.find_element_by_id("id_list_table")
        rows = self.browser.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows), "New to-do item did not appear in table")

        #There's a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        

        #The page updates, and shows both items on her list
        table = self.browser.find_element_by_id("id_list_table")
        rows = self.browser.find_elements_by_tag_name("tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows], "First to-do item did not appear in table")
        self.assertIn("2: Use peacock feathers to tie a fly", [row.text for row in rows], "Second to-do item did not appear in table")
        

        #She sees site has generated a unique URL for her list
        self.fail('Finish the test!')

        #She visits the URL and sees her list is present

        #She quits the site

if __name__ == '__main__':
    unittest.main(warnings='ignore')


