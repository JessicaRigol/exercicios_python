def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(multiplicacao(3,3,9))

def par_impar(num):
    if num % 2 == 0:
        return 'par'
    return 'impar'

print(par_impar(12))
print(par_impar(3))

