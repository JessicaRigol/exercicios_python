import os

lista = []

while True: 
    try:
        print('Selecione a opção')
        opcao = input('[i]nserir [a]pagar [l]istar: ')

        if opcao == 'i':
            os.system('cls') # limpar
            valor = input('Valor: ')
            lista.append(valor)

            print('Items na lista:')
            for indice, valor in enumerate(lista):
                print(indice, valor) 
            continue 
        
        elif opcao == 'a':
           apagar = int(input('Escolha o indice para apagar: '))
          
           if (apagar <= len(lista)-1):
                apagado = lista.pop(apagar)
                print(f'Item {apagado} apagado')
           else:
                print('Esse índice não existe')
                continue

        elif opcao == 'l':
            os.system('cls') # limpar
            if lista == []:
                print('Nada para listar')
            else:
                print('Items na lista:')
                for indice, valor in enumerate(lista):
                    print(indice, valor)
   
        else:
            print('Saindo da lista...')
            break

    except ValueError:
        print('Por favor digite número int.')
    except IndexError:
        print('Índice não existe na lista')
    except Exception:
        print('Erro desconhecido')
        