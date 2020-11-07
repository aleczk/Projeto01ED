from node import Node
from modulo.exception import Exception


class ListaEncadeada:
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, no):
        self.__head = no

    def vazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def buscar(self, busca):
        ponteiro = self.head

        while ponteiro != None:
            if ponteiro.data.banda == busca:
                return ponteiro.data

            ponteiro = ponteiro.next

        raise 'Dado não encontrado'

    def elemento(self, posicao):
        try:
            assert posicao > 0

            if self.vazia():
                raise Exception('A lista está vazia')

            ponteiro = self.__head
            contador = 1

            # Andar na lista
            while ponteiro != None and contador < posicao:
                ponteiro = ponteiro.next
                contador += 1

            # Posição encontrada
            if ponteiro != None:
                return ponteiro.data

            raise Exception('A posição é inválida')

        except TypeError:
            raise Exception('A posição deve ser um valor inteiro')
        except AssertionError:
            raise Exception('Posição negativa não é válida')
        except:
            raise

    def inserir(self, posicao, data):
        try:
            assert posicao > 0

            # CONDIÇÃO 1: Inserção se a lista estiver vazia
            if self.vazia():
                if posicao != 1:
                    raise Exception(
                        'A lista está vazia. Só poderá ser inserido na posição 1')

                self.__head = Node(data)
                self.__tamanho += 1
                return

            # CONDIÇÃO 2: Inserção na primeira posição em uma lista não vazia
            if posicao == 1:
                novo = Node(data)
                novo.next = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDIÇÃO 3: Inserção após a primeira posição em uma lista não vazia
            p = self.__head
            contador = 1

            while (contador < posicao-1) and (p != None):
                p = p.next
                contador += 1

            if p == None:
                raise Exception('A posição é inválida para inserção')

            novo = Node(data)
            novo.next = p.next
            p.next = novo
            self.__tamanho += 1

        except TypeError:
            raise Exception('A posição deve ser um valor inteiro')
        except AssertionError:
            raise Exception('Posição negativa não é válida')
        except:
            raise

    def remover(self, posicao):
        try:
            assert posicao > 0

            if self.vazia():
                raise Exception('Lista vazia. Não é possível remover elementos')

            p = self.__head
            contador = 1

            while (contador <= posicao - 1) and (p != None):
                anterior = p
                p = p.next
                contador += 1

            if p == None:
                raise Exception('Posição inválida para remoção')

            if posicao == 1:
                self.__head = p.next

            else:
                anterior.next = p.next
            
            self.__tamanho -= 1

        except TypeError:
            raise Exception('A posição deve ser um valor inteiro')
        except AssertionError:
            raise Exception('Posição negativa não é válida')
        except:
            raise

    def __str__(self):
        saida = 'Lista: \n'
        p = self.__head

        while p != None:
            saida += f'{p.data}'
            p = p.next
        
        # saida += "]"
        return saida

    def imprimir(self):
        print(self.__str__())

    def modificar(self, posicao, novoValor):
        try:
            assert posicao > 0

            if self.vazia():
                raise Exception(
                    'Lista vazia. Não é possível remover elementos')

            p = self.__head
            contador = 1

            while (p != None) and (contador < posicao):
                p = p.next
                contador += 1

            if p != None:
                p.data = novoValor
                return

            raise Exception('Posição inválida para a lista')

        except TypeError:
            raise Exception('A posição deve ser um valor inteiro')
        except AssertionError:
            raise Exception('Posição negativa não é válida')
        except:
            raise

    def ordena(self):
        for i in range(self.__tamanho-1):
            curr = self.__head
            nxt = curr.next
            prev = None
            while nxt:
                if curr.data.ano > nxt.data.ano:
                    if prev == None:
                        prev = curr.next
                        nxt = nxt.next
                        prev.next = curr
                        curr.next = nxt
                        self.head = prev
                    else:
                        temp = nxt
                        nxt = nxt.next
                        prev.next = curr.next
                        prev = temp
                        temp.next = curr
                        curr.next = nxt
                else:
                    prev = curr
                    curr = nxt
                    nxt = nxt.next
            i = i+1
