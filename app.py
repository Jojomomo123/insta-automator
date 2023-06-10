# from flask import Flask
# from subprocess import Popen
#
# app = Flask(__name__)
#
# @app.route('/automate-instagram', methods=['GET'])
# def automate_instagram():
#     print("hiiii")
#     process = Popen(['python', 'sel.py'])  # Replace 'sel.py' with the actual filename containing your Selenium code
#     return 'Automation started!'
#
# if __name__ == '__main__':
#     print("hiii")
#     app.run()
#     automate_instagram()
import time

# from flask import Flask
#
# app = Flask(__name__)
# def automate_instagram():
#     print("hiiii")
#     process = Popen(['python', 'sel.py'])  # Replace 'sel.py' with the actual filename containing your Selenium code
#     return 'Automation started!'
# if __name__ == '__main__':
#     app.run()
#     automate_instagram()

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
cwd = os.getcwd()
print(cwd)
# from selenium.webdriver.common.proxy import Proxy , ProxyType
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
browser = webdriver.ChromeOptions()

@app.route('/')
# ‘/’ URL is bound with hello_world() function.

def hello_world():
    global browser, cwd
    # hi()
    # browser = webdriver.Chrome(r'C:\Users\joshu\Downloads\chromedriver_win32 (11)\chromedriver.exe', options=options)
    options = Options()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(r'C:\Users\joshu\Downloads\chromedriver_win32 (11)\chromedriver.exe', options=options)
    # Open Instagram
    browser.get('https://www.instagram.com/')
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
    browser.find_elements(By.TAG_NAME, 'input')[0].send_keys("georgebailey065@gmail.com")
    browser.find_elements(By.TAG_NAME, 'input')[1].send_keys("Frog1468")
    browser.find_elements(By.TAG_NAME, 'button')[1].click()
    # browser.find_element
    notifications()
    # try:
    # WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'x1a2a7pz')))
    time.sleep(5)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'x1a2a7pz')))
    browser.find_elements(By.CLASS_NAME, 'x1a2a7pz')[7].click()
    time.sleep(3)
    browser.find_element(By.TAG_NAME, 'input').send_keys(cwd + "/images/sample.png")
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'x1yc6y37').click()
    print("klsjkljk")
    return 'Hello World'

def notifications():
    global browser
    try:
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'x1a2a7pz')))
        browser.find_element(By.CLASS_NAME, '_a9_1').click()
    except:
        pass


# main driver function
if __name__ == '__main__':
    # process = Popen(['python', 'sel.py'])
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
    print("hello llll")