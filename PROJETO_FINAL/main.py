from no import No
from dado import Dado
from pilha import Pilha
from lista import Lista
from fila import Fila
pilha = Pilha()
lista = Lista()
fila = Fila()
no = No()
# LISTA
l1 = Dado('Avengers', 2019, 'Marvel')
l2 = Dado('Batman Begins', 2005, 'Warner Bros')
l3 = Dado('The Simpsons', 2006, 'FOX')
l4 = Dado('Spider-Man - Homecoming', 2017, 'Sony')
l5 = Dado('Toy Story', 2019, 'Pixar')
#lista.remove(l1)
lista.append(l1)
lista.append(l2)
print(lista.Tamanho())
lista.insert(1, l3)
lista.insert(0, l4)
print(lista.Tamanho())

print(lista.Listando())
print('\n\n')
lista.insert(7, l5)

print(lista.Listando())
#lista.remove()
print(lista.Listando())
#lista.remove(l1)
print(lista.Listando())
#lista.remove(l2)
print(lista.Listando())
#
'''print(fila.Tamanho())
l1 = Dado('The Big Bang Theory', 2007, 'CBS')
fila.add(l1)
print(fila.Tamanho())
l2 = Dado('The Flash', 2015, 'Warner Bros')
fila.add(l2)
print(fila.Tamanho())
l1 = Dado('Friends', 1991, 'Warner')
fila.add(l1)
print(fila.Tamanho())
l3 = Dado('Everybody Hates Chris', 2007, 'CBS')
fila.add(l3)
print(fila.Tamanho())
print('==========================================================\n')
print(fila.Queue())
print('===========================================================\n')
print(fila.firstE())
print(fila.lastE())
print('============================================================\n')
fila.remove()
print(fila.Tamanho())
print(fila.Queue())
print('============================================================\n')
fila.remove()
print(fila.Tamanho())
print(fila.Queue())
print('============================================================\n')
fila.remove()
print(fila.Tamanho())
print(fila.Queue())
print('============================================================\n')
fila.remove()
print(fila.Tamanho())
print(fila.Queue())
print('============================================================\n')'''
# PILHA
'''pilha.exibeTopo()
print(pilha.Tamanho())
print('============================\n')
f1 = Dado('Avengers - Endgame', 2017, 'Marvel')
pilha.push(f1)
print(pilha.exibeTopo())
print(pilha.Tamanho())
print(pilha.exibePilha())
print('============================\n')
f2 = Dado('Batman Begins', 2005, 'DC Domics')
pilha.push(f2)
print(pilha.exibeTopo())
print(pilha.Tamanho())
print(pilha.exibePilha())
print('============================\n')
print(pilha.exibePilha())
print('============================\n')
pilha.pop()
print(pilha.exibePilha())
print(pilha.Tamanho())'''
print(lista.BuscaByIndex(1))
print(lista.BuscaAno(2019))