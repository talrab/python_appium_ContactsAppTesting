from Activities.BaseActivity import BaseActivity


locators = {
    'search'            : 'id==com.android.contacts:id/menu_search',
    'searchBox'         : 'id==com.android.contacts:id/search_view',
    'foundContact'      : 'id==com.android.contacts:id/cliv_name_textview',
    'contacts_message'  : 'id==com.android.contacts:id/totalContactsText'
}


class AllContactActivity(BaseActivity):
    def __init__(self,driver):
        super().__init__(driver)

    def search(self):
        return self.find_element_by_locator(locators['search'])

    def searchBox(self):
        return self.find_element_by_locator(locators['searchBox'])

    def clickFoundContact(self):
        from Activities.ContactDetailsActivity import ContactDetailsActivity
        self.find_element_by_locator(locators['foundContact']).click()
        return ContactDetailsActivity(self.driver)

    def isEmpty(self):
        return self.find_element_by_locator(locators['contacts_message']).text == 'No contacts'


