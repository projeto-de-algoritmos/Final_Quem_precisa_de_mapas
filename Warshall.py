import numpy as np
import pdb
import json

def Path(u, v, caminhos):
    if caminhos[u][v] == None:
        return []
    path = [u]
    while u != v:
        u = caminhos[u][v]
        path.append(u)
    return path

f = open('JotaZao.json')
data = json.load(f)
inf = np.inf

n = len(data['Matriz'])


matriz = [[inf for i in range(n)] for j in range(n)]
caminhos = [] 

for i in range(n):
	line = []
	for j in range(n):
		line.append(None)
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


print(Path(1,15, caminhos))



