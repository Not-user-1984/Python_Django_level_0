from selenium import webdriver
import unittest

driver = webdriver.Firefox (executable_path='/Users/diplug/Python _Projetc/Selenium_Python/firefoxdriver/geckodriver')


class NewVizitorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox (executable_path='/Users/diplug/Python _Projetc/Selenium_Python/firefoxdriver/geckodriver')

    def tearDown(self):
        self.driver.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')

        self.assertIn('Django',self.driver.title)
        self.fail('закочить тест')
if __name__ == '__main__':
    unittest.main(warnings='ignore')

