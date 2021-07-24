'''
Link Verification
Write a program that, given the URL of a web page, will attempt to download 
every linked page on the page. The program should flag any pages that have 
a 404 “Not Found” status code and print them out as broken links.
'''
import bs4
import requests

#main_url = 'https://pt.wikipedia.org/wiki/Iced_Earth'
main_url = 'https://automatetheboringstuff.com/chapter11/'

res = requests.get(main_url)

try:
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	alist = soup.find_all('a', href=True)

	links = []

	for elem in alist:
		if elem['href'][0:4] == 'http':
			links.append(elem['href'])
		elif elem['href'][0:2] == '//':
			links.append('http:' + elem['href'])
		elif elem['href'][0] == '#':
			links.append(main_url + elem['href'])
		elif elem['href'][0] == '/' and elem['href'][1] != '/':
			links.append( 'https://' + main_url.split('/')[2] + elem['href'])

except Exception as exc:
	print('There was a problem: ' + str(exc))

for elem in links:
	print(elem)
