##################################
### Only for education perpose ###
#Details: Operate Chrome browser from python script, webscraping a webpage on it and trying to automate "typing and showing message option" with python scripting"
##################################

# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
import time

#keepTheBrowserAlive
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
chrome_browser = Chrome(options=opts)

# chrome_browser = webdriver.Chrome(keep_alive=True)

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# print('Python Easy Demo' in chrome_browser.title)
# assert 'Python Easy Demo' in chrome_browser.title
# print('Selenium Easy Demo' in chrome_browser.title)
# assert 'Selenium Easy Demo' in chrome_browser.title
# button = chrome_browser.find_elements('class name', value='btn-default')
# button = chrome_browser.find_elements(By.CLASS_NAME, value='btn-default')
button = chrome_browser.find_element(By.CLASS_NAME, value='btn-primary')
# print(button.__getattribute__('innerHTML'))
print((button.get_attribute('innerHTML')))
# print(button)
# print(button.__class_getitem__('innerHTML'))
# print(button.__getattribute__('innerHTML'))
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I am writing too fast, Rocked!!!')

button.click()

output_message = chrome_browser.find_elements(By.ID,'display')
# x = chrome_browser.find_element(By.ID,'display')
# print((x.get_attribute('innerHTML')))

print(chrome_browser.find_element(By.CLASS_NAME,'form-control').get_attribute('outerHTML'))
print(time.time())
time.sleep(10)
chrome_browser.quit()



