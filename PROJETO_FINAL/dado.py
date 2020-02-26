class Dado:
    def __init__(self, nome, ano, produtora):
        self.nome = nome
        self.ano = ano
        self.produtora = produtora

    def get_nome(self):
        return self.nome

    def get_ano(self):
        return self.ano

    def get_produtora(self):
        return self.produtora

    def __str__(self):
        return f'\nTítulo: {self.nome} - Ano: {self.ano} - Produtora: {self.produtora}'