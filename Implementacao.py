class ListaSequencial:


    def __init__(self):
        self.__dados = []

    def vazia(self):
        return len(self.__dados) == 0

  # def cheia(self):
  #     pass

    def tamanho(self):
        return len(self.__dados)

    def busca(self, dado):
        for i in range(self.__dados):
            if self.__dados[i] == dado:
                return i+1

    def elemento(self,posicao):
        return self.__dados[posicao -1]

    def inserir(self, posicao, dado):
        self.__dados.insert(posicao -1, dado)

    def remover(self, posicao):
        if (self.vazia()):
            return None
        valor = self.__dados[posicao-1]
        del self.__dados[posicao-1]
        return valor

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

    def modificar(self, posicao, novoValor):
        if (self.vazia()):
            return False
        self.__dados[posicao-1] = novoValor
        return True
            
            
l1 = ListaSequencial()
if (l1.vazia()):
    print('lista vazia')

print('Tamanho: ', l1.tamanho())

for i in range(10):
    l1.inserir(1, i*10)
    print(l1)

print('Tamanho: ', l1.tamanho())

valorRemover = l1.remover(2)
print(valorRemover)
print(l1)

print()

l1.imprimir()

l1.modificar(3,7)

l1.imprimir()