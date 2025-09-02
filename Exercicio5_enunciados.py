"""
numero = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print(f'o número {numero_inteiro} é par')
    else:
        print(f'o número {numero} é ímpar')
except:
    print(f'{numero} não é um número inteiro')

"""

"""
hora = input("Que horas são: ")

try:
    hora_inteira = int(hora)

    if hora_inteira >=0 and hora_inteira <= 11:
        print('Bom dia!')

    elif hora_inteira >= 12 and hora_inteira <= 17:
        print('Boa tarde!')

    elif hora_inteira >= 18 and hora_inteira <= 23:
        print('Boa noite!')

    else: 
        print('Digite um horario entre 0 e 23')
except:
 print(f'{hora} não é um horário inteiro')
 print('Digite um horario entre 0 e 23')
"""

nome = input('Digite seu primeiro nome: ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto')
elif letras >=5 and letras <=6:
    print('Seu nome é normal')
elif letras > 6:
    print('Seu nome é muito grande')

