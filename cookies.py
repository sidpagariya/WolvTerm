import pickle, getpass
from webdriver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def readCookies():
    try:
        with open('cookies.pkl', 'rb') as j:
            cookies = pickle.load(j)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print("Using cookies.")
    except Exception as e:
        print(str(e))
        print("Did not find cookies.")
        from helpers import enterLogin, navTo, handleLogin
        print(driver.title)
        print("Getting cookies now...")
        from pages import Student
        Student()
        #print(driver.title)
    writeCookies()
    from pages import Home
    Home()
        

def writeCookies():
    #pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    with open('cookies.pkl', 'wb') as j_out:
        pickle.dump(driver.get_cookies(), j_out)