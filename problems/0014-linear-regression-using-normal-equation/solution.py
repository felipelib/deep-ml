import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    at = []
    for i in range(len(a[0])):
        nova_linha = []
        for j in range(len(a)):
            nova_linha.append(a[j][i])
        at.append(nova_linha)
    return at

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    c = []
    if len(a[0]) != len(b):
        return -1
    for i in range(len(a)):
            nova_linha = []
            for j in range(len(b[0])):
                soma_elemento = 0
                for k in range(len(b)):
                    soma_elemento += a[i][k] * b[k][j]
                nova_linha.append(soma_elemento)
            c.append(nova_linha)
    return c

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	y_coluna = [[valor] for valor in y]
	X_transposta = transpose_matrix(X)
	Xt_X = matrixmul(X_transposta, X)
	Xt_X = np.array(Xt_X)
	Xt_y = matrixmul(X_transposta, y_coluna)
	Xt_y = np.array(Xt_y)
	solucao = np.linalg.solve(Xt_X, Xt_y)
	return solucao.flatten().tolist()