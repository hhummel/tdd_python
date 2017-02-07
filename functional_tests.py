from selenium import webdriver
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
        self.fail("Finish the test!")

        #She is invited to enter a to-do item straight away

        #She types "Buy peacock feathers" into text box (for fly fishing)

        #When she hits "Enter", the page updates and "1: Buy peacock feathers is an item on to-do list

        #There's a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"

        #The page updates, and shows both items on her list

        #She sees site has gnerated a unique URL for her list

        #She visits the URL and sees her list is present

        #She quits the site

if __name__ == '__main__':
    unittest.main(warnings='ignore')


