import time
import unittest
import os

from appium import webdriver

from Activities.FirstActivity import FirstActivity
from Activities.CreateNewContactActivity import CreateNewContactActivity
from Activities.AllContactsActivity import AllContactActivity

class contactsTests(unittest.TestCase):

    "Class to run tests against the calculator Free app"
    contact_name = "Test Name"

    def setUp(self):
        "Setup for the test"
        #os.system("adb shell pm clear com.android.contacts")  --> didn't work...
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(1)  # added this sleep in order to let the activity full load


    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    # each function which starts with a 'test' and belongs to a
    # class which derives from unittest.TestCase is regarded as a 'test case'
    def test_create_a_new_contact(self):

        "Test the create a new contact flow"
        firstActivity = FirstActivity(self.driver)
        createNewContactActivity = firstActivity.create_a_new_contact()
        createNewContactActivity.name().click()
        createNewContactActivity.name().send_keys(self.contact_name + '\n')
        createNewContactActivity.phone().click()
        createNewContactActivity.phone().send_keys("555555")
        # closing the android keyboard so the email element will be visible
        self.driver.hide_keyboard()
        createNewContactActivity.email().click()
        createNewContactActivity.email().send_keys("test_name@test.com")
        contactDetailsActivity = createNewContactActivity.save()
        self.assertEqual(self.contact_name, contactDetailsActivity.title().text)

    def test_delete_contact(self):

        "Test the delete contact flow"
        allContactsActivity = AllContactActivity(self.driver)
        allContactsActivity.search().click()
        allContactsActivity.searchBox().send_keys("Test")
        contactDetailsActivity = allContactsActivity.clickFoundContact()
        self.assertEqual(self.contact_name, contactDetailsActivity.title().text)
        contactDetailsActivity.moreOptions().click()
        contactDetailsActivity.delete()
        allContactsActivity = contactDetailsActivity.confirm_delete()
        print("++++++++++++++++++++++++++++")
        print(allContactsActivity.isEmpty())
        print("++++++++++++++++++++++++++++")
        self.assertTrue(allContactsActivity.isEmpty())



        # ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(contactsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)