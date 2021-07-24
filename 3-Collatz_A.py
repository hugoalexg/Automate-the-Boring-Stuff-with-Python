'''
The Collatz Sequence

Write a function named collatz() that has one parameter named number. If number is even, then 
collatz() should print number // 2 and return this value. If number is odd, then collatz() should 
print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on 
that number until the function returns the value 1. (Amazingly enough, this sequence actually 
works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians 
aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called 
“the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the int() function; otherwise, 
it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

The output of this program could look something like this:


Enter number:
3
10
5
16
8
4
2
1

'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def collatz(x):
	try:
		lista = []
		x = int(x)
		while x > 1:
			if x % 2 == 0:
				x = int(x/2)
			else:
				x = int(3*x+1)
			lista.append(x)
	except:
		print('Digite um valor numerico inteiro!')
	return lista


print('Por favor digite um numero para verificar a sequencia de collatz:')
num = input()

df = pd.DataFrame({'numero': collatz(num)})
print(df)

sns.lineplot(data=df, x= df.index, y='numero')
plt.tight_layout()
plt.show()


