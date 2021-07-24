'''
PDF Paranoia
Using the os.walk() function from Chapter 9, write a script that will go 
through every PDF in a folder (and its subfolders) and encrypt the PDFs 
using a password provided on the command line. Save each encrypted PDF 
with an _encrypted.pdf suffix added to the original filename. Before 
deleting the original file, have the program attempt to read and decrypt 
the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its 
subfolders) and creates a decrypted copy of the PDF using a provided 
password. If the password is incorrect, the program should print a message 
to the user and continue to the next PDF.
'''
import pyperclip
import os
import PyPDF2
import send2trash as s2t
import sys
import time

password = str(sys.argv[1])

# função que retorna uma lista com uma tupla (caminho, arquivo) para todos os arquivos
# dentro daquele diretorio da extensão determinada
def filesInFolder(dirc, extension):
	pathlist = []
	os.chdir(dirc)
	#faz a varredura de todas as pastas e arquivos para encontrar os PFDs
	for folderName, subfolder, filenames in os.walk(dirc):
		for file in filenames:
			if extension in file.split('.')[-1].lower():
				pathlist.append((folderName, file)) #lista de tuplas
	return pathlist


maindir = pyperclip.paste()
os.chdir(maindir)

pathlist = filesInFolder(maindir, 'pdf')

#criando arquivos encriptados
for path in pathlist:
	os.chdir(path[0])
	pdfFileObj = open(path[1], 'rb')
	pdfWriter = PyPDF2.PdfFileWriter()
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

	pdfWriter.encrypt(password)
	
	newFileName = path[1].split('.')[0] + '_encrypted.pdf'
	pdfOutputFile = open(newFileName, 'wb')
	pdfWriter.write(pdfOutputFile)
	pdfOutputFile.close()
	pdfFileObj.close()
	
	time.sleep(1)
	#abrindo o arquivo criado para verificar e foi mesmo protegido
	pdfNewReader = PyPDF2.PdfFileReader(open(newFileName, 'rb'))

	if (pdfNewReader.isEncrypted is True) and (pdfNewReader.decrypt(password) == 1):
		s2t.send2trash(path[1]) 
	else:
		print("Arquivo " + newFileName + " não foi protegido da forma correta.")