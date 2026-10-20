def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    inversa = []
    primeira_linha = []
    segunda_linha = []
    determinante = matrix[0][0] * matrix [1][1] - matrix[0][1] * matrix[1][0]
    if determinante == 0:
        return 'None'
    else:
        novo_primeiro_elemento = matrix[1][1]
        novo_segundo_elemento = matrix[0][1] * -1
        primeira_linha.append(novo_primeiro_elemento)
        primeira_linha.append(novo_segundo_elemento)
        inversa.append(primeira_linha)

        novo_terceiro_elemento = matrix[1][0] * -1
        novo_quarto_elemento = matrix[0][0]
        segunda_linha.append(novo_terceiro_elemento)
        segunda_linha.append(novo_quarto_elemento)
        inversa.append(segunda_linha)

        for i in range(len(inversa)):
            for j in range(len(inversa[0])):
                inversa[i][j] = inversa [i][j] * 1/determinante

        return inversa        