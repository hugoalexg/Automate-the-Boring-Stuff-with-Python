'''
Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the 
player’s inventory will be a dictionary where the keys are string values 
describing the item in the inventory and the value is an integer value 
detailing how many of that item the player has. For example, the 
dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,
 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, 
 and so on.

Write a function named displayInventory() that would take any possible 
“inventory” and display it like the following:


Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''
def displayInventory(dic_itens):
	it_count = 0
	for key in dic_itens:
		print(str(dic_itens[key]) + ' ' + key)
		it_count += dic_itens[key]
	print('Total number of items: ' + str(it_count))


def addToInventory(dic_itens, add_items):
	dic_list = []
	#gerar lista de todos os itens ja no inventario
	for key in dic_itens:
		dic_list.append(key)
	#adicionar itens novos	
	for it in add_items:
		if it not in dic_list:
			dic_itens.setdefault(it, 0)
		for key in dic_itens:
			if (key == it):
				dic_itens[key] = dic_itens[key] + 1

		
itens = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby','spell', 'gold coin']

displayInventory(itens)
addToInventory(itens, dragon)
print('----------------------------------------------------------------------------------------------')
displayInventory(itens)




	