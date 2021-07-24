'''
Selective Copy
Write a program that walks through a folder tree and searches for files 
with a certain file extension (such as .pdf or .jpg). Copy these files 
from whatever location they are in to a new folder.
'''
import os
import shutil

maindir = 'C:\\Users\\H103893\\Desktop\\Hugo\\MACAE\\RADIOATIVO'
os.chdir(maindir)

pathlist = []
extension = 'txt'

#faz a varredura de todas as pastas e arquivos
for folderName, subfolder, filenames in os.walk(maindir):
	for file in filenames:
		if extension in file.split('.')[-1]:
			pathlist.append(folderName + '\\' + file)

maindir = 'C:\\Users\\H103893\\Desktop\\Hugo\\PYTHON'
os.chdir(maindir)
newfolder = os.path.join(os.getcwd(),'TESTE')

#criar nova pasta
try:
	os.makedirs(newfolder)
except:
	print('Pasta ja criada.')

#copiar arquivos para nova pasta
for path in pathlist:
	print(os.path.basename(path))	
	try:
		shutil.copy(path, newfolder)
	except:
		print('o arquivo "' + os.path.basename(path) + '" ja existe nessa pasta.')