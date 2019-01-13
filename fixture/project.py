from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") and len(wd.find_element_by_link_text('Manage')) > 0):
            wd.find_element_by_link_text('Manage').click()

    def open_manage_project_page(self):
        wd = self.app.wd
        self.open_manage_page()
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_element_by_xpath("//input[@value='Create New Project']")) > 0):
            wd.find_element_by_link_text('Manage Projects').click()

    def create(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_manage_project_page()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.state)
        if not project.enabled:
            wd.find_element_by_name("inherit_global").click()
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_project_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % project_id).click()

    def delete_project_by_id(self, project_id):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_id(project_id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        #self.open_manage_project_page()
        self.project_cache = None

    project_cache = None