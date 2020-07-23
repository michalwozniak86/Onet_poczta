class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.cookies_accept_xpath = "//*[@id='pageMainContainer']/div[4]/div[1]/div[2]/div/div[3]/button[2]"
        self.mail_click_xpath = "/html/body/header/div[1]/div[2]/nav/ul/li[6]/a"

    def click_cookies(self):
        self.driver.find_element_by_xpath(self.cookies_accept_xpath).click()

    def click_mail(self):
        self.driver.find_element_by_xpath(self.mail_click_xpath).click()