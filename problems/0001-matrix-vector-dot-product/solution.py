def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	indicador = 0
	soma_linha = 0
	matriz_resultado = []
	for i in a:
		if len(a[indicador]) != len(b):
			return -1
		else:
			for j in range(len(a[indicador])):
				soma_linha += a[indicador][j] * b[j]
			matriz_resultado.append(soma_linha)
			soma_linha = 0
		indicador += 1
	return matriz_resultado