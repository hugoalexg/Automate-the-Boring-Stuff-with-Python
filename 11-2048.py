'''
2048
2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high 
score by repeatedly sliding in an up, right, down, and left pattern over 
and over again. Write a program that will open the game at 
https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, 
and left keystrokes to automatically play the game.
'''
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://play2048.co/")

driver.maximize_window()

driver.find_element_by_css_selector('div.above-game > a').click()

keys_list = [ Keys.UP, Keys.LEFT, Keys.DOWN, Keys.RIGHT]

time.sleep(2)

while True:
	for elem in keys_list:
		driver.find_element_by_tag_name('html').send_keys(elem)
		time.sleep(1)

		
