import inspect
import logging
from typing import List

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def women(self, xpath):
        women = ActionChains(self.driver).move_to_element(xpath)
        return women

    def tops(self, xpath):
        tops = ActionChains(self.driver).move_to_element(xpath)

        return tops

    def jacket(self, xpath):
        jacket =ActionChains.click(self.jacket(xpath))
        return jacket

