# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class test_add_project(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_login(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/")
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("administrator")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("root")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def test_add_project(self):
        wd = self.wd
        #wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("luhlhlhj")
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_xpath("//select[@name='status']")).select_by_visible_text("release")
        wd.find_element_by_xpath("//td[2]/select/option[2]").click()
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_xpath("//select[@name='view_state']")).select_by_visible_text("private")
        wd.find_element_by_xpath("//tr[5]/td[2]/select/option[2]").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("kfkghvh")
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

