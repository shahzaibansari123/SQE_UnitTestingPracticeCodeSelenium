import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

class demoQA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://demoqa.com/text-box")
        cls.driver.maximize_window()

    def test_froms(self):
        self.driver.find_element(By.ID, "userName").clear()
        self.driver.find_element(By.ID, "userName").send_keys("Shahzaib")
        self.driver.find_element(By.ID, "userEmail").clear()
        self.driver.find_element(By.ID, "userEmail").send_keys("ansarishahzaib567@gmail.com")
        time.sleep(5)

    def test_address(self):
        self.driver.find_element(By.XPATH, "//*[@id='currentAddress']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys("abc address")
        self.submit = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click()", self.submit)

        self.driver.switch_to.alert.accept()
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()