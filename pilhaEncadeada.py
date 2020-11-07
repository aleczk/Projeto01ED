from node import Node
from modulo.exception import Exception


class PilhaEncadeada:
  def __init__(self):
    self.__head = None
    self.__tamanho = 0

  @property
  def head(self):
      if self.vazia():
        raise Exception('A pilha está vazia')

      return self.__head

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def inserir(self, data):
    no = Node(data)
    no.next = self.__head
    self.__head = no

    self.__tamanho += 1  

  def remover(self):
      if self.vazia():
        raise Exception('A pilha está vazia')

      self.__head = self.__head.next
      self.__tamanho -= 1  
  
  def elemento(self):
      if(self.vazia()):
          raise Exception('A pilha está vazia')
      return self.__head.data
  
  def __str__(self):
    saida = 'Pilha:\n'
    p = self.__head

    while p != None:
      saida += f'{p.data}'
      p = p.next
    
    # saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, novoValor):
      if self.vazia():
        raise Exception('A pilha está vazia')
      
      self.__head.data = novoValor