from webdriver import driver
from helpers import navTo, handleLogin

def Home():
    navTo('https://wolverineaccess.umich.edu')

def Student():
    handleLogin(navTo, 'https://weblogin.umich.edu/?cosign-csprod.dsc&https://csprod.dsc.umich.edu/services/student', False)

def StudentCenter():
    handleLogin(Student)
    driver.execute_script("LaunchURL(this,'https://csprod.dsc.umich.edu/psp/csprodnonop_newwin/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL',0,'bGrouplet@1;','')")

def EmployeeSelfService():
    handleLogin(navTo, 'https://weblogin.umich.edu/?cosign-hcmprod.dsc&https://hcmprod.dsc.umich.edu/services/employee', True)