from no import No
class Lista(No):
    def __init__(self):
        self.head = None
        self.size = 0

    # MÉTODO PARA ADICIONAR NO TOPO
    def append(self, elem):
        if self.head:
            # INSERÇÃO COM A LISTA POSSUINDO ELEMENTOS
            pointer = self.head
            while pointer.get_proximo():
                pointer = pointer.get_proximo()
            pointer.next = No(elem)
            print(f'Elemento: {elem} adicionado ao final da lista.')
        else:
            # INSERÇÃO NO TOPO - LISTA VAZIA
            self.head = No(elem)
            print(f'Primeiro elemento da lista: {elem}')
        self.size += 1


    # MÉTODO PARA PERCORRER O NÓ
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.get_proximo()
            else:
                return 'Posição Inexistente'
        return pointer

    # MÉTODO PARA INSERIR EM QUALQUER POSIÇÃO
    def insert(self, index, elem):
        last = self.head
        no = No(elem)
        pos = index - 1
        pos = int(pos)
        if pos == 0:
            no.set_proximo(self.head)
            self.head = no
            print(f'Elemento adicionado na primeira posição: {self.head}')
            self.size += 1
        elif pos > self.size:
            print(f'A posição {index}, não existe.')
            answer = input('Deseja adicionar no final da lista? [S/N] ')
            if answer == 'S':
                while last.get_proximo():
                    last = last.get_proximo()
                last.next = No(elem)
                self.size += 1
                print(f'Elemento: {elem} adicionado ao final da lista.')
            else:
                print('OKAY')
        else:
            pointer = self._getnode(pos-1)
            no = No(elem)
            aux = pointer.get_proximo()
            no.set_proximo(aux)
            pointer.set_proximo(no)
            print(f'Elemento: {elem} adicionado na posição {pos + 1}')
            self.size += 1

    # MÉTODO PARA REMOVER
    '''def remove(self, elem):
        if self.head == None:
            print('Lista está vazia, não há elementos para serem removidos.')
        elif self.head.get_dado() == elem:
            self.head = self.head.get_proximo()
            print(f'{elem} removido da lista')
            self.size -= 1
        else:
            antecessor = self.head
            pointer = self.head.get_proximo()
            while pointer is not None:
                if pointer.get_dado() == elem:
                    antecessor.set_proximo(pointer.get_proximo())
                    pointer.set_proximo(None)
                antecessor = pointer
                pointer = pointer.get_proximo()
            print(f'{elem} removido da lista')
            self.size -= 1'''

    # MÉTODO PARA REMOVER POR POSIÇÃO
    def removeByIndex(self, pos):
        pos = pos - 1
        if self.head == None:
            print('Lista está vazia, não há elementos para serem removidos.')
        elif pos == 0:
            aux = self.head
            self.head = aux.get_proximo()
            print('Elemento da posição  removido.')
            self.size -= 1
        else:
            pointer = self._getnode(pos-1)
            aux = pointer.get_proximo()
            bah = aux.get_proximo()
            pointer.set_proximo(bah)
            print(f'Elemento {aux} removido da posição {pos}.')

    # MÉTODO PARA VERIFICAR SE LISTA ESTÁ VAZIA
    def isEmpty(self):
        return self.start is None

    # MÉTODO PARA VERIFICAR O TAMANHO DA LISTA EM NÚMERO DE ELEMENTOS
    def Tamanho(self):
        if self.size == 1:
            return "Lista possui apenas um elemento."
        elif self.size == 0:
            return "Lista está vazia"
        else:
            return f'Lista possui {self.size} elementos.'

    # MÉTODO PARA BUSCAR POR POSIÇÃO.
    def BuscaByIndex(self, index):
        pointer = self._getnode(index-1)
        if pointer:
            aux = pointer.get_dado()
            print(f'Elemento da posição {index}: {aux}')
        else:
            print(f'Não há elemento na posição informada {index}.')

    # MÉTODO PARA LISTAR
    def Listando(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.get_dado()) + " ->"
            pointer = pointer.get_proximo()
        print(f'{r}',end=' ')

    def __str__(self):
        return self.Listando()

    def BuscaNome(self, nome):
        aux = self.head
        i = 1
        while (aux and aux.get_dado().nome != nome):
            aux = aux.get_proximo()
            i += 1

        if (aux != None):
            print(f'Item encontrado com o nome desejado: {aux} na posição {i}.')
        else:
            print(f'Item {nome} não encontrado!')

        # BUSCA POR ANO DE LANÇAMENTO:

    def BuscaAno(self, ano):
        aux = self.head
        i = 1
        while (aux and aux.get_dado().ano != ano):
            aux = aux.get_proximo()
            i += 1

        if (aux != None):
            print(f'Item encontrado com o ano desejado: {aux} na posição {i}.')
        else:
            print(f'Item {ano} não encontrado!')

        # BUSCA POR PRODUTORA:

    def BuscaProdutora(self, produtora):
        aux = self.head
        i = 1
        while (aux and aux.get_dado().produtora != produtora):
            aux = aux.get_proximo()
            i += 1

        if (aux != None):
            print(f'Item encontrado com a produtora desejada: {aux} na posição {i}.')
        else:
            print(f'Item {produtora} não encontrado!')