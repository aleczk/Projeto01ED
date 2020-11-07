class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


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
        '''for i in range(self.__dados):
            if self.__dados[i] == dado:
                return i+1
        return None'''
        try:
            return self.__dados.index(dado) + 1
        except ValueError:
            raise ListaException(f'O valor {dado} não se encontra na lista')
        except:
            raise

    def elemento(self,posicao):
        #valor negativo:
        #posição invalida (IndexError)
        #posição com o tipo de dado diferente de Int TypeError
        try:
            assert posicao > 0 #Assegure que posição é maior que zero
            return self.__dados[posicao -1]
        except TypeError:
            raise ListaException('Passe um número inteiro para buscar na lista')
        except IndexError:
            raise ListaException('Essa posição não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise


    def inserir(self, posicao, dado):
        try:
            assert posicao > 0
            self.__dados.insert(posicao -1, dado)
        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')
        except IndexError:
            raise ListaException('Esse índice não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise


    def remover(self, posicao):
        try:
            assert posicao > 0
            if (self.vazia()):
                raise ListaException('Lista vazia. Não é possível remover elementos')
            valor = self.__dados[posicao-1]
            del self.__dados[posicao-1]
            return valor
        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')
        except IndexError:
            raise ListaException('Esse índice não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

    def modificar(self, posicao, novoValor):
        try:
            assert posicao > 0
            if (self.vazia()):
                raise ListaException('Lista vazia. Não é possível modificar elementos')
            self.__dados[posicao-1] = novoValor
            return True
        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')
        except IndexError:
            raise ListaException('Esse índice não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise        
            
            
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

#l1.inserir(-10,99)

try:
    #print(f'O indice do elemento que esta procurando se encontra na posição: {l1.busca(55)}')
    #print(l1.elemento(5))
    #l1.inserir(5,111)
    #print(l1)
    #l1.remover('1')
    l1.modificar(100,999)
    
except ListaException as li:
    print(li)