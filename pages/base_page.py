from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Find a single web element"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        """Find a clickable web element"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator):
        """Find a visible web element"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def enter_text(self, locator, text):
        """Enter text into an input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        """Click on a web element"""
        element = self.find_clickable_element(locator)
        element.click()

    def get_text(self, locator):
        """Get text from a web element"""
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        """Check if an element is present"""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False