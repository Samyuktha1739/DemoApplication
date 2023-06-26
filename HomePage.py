from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def women(self, xpath):
        return self.driver.find_element(By.ID, xpath)

    def tops(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def jacket(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)