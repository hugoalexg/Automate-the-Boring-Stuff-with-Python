'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password 
string it is passed is strong. A strong password is defined as one that is 
at least eight characters long, contains both uppercase and lowercase 
characters, and has at least one digit. You may need to test the string 
against multiple regex patterns to validate its strength.
'''
import re

def test_password(password):	
	if not re.compile(r'\S{8}\S*').search(password):
		return False
	elif not re.compile(r'[a-z]+').search(password):
		return False
	elif not re.compile(r'[A-Z]+').search(password):
		return False
	elif not re.compile(r'\d+').search(password):
		return False
	else:
		return True

print('Please type a password:')
text = input()

if test_password(text):
	print('Strong password!')
else:
	print('Weak password!')
