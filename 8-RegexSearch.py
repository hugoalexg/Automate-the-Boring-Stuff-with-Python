'''
Regex Search
Write a program that opens all .txt files in a folder and searches for any 
line that matches a user-supplied regular expression. The results should 
be printed to the screen.
'''
import re
import os

maindir = 'C:\\Users\\H103893\\Desktop\\Hugo\\PYTHON'

os.chdir(maindir)

pathlist = []

pattern = re.compile(r'([\D\s]*)([1]\d{7})([\D\s])') #procurar um numero SAP

#faz a varredura de todas as pastas e arquivos
for folderName, subfolder, filenames in os.walk(maindir):
	for file in filenames:
		if 'txt' in file.split('.')[-1]:
			pathlist.append(folderName + '\\' + file)

#imprime path e linha com padrao encontrado
for path in pathlist:
	currentfile = open(path)
	lines = currentfile.readlines()
	for line in lines:
		mo = pattern.findall(line)
		if len(mo) > 0:
			print('---------------------------------------')
			print(path)
			print(line)
			print('---------------------------------------')
	currentfile.close()