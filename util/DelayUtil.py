from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitWrapper:
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, *args, **kwargs):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(args[0])
    )