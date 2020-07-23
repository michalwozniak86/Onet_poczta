import unittest
from selenium import webdriver
import time
from PageObjectModel.Pages.homePage import HomePage

class CreatingAccountTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testLoginValid(self):
        driver = self.driver

        driver.get("https://www.onet.pl")
        driver.implicitly_wait(30)

        homepage = HomePage(driver)
        homepage.click_cookies()
        homepage.click_mail()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")

if __name__=='__main__':
    unittest.main(verbosity=2)