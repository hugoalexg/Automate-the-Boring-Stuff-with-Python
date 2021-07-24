'''
Auto Unsubscriber
Write a program that scans through your email account, finds all the 
unsubscribe links in all your emails, and automatically opens them in 
a browser. This program will have to log in to your email provider’s IMAP 
server and download all of your emails. You can use BeautifulSoup (covered 
in Chapter 11) to check for any instance where the word unsubscribe occurs 
within an HTML link tag.

Once you have a list of these URLs, you can use webbrowser.open() to 
automatically open all of these links in a browser.

You’ll still have to manually go through and complete any additional steps 
to unsubscribe yourself from these lists. In most cases, this involves 
clicking a link to confirm.

But this script saves you from having to go through all of your emails 
looking for unsubscribe links. You can then pass this script along to 
your friends so they can run it on their email accounts. (Just make 
sure your email password isn’t hardcoded in the source code!)
'''
import imapclient
import datetime
import pyzmail
import bs4
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time

#https://medium.com/pyladiesbh/beautiful-soup-parseamento-de-html-337197a7d4b9
print('Please type your email:')
myemail = input()
print('Now type your email\'s password:')
mypassword = input()

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(myemail, mypassword)
imapObj.select_folder('INBOX', readonly=False)

#UIDs = imapObj.search(['SINCE', datetime.date(2021, 6, 26)])
UIDs = imapObj.search(['ON', datetime.date(2021, 7, 6)]) #para teste, peguei apenas emails de 6-jul-2021
print(UIDs)

links = []
#vai procurar em todos os emails links de unsubscribe
for index in UIDs:
	rawMessages = imapObj.fetch([index], ['BODY[]', 'FLAGS'])
	message = pyzmail.PyzMessage.factory(rawMessages[index][b'BODY[]'])
	if message.html_part != None:
		html = message.html_part.get_payload().decode(message.html_part.charset)
		soup = bs4.BeautifulSoup(html, 'lxml')
		alist = soup.find_all('a', href=True)
		for i in alist:
			if 'unsubscribe' in str(i).lower():
				links.append(i['href'])
			elif 'cancelar' in str(i).lower():
				links.append(i['href'])
			elif 'descadastre' in str(i).lower():
				links.append(i['href'])
imapObj.logout()
	
mainladd = []
tabs = 0
driver = webdriver.Chrome()
#abrir todos os links de unsubscribe, fazendo verificação para não abrir repetido
for link in links:
	mainl = link.split('/')[2]
	if mainl not in mainladd: #se o link ainda não foi aberto, abrir
		print('Opening link to ' + mainl + '...')
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[tabs])
		tabs += 1
		driver.get(link)	
		time.sleep(2)
	mainladd.append(mainl)