lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def duplicados():
    # Percorre cada lista dentro da lista de listas
    for lista in lista_de_listas_de_inteiros:
        # Conjunto para guardar os números já vistos
        vistos = set()
        # Marcador para saber se encontramos um duplicado
        encontrou = False

        # Percorre cada número dentro da lista atual
        for numero in lista:
            # Se o número já apareceu antes (está em "vistos")
            if numero in vistos:
                print(numero)       # Mostra o duplicado encontrado
                encontrou = True    # Marca que já achamos
                break               # Para o laço, não precisa continuar
            # Caso contrário, adiciona o número em "vistos"
            vistos.add(numero)

        # Se terminou a lista sem encontrar duplicado
        if not encontrou:
            print(-1)   # Mostra -1 porque não havia duplicados

print(duplicados())