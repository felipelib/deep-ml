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