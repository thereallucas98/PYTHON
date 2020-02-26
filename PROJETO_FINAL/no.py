class No:
    def __init__(self, dado = None, next = None):
        self.dado = dado
        self.next = next

    def get_dado(self):
        return self.dado

    def set_dado(self, novoDado):
        self.dado = novoDado

    def get_proximo(self):
        return self.next

    def set_proximo(self, nexto):
        self.next = nexto

    def __str__(self):
        return f'{self.dado}'





