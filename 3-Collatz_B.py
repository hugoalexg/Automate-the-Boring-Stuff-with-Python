import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def collatz(x):
	x = int(x)
	seq = 0
	while x > 1:
		seq += 1
		if x % 2 == 0:
			x = int(x/2)
		else:
			x = int(3*x+1)
	return seq


vec = np.arange(1,1001)
df = pd.DataFrame({'numero': vec })
df['inter'] = df['numero'].apply(collatz)
df['div4'] = df['numero'].apply(lambda x: 'sim' if x % 4 == 0 else 'nao')
print(df)

plt.figure(figsize=(10,6))
sns.scatterplot(x = 'numero', y = 'inter', hue = 'div4', data = df)
plt.show()
