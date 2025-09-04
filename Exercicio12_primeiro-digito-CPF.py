import re
# cpf = '964.567.100-06'.replace('.','').replace('-','') 
# -- OU --
cpf = re.sub(r'[^0-9]','','964.567.100-06')
# str_cpf = str(cpf)
quebra_cpf = list(cpf)
multiplicar_1 = range(10, 1, -1)
multiplicar_2 = range(11, 1, -1)
juntar_1 = zip(quebra_cpf, multiplicar_1)
juntar_2 = zip(quebra_cpf, multiplicar_2)

# for para primeiro digito
total = 0
for digito, multiplicador in juntar_1:
    mult = int(digito) * multiplicador
    total += mult

# for para segundo digito
total2 = 0
for digito2, multiplicador2 in juntar_2:
    mult2 = int(digito2) * multiplicador2
    total2 += mult2

multipla_10 = total * 10
multipla_10_2 = total2 * 10
resto = multipla_10 % 11
resto2 = multipla_10_2 % 11

primeiro_digito = resto if resto <= 9 else 0
segundo_digito = resto2 if resto2 <= 9 else 0

print(f'O primerio digito do CPF é {primeiro_digito}')
print(f'O segundo digito do CPF é {segundo_digito}')
    



    







    
    





    
