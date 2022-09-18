from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser) #команда raise - выполение кода в этом месте будет аварийно прервано
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def is_element_present(self, how, what):
        try:self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def destroy(self):
        self.wd.quit()
        #метод разрушающий фикстуру (заркрывает браузер)
