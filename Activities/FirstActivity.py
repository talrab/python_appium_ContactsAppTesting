from Activities.BaseActivity import BaseActivity
from Activities.CreateNewContactActivity import CreateNewContactActivity

# placing all the locators needed in this page/activity in one place for easy modifications when needed
locators = {
    'new_contact'       : 'id==create_contact_button',
    'sign_in_to_account': 'id==add_account_button',
    'import_contacts'   : 'id==import_contacts_button',
    'contacts_message'  : 'id==com.android.contacts:id/message'
}



class FirstActivity(BaseActivity):
    def __init__(self, driver):
        super().__init__(driver)

    def create_a_new_contact(self):
        # return self.find_element_by_locator(locators['new_contact'])
        self.find_element_by_locator(locators['new_contact']).click()
        return CreateNewContactActivity(self.driver)

    def sign_in_to_an_account(self):
        return self.find_element_by_locator(locators['sign_in_to_account'])

    def import_contacts(self):
        return self.find_element_by_locator(locators['import_contacts'])

    def isEmpty(self):
        return self.find_element_by_locator(locators['contacts_message']).text == 'No contacts'


