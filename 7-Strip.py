'''
Regex Version of strip()
Write a function that takes a string and does the same thing as the strip() 
string method. If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the 
string. Otherwise, the characters specified in the second argument to the 
function will be removed from the string.
'''
import re

def regex_strip(text, remove = ' '):
	patter = re.compile(r'([\W\s]*)(\w.*\w)([\W\s]*)')
	mo = patter.search(text)
	if remove in mo.group(1):
		return mo.group(2)
	else:
		return text

print(regex_strip('................Teste para verificar se remove...................','.'))

