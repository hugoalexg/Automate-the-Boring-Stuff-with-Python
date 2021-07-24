'''
Umbrella Reminder
Chapter 11 showed you how to use the requests module to scrape data from 
http://weather.gov/. Write a program that runs just before you wake up in 
the morning and checks whether it’s raining that day. If so, have the 
program text you a reminder to pack an umbrella before leaving the house.
'''
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time
import bs4
import requests
import smtplib

print('Please type your email:')
myemail = input()
print('Now type your email\'s password:')
mypassword = input()

def weather(zip_code):
	driver = webdriver.Chrome()

	driver.get("https://www.weather.gov/")

	#entra no site para verificar qual a URL da previsao para o zipcode
	search = driver.find_element_by_css_selector('input#inputstring') #CSS selector
	search.clear()
	search.send_keys(zip_code)
	time.sleep(2)
	driver.find_element_by_css_selector('input#btnSearch').click()
	time.sleep(2)

	res = requests.get(driver.current_url)
	#coleta dado de clima na URL acima
	try:
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		elem = soup.select('div#current_conditions-summary > p.myforecast-current') #CSS selector
		return elem[0].text
		
	except Exception as exc:
		print('There was a problem: ' + str(exc))
		return None

subject = "ATENCAO!!!"
text = "LEVE O GUARDA-CHUVA, VAI CHOVER!!!"
message = 'Subject: {}\n\n{}'.format(subject, text)

#se etiver chovendo, envia email dizendo pra levar o guardachuva
if 'cloudy' in weather('76132').lower():  #Fort Worth (ZIP 76132)
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(myemail, mypassword)
	smtpObj.sendmail(myemail, myemail, message)
	smtpObj.quit()
	print("Email enviado!")