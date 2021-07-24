'''
Comma Code
Say you have a list value like this:


spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns 
a string with all the items separated by a comma and a space, with and 
inserted before the last item. For example, passing the previous spam 
list to the function would return 'apples, bananas, tofu, and cats'. 
But your function should be able to work with any list value passed 
to it.

'''
def phrase(listn):
	tx = ''
	for i in range(len(listn) - 2):
		tx = tx + listn[i] + ', '
	tx = tx + listn[len(listn) - 2] + ' and ' + listn[len(listn) - 1]
	return tx	

spam = ['apples', 'bananas', 'tofu', 'cats', 'blueberry','potatoes','banana','pasta','barbecue','pork']

print(phrase(spam))
