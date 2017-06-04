from Activities.BaseActivity import BaseActivity
from Activities.ContactDetailsActivity import ContactDetailsActivity

# placing all the locators needed in this page/activity in one place for easy modifications when needed
locators = {
    'name' : 'xpath==//android.widget.EditText[@text="Name"]',
    'phone': 'xpath==//android.widget.EditText[@text="Phone"]',
    'email': 'xpath==//android.widget.EditText[@text="Email"]',
    'save' : 'id==com.android.contacts:id/menu_save',
}



class CreateNewContactActivity(BaseActivity):
    def __init__(self, driver):
        super().__init__(driver)

    def name(self):
        return self.find_element_by_locator(locators['name'])

    def phone(self):
        return self.find_element_by_locator(locators['phone'])

    def email(self):
        return self.find_element_by_locator(locators['email'])

    def save(self):
        self.find_element_by_locator(locators['save']).click()
        return ContactDetailsActivity(self.driver)



