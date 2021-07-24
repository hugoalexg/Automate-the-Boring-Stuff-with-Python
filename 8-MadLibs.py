'''
Mad Libs
Create a Mad Libs program that reads in text files and lets the user add 
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears 
in the text file. For example, a text file may look like this:


The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.


Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:


The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.
'''
import os
import shelve
import re

os.chdir('C:\\Users\\H103893\\Desktop\\Hugo\\PYTHON\\Curso Automate Boring Stuff\\Exercicios')

inFile = open('MadLidsIn.txt').read()

rls = re.compile(r'ADJECTIVE|NOUN|VERB')
getall = rls.findall(inFile)
suball = rls.sub('xxxx',inFile).split('xxxx')
outFile = ''

print(suball)

for i in range(len(getall)):
	print('Please type a ' + getall[i] + ':')
	subword = input()
	outFile = outFile + suball[i] + subword
outFile = outFile + suball[-1]

print(outFile)

open('MadLidsOut.txt','w').write(outFile)
