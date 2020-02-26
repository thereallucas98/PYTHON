from no import No
from dado import Dado
from fila import Fila
from pilha import Pilha
from lista import Lista
#import os
import time
fila = Fila()
pilha = Pilha()
no = No()
lista = Lista()
print('PROJETO ESTRUTURA DE DADOS - PILHA - FILA - LISTA')
print('PROFESSOR: THIAGO MOURA')
print('ALUNOS:\nDAVID LUCAS;\nMARIA REBECA.')
time.sleep(5)
while True:
    print('=======================================')
    print('Escolha uma das opções abaixo:\n'
          '1. Pilha\n'
          '2. Fila\n'
          '3. Lista\n'
          '0. Sair\n')
    op = int(input('Opção: '))

    if op == 0:
        print('Encerrando operações!')
        break
    # PILHA
    elif op == 1:
        while True:
            print('======================================')
            time.sleep(1)
            print('Escolha uma das opções abaixo:\n'
                  '1. Adicionar elemento a pilha\n'
                  '2. Remover elemento da pilha\n'
                  '3. Exibir o topo da pilha\n'
                  '4. Exibir o tamanho da pilha\n'
                  '5. Exibir a pilha\n'
                  '0. Sair')
            op_pilha = int(input('Informe a opção: '))
            if op_pilha == 0:
                time.sleep(1)
                print('Encerrando operações.')
                break
            elif op_pilha == 1:
                p_nome = str(input('Informe o nome do filme/série: '))
                p_ano = int(input('Informe o ano de lançamento: '))
                p_produtora = str(input('Informe a distribuidora do filme/série: '))
                time.sleep(2)
                p_op = Dado(p_nome, p_ano, p_produtora)
                pilha.push(p_op)
            elif op_pilha == 2:
                if pilha.isEmpy() == True:
                    print(f'Pilha encontrase vazia. Não há elemento para ser removido.')
                else:
                    print('O elemento do topo será removido.')
                    time.sleep(3)
                    pilha.pop()
            elif op_pilha == 3:
                time.sleep(1)
                print(pilha.exibeTopo())
            elif op_pilha == 4:
                time.sleep(1)
                print(pilha.Tamanho())
            elif op_pilha == 5:
                time.sleep(1)
                print(pilha.exibePilha())
            else:
                print('OPÇÃO INVÁLIDA')
    # FILA
    elif op == 2:
        while True:
            print('======================================')
            time.sleep(1)
            print('Escolha uma das opções abaixo:\n'
                  '1. Adicionar elemento a fila\n'
                  '2. Remover elemento da fila\n'
                  '3. Exibir o primeiro elemento da fila\n'
                  '4. Exibir o último elemento da fila\n'
                  '5. Exibir o tamanho da fila\n'
                  '6. Exibir a fila\n'
                  '0. Sair')
            op_fila = int(input('Informe a opção: '))

            if op_fila == 1:
                f_nome = str(input('Informe o nome do filme/série: '))
                f_ano = int(input('Informe o ano de lançamento: '))
                f_produtora = str(input('Informe a distribuidora do filme/série: '))
                time.sleep(2)
                f_op = Dado(f_nome, f_ano, f_produtora)
                fila.add(f_op)
            elif op_fila == 2:
                print('De acordo com as regras, o primeiro elemento será removido.')
                time.sleep(3)
                fila.remove()
            elif op_fila == 3:
                pass
            elif op_fila == 4:
                pass
            elif op_fila == 5:
                time.sleep(2)
                print(fila.Tamanho())
            elif op_fila == 6:
                time.sleep(2)
                print(fila.Queue())
            elif op_fila == 0:
                print('OPERAÇÕES ENCERRADAS')
                break
            else:
                print('OPÇÃO INVÁLIDA')
    # LISTA
    if op == 3:
        while True:
            print('======================================')
            time.sleep(1)
            print('Escolha uma das oções abaixo:\n'
                  '1. Adicionar elemento na lista\n'
                  '2. Adicionar elemento em uma posição\n'
                  '3. Remover por posição\n'
                  '4. Exibir lista\n'
                  '5. Exibir o tamanho da lista\n'
                  '6. Buscar por posição\n'
                  '7. Tipos de Busca\n'
                  '0. Sair')
            op_lista = int(input('Informe a opção: '))
            if op_lista == 0:
                time.sleep(1)
                print('Encerrando operações.')
                break
            elif op_lista == 1:
                l_nome = str(input('Informe o nome do filme/série: '))
                l_ano = int(input('Informe o ano de lançamento: '))
                l_produtora = str(input('Informe a distribuidora do filme/série: '))
                time.sleep(2)
                l_op = Dado(l_nome, l_ano, l_produtora)
                lista.append(l_op)
            elif op_lista == 2:
                l_nome = str(input('Informe o nome do filme/série: '))
                l_ano = int(input('Informe o ano de lançamento: '))
                l_produtora = str(input('Informe a distribuidora do filme/série: '))
                pos = int(input('Informe a posição da lista, observação. A lista começa com a numeração padrão: [1 - ...]:   '))
                time.sleep(2)
                l_op_pos = Dado(l_nome, l_ano, l_produtora)
                lista.insert(pos, l_op_pos)
            elif op_lista == 3:
                pos_opfour = int(input('Informe a oposição que deseja remover: '))
                time.sleep(2)
                lista.removeByIndex(pos_opfour)
            elif op_lista == 4:
                time.sleep(2)
                print(lista.Listando())
            elif op_lista == 5:
                time.sleep(2)
                print(lista.Tamanho())
            elif op_lista == 6:
                pos_opseven = int(input('Informe a posição que deseja obter da lista: '))
                time.sleep(3)
                print(lista.BuscaByIndex(pos_opseven))
            elif op_lista == 7:
                print('1. Busca por Ano\n'
                      '2. Busca por Nome\n'
                      '3. Busca por Produtora')
                op_listaseven = int(input('Informe o tipo de busca abaixo: '))
                if op_listaseven == 1:
                    op_ano = int(input('Informe o ano: '))
                    time.sleep(3)
                    print(lista.BuscaAno(op_ano))
                elif op_listaseven == 2:
                    op_name = str(input('Informe o nome: '))
                    time.sleep(3)
                    print(lista.BuscaNome(op_name))
                elif op_listaseven == 3:
                    op_produtora = str(input('Informe a produtora: '))
                    time.sleep(3)
                    print(lista.BuscaProdutora(op_produtora))
                else:
                    time.sleep(3)
                    print('OPÇÃO INVÁLIDA')

    else:
        print(end='')
