import unittest
from selenium import webdriver

class IdentifyElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://demo-m2.bird.eu/")

    def test_identify_element(self):
        self.find_element = self.driver.find_element_by_id('switcher-language')
        self.assertTrue(self.find_element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
