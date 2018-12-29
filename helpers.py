from webdriver import driver
from cookies import readCookies, writeCookies
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import getpass

def enterTextId(id, text):
    elem = driver.find_element_by_id(id)
    elem.clear()
    elem.send_keys(text)

def pressEnterId(id):
    elem = driver.find_element_by_id(id)
    elem.send_keys(Keys.RETURN)

def enterLogin(isEmpl):
    if isEmpl:
        navTo('https://weblogin.umich.edu/?cosign-hcmprod.dsc&https://hcmprod.dsc.umich.edu/services/employee/')
    else:
        navTo('https://weblogin.umich.edu/?cosign-csprod.dsc&https://csprod.dsc.umich.edu/services/student/')

    if "Weblogin" in driver.title:
        try:
            usr = getpass('Enter username: ')
            password = getpass('Enter password: ')
            enterTextId('login', usr)
            enterTextId('password', password)
            pressEnterId('password')
        except:
            print("Oops, something went wrong...")
    wait = WebDriverWait(driver, 60)
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'PT_HOME')))
    except:
        driver.quit()

# This functions doesn't work... :(
# def waitId(id):
#     wait = WebDriverWait(driver, 60)
#     try:
#         wait.until(EC.presence_of_element_located((By.ID, id)))
#     finally:
#         driver.quit()

# This functions doesn't work... :(
# def waitTitle(str):
#     wait = WebDriverWait(driver, 60)
#     try:
#         wait.until(not EC.title_is(str))
#     finally:
#         driver.quit()

def navTo(url):
    driver.get(url)

def close():
    driver.close()

def quitSess():
    writeCookies()
    driver.close()
    driver.quit()
    exit()

def handleLogin(func, args=None, isEmpl=False):
    if args:
        func(args)
    else:
        func()
    if 'Weblogin' in driver.title:
        enterLogin(isEmpl)
        if args:
            func(args)
        else:
            func()
    
