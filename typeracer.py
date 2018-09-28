from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import smtplib
import sys


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
chrome_path = ""

driver = webdriver.Chrome(chrome_path, options=options)

driver.get("https://play.typeracer.com/")

while True:
	try:
		driver.find_element_by_xpath("""//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a""").click()
		break
	except:
		continue
sleep(5)

try:
	words = driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]""").text
except:
	print("")

try:
	words += driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]""").text + " "
except:
	print("")

try:
	words += driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]""").text
except:
	print("")


print(words)


inputField = driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input""")

#Sleeps because the game can detect cheaters if the sleep is not used...Slows down the WPM slightly
for character in words:
	inputField.send_keys(character)
	sleep(0.01)



