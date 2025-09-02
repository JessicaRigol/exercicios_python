
print('---CALCULADORA---')
print('(+) para somar\n' \
    '(-) para subtrair\n' \
    '(*) para multiplicar\n' \
    '(/) para dividir\n' \
    '(s) para sair')

while True:
    operacao = input('Digite a operação que deseja calcular: ')
    
    if operacao.lower() == 's':
        print('Saindo...')
        break

    if operacao not in ['+','-','*','/']:
        print('Erro. Digite uma das operações válidas')
        continue
    
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if operacao == '+':
            soma = num1 + num2
            print(f'Resultado: {num1} + {num2} = {soma:.1f}')
        
        elif operacao == '-':
            subtracao = num1 - num2
            print(f'Resultado: {num1} - {num2} = {subtracao:.1f}')

        elif operacao == '*':
            multiplicacao = num1 * num2
            print(f'Resultado: {num1} * {num2} = {multiplicacao:.1f}')
        
        elif operacao == '/':
            if num2 == 0:
                print('Erro: não é possível dividir por zero.')
            else:
                divicao = num1 / num2
                print(f'Resultado: {num1} / {num2} = {divicao:.1f}')

        else: 
            print('Erro. Digite uma das operações válidas')
            continue
    except:
        print('Erro! Digite apenas números')
        continue

    