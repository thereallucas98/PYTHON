from no import No
class Pilha(No):
    def __init__(self, topo = None):
        self.topo = topo
        self.size = 0


    # Método para adicionar elemento a pilha - sempre topo
    def push(self, new):
        no = No(new)
        no.set_proximo(self.topo)
        self.topo = no
        print(f'Elemento: {self.topo} adicionado a pilha.')
        self.size += 1


    # Método para remover o primeiro elemento da pilha
    def pop(self):
        if self.topo is None:
            print(f'Pilha está vazia, não há elemento para ser removido')
        else:
            aux = self.topo
            self.topo = self.topo.get_proximo()
            print(f'Elemento {aux} removido.')
            self.size -= 1


    # Método para verificar se pilha está vazia - função para utilizar em outras funções
    def isEmpy(self):
        return self.topo is None


    # Método para exibir o tamanho da pilha
    def Tamanho(self):
        if self.size == 1:
            return f'Pilha possui apenas um elemento.'
        elif self.size == 0:
            return f'Pilha está vazia.'
        else:
            return f'Pilha possui {self.size} elementos.'


    # Método para percorrer a pilha - desempilhando
    def exibePilha(self):
        aux = self.topo
        if aux == None:
            return f'Pilha está vazia'
        else:
            while(aux != None):
                print(aux.get_dado())
                aux = aux.get_proximo()


    # Método para exibir o topo da pilha
    def exibeTopo(self):
        aux = self.topo
        if self.topo != None:
            print(f'TOPO: {aux}')
        else:
            print('Pilha está vazia.')

