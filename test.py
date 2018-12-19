from webdriver import driver
from cookies import readCookies, writeCookies
from helpers import handleLogin, quitSess, enterLogin
from pages import Home, Student, StudentCenter, EmployeeSelfService
from helpers import navTo

Home()

readCookies()

print(driver.title)

Student()

print(driver.title)

StudentCenter()

print(driver.title)

quitSess()