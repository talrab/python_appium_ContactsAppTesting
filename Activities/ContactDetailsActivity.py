from Activities.BaseActivity import BaseActivity
from Activities.AllContactsActivity import AllContactActivity
import time

# placing all the locators needed in this page/activity in one place for easy modifications when needed
locators = {
    'title'             : 'id==com.android.contacts:id/large_title',
    'moreOptions'       : 'xpath==//android.widget.ImageButton[@content-desc="More options"]',
    'moreOptions_delete': 'xpath==//android.widget.TextView[@text="Delete"]',
    'confirm_ok'        : 'xpath==//android.widget.Button[@text="OK"]',

}



class ContactDetailsActivity(BaseActivity):
    def __init__(self, driver):
        super().__init__(driver)

    def title(self):
        return self.find_element_by_locator(locators['title'])

    def moreOptions(self):
        return self.find_element_by_locator(locators['moreOptions'])

    def delete(self):
        time.sleep(1)
        self.find_element_by_locator(locators['moreOptions_delete']).click()

    def confirm_delete(self):
        from Activities.FirstActivity import FirstActivity
        time.sleep(1)
        self.find_element_by_locator(locators['confirm_ok']).click()
        #return FirstActivity(self.driver)
        return AllContactActivity(self.driver)


