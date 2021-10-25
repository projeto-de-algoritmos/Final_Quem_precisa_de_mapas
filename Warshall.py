import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json

def getPath(u, v, caminhos):
	if caminhos[u][v] is None:
		return []
	path = [u]
	while u != v:
			u = caminhos[u][v]
			path.append(u)
	return path

def warshall(path):
	f = open(path + '.json')
	data = json.load(f)
	inf = np.inf

	n = len(data['Matriz'])


	matriz = [[inf for i in range(n)] for j in range(n)]
	caminhos = [] 

	for _ in range(n):
			line = [None for _ in range(n)]
			caminhos.append(line)


	for i in range(len(data['Matriz'])):
		for adj in data['Matriz'][i]['adj']:
			matriz[i][adj] = abs(data['Matriz'][i]['x'] - data['Matriz'][adj]['x']) + abs(data['Matriz'][i]['y'] - data['Matriz'][adj]['y'])
			caminhos[i][adj] = adj

	for i in range(n):
		matriz[i][i] = 0;
		caminhos[i][i] = i;

	for k in range(n):
		old = matriz
		for i in range(n):
			for j in range(n):
				if(old[i][j] > old[i][k] + old[k][j]):
					matriz[i][j] = old[i][k] + old[k][j]
					caminhos[i][j] = caminhos[i][k]
	
	return caminhos

def draw(path):
	caminhos = warshall(path)

	f = open(path + '.json')
	data = json.load(f)['Matriz']

	while True:
		print()
		print('Digite 0 para sair no ponto inicial ou final')
		pi = int(input('Digite o ponto inicial 1-' + str(len(data)) + ': '))
		pf = int(input('Digite o ponto final 1-' + str(len(data)) + ': '))

		if pi in [pf, 0]:
			menu()

		ordem = getPath(pi, pf, caminhos)

		for i in range(len(ordem) - 1):
			j = ordem[i]
			j2 = ordem[i+1]

			plt.plot((data[j]['x'], data[j2]['x']), (data[j]['y'], data[j2]['y']), marker = 'o')

		img = mpimg.imread(path + '.png')
		imgplot = plt.imshow(img)
		plt.show()

def menu():
	print()
	print('Digite 1 para o mapa1')
	print('Digite 2 para o mapa2')
	print('Digite 3 para sair')
	opcao = int(input())

	if(opcao == 1):
		draw('mapas/mapa1')
	elif(opcao == 2):
		draw('mapas/mapa2')
	elif(opcao == 3):
		exit()
	else:
		print('Digite um numero válido')
		menu()

menu()







