import os

arquivo_tarefas = 'tarefas.txt'
linhas_desfeitas = [] # para armazenar linhas removidas

def inserir_tarefas(tarefa):
    with open(arquivo_tarefas,'a', encoding='utf-8') as arquivo:
            arquivo.write(tarefa + '\n')  

def listar_tarefas():
     with open(arquivo_tarefas, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        if not conteudo:
            return 'Nada para listar'
        return conteudo
     
def desfazer_tarefas():
    global linhas_desfeitas
    with open(arquivo_tarefas, 'r+', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            return 'Nada para desfazer'
        ultima_linha = linhas.pop()             # remove a última linha
        linhas_desfeitas.append(ultima_linha)   # guarda para refazer
        with open(arquivo_tarefas, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
        return f"Desfeito: {ultima_linha.strip()}"           

def refazer_tarefas(): 
    global linhas_desfeitas
    if not linhas_desfeitas:
        return "Nada para refazer."
    linha = linhas_desfeitas.pop()              # pega a última linha desfeita
    with open(arquivo_tarefas, 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha)
    return f"Refeito: {linha.strip()}"

while True:

    print('Comandos:\n' \
    '1 - Listar\n' \
    '2 - Desfazer\n' \
    '3 - Refazer \n' \
    '4 - Inserir tarefa')
    comandos = int(input('Escolha o número do comando: '))

    os.system('cls')

    if comandos == 4:
        tarefa  = input('Digite a tarefa: ')
        print(inserir_tarefas(tarefa))

    elif comandos == 1:
     print(listar_tarefas())

    elif comandos == 2:
     print(desfazer_tarefas())

    elif comandos == 3:
     print(refazer_tarefas())
     
    print('TAREFAS:')
    print(listar_tarefas())