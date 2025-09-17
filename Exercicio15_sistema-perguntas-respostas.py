# Lista de perguntas, cada uma representada por um dicionário
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',  
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Contador para armazenar quantas perguntas o usuário acertou
qtd_acertos = 0

# Loop para percorrer todas as perguntas
for pergunta in perguntas:
    # Mostra o enunciado da pergunta
    print('Pergunta:', pergunta['Pergunta'])

    # Obtém a lista de opções dessa pergunta
    opcoes = pergunta['Opções']

    # Mostra cada opção numerada (0, 1, 2, ...)
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    # Pede para o usuário escolher uma opção digitando o número correspondente
    escolha = input('Escolha uma opção: ')

    # Variáveis de controle para validar a resposta
    acertou = False  # Assume que errou até provar o contrário
    escolha_int = None  # Vai guardar o número digitado convertido para inteiro
    qtd_opcoes = len(opcoes)  # Quantidade total de opções

    # Verifica se o valor digitado é um número
    if escolha.isdigit():
        escolha_int = int(escolha)  # Converte para inteiro

    # Se foi digitado um número válido, verifica se está dentro do intervalo de opções
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            # Compara a opção escolhida com a resposta correta
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True  # Marca como acerto

    print()  # Pula uma linha para organização da saída

    # Exibe se acertou ou errou
    if acertou:
        qtd_acertos += 1  # Soma mais 1 ao total de acertos
        print('✔️   Acertou')
    else:
        print('❌   Errou')

    print()  # Linha em branco para separar as perguntas

# Exibe a pontuação final
print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')
