import time

from TestCases.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class Test_testApp(BaseClass):

    def test_women(self):
        self.homePage = HomePage(self.driver)
        self.women("//a[@role='menuitem']//span[contains(text(),'Women')]")
        time.sleep(25)

    def test_tops(self):
        self.homePage = HomePage(self.driver)
        self.tops("//a[@id='ui-id-9']").click('Tops')
        time.sleep(18)

    def test_jacket(self):
        self.homePage = HomePage(self.driver)
        self.jacket("//a[@id='ui-id-11']//span[contains(text(),'Jackets')]").click('Jackets')
        time.sleep(26)