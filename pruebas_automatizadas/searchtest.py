import unittest
from pyunitreport import HTMLTestRunner
import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class SearchTests(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        chrome = Service(r"C:\Users\olvis\OneDrive\Escritorio\Prueba-automatizada-main\chromedriver.exe")

        self.driver = webdriver.Chrome(service= chrome)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_tee(self):
        self.driver.save_screenshot("capturas/Portada.png")
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('tee')
        self.driver.save_screenshot("capturas/buscar_camisa.png")
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.send_keys('salt shaker')
        self.driver.save_screenshot("capturas/buscar_salero.png")
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//div[@class = "product-info"]/h2[@class="product-name"]/a')                                       
        self.assertEqual(1, len(products))

    def tearDown(self) -> None:
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)
