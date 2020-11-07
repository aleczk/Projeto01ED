from node import Node
from modulo.exception import Exception


class FilaEncadeada:
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__tamanho = 0

  def vazia(self):
      return self.__tamanho == 0

  def tamanho(self):
    return self.__tamanho

  def inserir(self, NovoDado):
    node = Node(NovoDado)
    if self.__head is None:
      self.__head = node
      self.__tail = node
    else:
      self.__tail.next = node
      self.__tail = node

    self.__tamanho += 1

  def remover(self):
    if self.vazia():
      raise Exception('A fila está vazia.')
    
    self.__head = self.__head.next
    self.__tamanho -= 1
  
  def elemento(self):
    if(self.vazia()):
        raise Exception('A fila está vazia')
    return self.__head.data
  
  def __str__(self):
    saida = 'Fila:\n'
    p = self.__head

    while p != None:
      saida += f'{p.data}'
      p = p.next
    
    # saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())