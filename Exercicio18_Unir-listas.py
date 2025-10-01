# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

def zipper(cidade, estado):
    zipper = []
    for x, y in zip(cidade, estado):
        zipper.append((x,y)) # <--tupla para juntar (cidade, estado)
    return zipper

print(zipper(cidade, estado))
