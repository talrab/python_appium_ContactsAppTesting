
class BaseActivity:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_locator(self, locator):
        locator_type, locator_name = locator.split("==")
        return self.driver.find_element(locator_type, locator_name)

    def find_elements_by_locator(self, locator):
        locator_type, locator_name = locator.split("==")
        return self.driver.find_elements(locator_type, locator_name)