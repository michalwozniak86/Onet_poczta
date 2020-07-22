#Testing create new account on Poczta Onet without accepting statute

import unittest
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

Name_Surname = "Adam Kowalski"
login = "add.am.kowalsky"
password = "1QaZ666wSxMh"
d_birth = "6"
m_birth = "5"
y_birth = "1976"

class Registration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        sleep(1)
        self.driver.maximize_window()
        self.driver.get("https://www.onet.pl/poczta")
        self.driver.implicitly_wait(45)

    def test(self):
        driver = self.driver
        id = driver.find_element_by_id
        xpath = driver.find_element_by_xpath
        cls = driver.find_element_by_class_name
        name = driver.find_element_by_name

        sleep(5)

        #accept coockies
        xpath('//*[@id="pageMainContainer"]/div[4]/div[1]/div[2]/div/div[3]/button[2]/span').click()

        #wybieramy zakladanie konta
        cls("createAccount").click()

        #wpisujemy imie i nazwisko
        id("f_nameSurname").send_keys(Name_Surname)

        #wpisujemy login
        id("login_user").click()
        sleep(1)
        id("login_user").clear()
        id("login_user").send_keys(login)

        #klikamy sprawdz
        name("checkLogin").click()

        sleep(1)

        #wyberamy z listy
        element = xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div[3]/div[1]/fieldset/div/div/ul/li[2]/div/ul/li/div/div[3]/ul/li[1]')
        hover = ActionChains(driver).move_to_element(element)
        hover.click().perform()
        sleep(1)


        #wybranie dnia urodzin
        xpath('//*[@id="f_birthDate_day"]').click()
        xpath('//*[@id="f_birthDate_day"]').send_keys(d_birth)
        xpath('//*[@id="f_birthDate_day"]').click()
        sleep(1)

        #wybranie miesiaca urodzin
        month = Select(name("birthDate[month]"))
        month.select_by_value(m_birth)

        #wybieranie roku urodzin
        year = Select(name("birthDate[year]"))
        year.select_by_value(y_birth)

        #wybieramy plec
        id("f_gender_M").click()

        #wpisujemy haslo
        id("f_password").send_keys(password)

        #potwierdzenie hasla
        xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div[3]/fieldset[1]/div/div/ul/li[2]/div[1]/input')\
        .send_keys(password)

        #klikamy zaloz konto
        id("registerEmailFormSubmitButton").click()

        sleep(5)
        pass

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
