from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])
        

    def test_can_start_a_list_and_retrieve_it_later(self):
        #She goes to check out home page
        self.browser.get(self.live_server_url)

        #She notices page title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #She types "Buy peacock feathers" into text box (for fly fishing)
        inputbox.send_keys("Buy peacock feathers")

        #When she hits "Enter", she is sent to a new URL
        #and now the page lists "1: Buy peacock feathers is an item on to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+', "edith_list_url: " + edith_list_url)        
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        #There's a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        #The page updates, and shows both items on her list
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        #A new user Francis visits and does not see Edith's list
        
        ##We use a new browser session to make sure no information of Edith's is visible to Francis
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make fly', page_text)

        #Francis starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        #Francis gets her own URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')        
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        #Satified, they both go back to sleep


