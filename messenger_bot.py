from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import sys

# validating arguments and creating link

if len(sys.argv) < 3:
    raise Exception("You must enter at least 2 arguments")

name = sys.argv[1]
name = name.lower()
name = name.replace(" ",".")

link = 'https://www.facebook.com/messages/t/'+name

# Setting notifications to not show while bot is running
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)

# getting persons messenger website
print("Driver ok: ", type(driver))
driver.get(link)

# Logging to website
with open("pass.txt") as f:
    passlist = f.readlines()

passlist[0] = passlist[0].rstrip("\n")
userLog = driver.find_element_by_name("email")
userLog.send_keys(passlist[0])
userLog = driver.find_element_by_name("pass")
userLog.send_keys(passlist[1])
userLog.submit()

time.sleep(1)

# sending message
textBox = driver.find_element_by_class_name("_1mj")
textBox.click()
textBox.send_keys(sys.argv[2], Keys.ENTER)

