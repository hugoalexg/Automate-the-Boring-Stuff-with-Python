'''
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files or folders to take 
up the bulk of the space on your hard drive. If you’re trying to free up 
room on your computer, you’ll get the most bang for your buck by deleting 
the most massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for 
exceptionally large files or folders—say, ones that have a file size of 
more than 100MB. (Remember, to get a file’s size, you can use 
os.path.getsize() from the os module.) Print these files with their 
absolute path to the screen.
'''
import os
import shutil

maindir = 'C:\\Users\\H103893\\Desktop\\Hugo\\MACAE'
os.chdir(maindir)

#mapear aquivos em uma pasta maiores que 100MB
for folderName, subfolder, filenames in os.walk(maindir):
	for file in filenames:
		filesize = os.path.getsize(os.path.join(folderName, file))
		if filesize > 104857600:
			print('---------------------------------------')
			print(os.path.join(folderName, file))
			print(str(filesize) + ' BYTES')
			print('---------------------------------------')


	
