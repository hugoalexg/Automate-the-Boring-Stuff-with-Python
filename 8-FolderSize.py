import os
#calcula a soma de todos os aquivos que estão no diretorio
def calc_size(dirname):
	totalSize = 0
	for filename in os.listdir(dirname):
		if not os.path.isfile(os.path.join(dirname, filename)):
			totalSize = totalSize + calc_size(os.path.join(dirname, filename))
			continue
		totalSize = totalSize + os.path.getsize(os.path.join(dirname, filename))
	return totalSize	

maindir = 'C:\\Users\\H103893\\Desktop\\Hugo\\PYTHON'
os.chdir(maindir)

print(str(calc_size(maindir)) + ' bytes')