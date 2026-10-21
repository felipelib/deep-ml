
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	projecao = []
	numerador = 0
	denominador = 0
	for i in range(len(L)):
		numerador += L[i] * v[i]
		denominador += L[i] * L[i]
	fracao = numerador / denominador
	for i in range(len(L)):
		L[i] = fracao * L[i]
		projecao.append(L[i])
	return projecao
