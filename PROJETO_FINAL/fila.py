from no import No
class Fila(No):
    def __init__(self, size=0):
        self.first = None
        self.last = None
        self.size = size

    # Método para adicionar elemento na fila - última posição
    def add(self, elem):
        no = No(elem)
        add = self.first
        if add == None:
            self.first = no
            print(f'Elemento {self.first} adicionado na primeira posição.')
        else:
            while (add.get_proximo() != None):
                add = add.get_proximo()
            add.set_proximo(no)
            print(f'Elemento {elem} adicionado na útlima posição.')
        self.size += 1

    # Método para remover elemento na fila - primeira posição
    def remove(self):
        if self.first != None:
            print(f'Elemento: {self.first} sendo removido da fila.')
            self.first = self.first.get_proximo()

            self.size -= 1
        else:
            print('Fila está vazia, não há elemento na fila.')

    # Método para verificar se fila está vazia
    def isEmpty(self):
        return self.topo is None

    # Método para exibir o tamanho da fila
    def Tamanho(self):
        if self.size == 0:
            return f'Fila está vazia, zero elementos.'
        elif self.size == 1:
            return f'Fila possui apenas um elemento na lista.'
        else:
            return f'Fila possui {self.size} elementos.'

    # Método para percorrer a fila
    def Queue(self):
        aux = self.first
        if aux is None:
            print('Fila está vazia, não há elemento para ser mostrado: ', end=' ')
        else:
            while aux is not None:
                print(aux.get_dado())
                aux = aux.get_proximo()

    # Método para mostrar o primeiro elemento
    def firstE(self):
        return f'Primeiro elemento: {self.first}'

    # Método para mostrar o último elemento
    def lastE(self):
        last = self.first
        aux = last.get_proximo()
        if last == None:
            'Fila está vazia.'
        else:
            while aux != None:
                last = aux.get_proximo()
                if last is None:
                    break
                aux = last

            print(f'ÚLTIMO {aux}')