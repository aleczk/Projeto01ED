class FilaException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)


class Node:
  def __init__(self, date):
    self.__date = date
    self.__next = None
  
  # get
  @property
  def date(self):
    return self.__date
  
  # set
  @date.setter
  def date(self, newDate):
    self.__date = newDate

  # get
  @property
  def next(self):
    return self.__next
  
  # set
  @next.setter
  def next(self, newDate):
    self.__next = newDate

class FilaEncadeada:
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
      if self.vazia():
        raise FilaException('A fila está vazia')

      return self.__head

  def vazia(self):
    return self.__size == 0
  
  def size(self):
    return self.__size
  
  def inserir(self, date):
    createNode = Node(date)
    if self.vazia():
      self.__head = createNode
      self.__tail = createNode        
    
    self.__tail.next = createNode
    self.__tail = createNode 
    self.__size +=1 
     

  def remover(self):
    if self.vazia():
      raise FilaException('A fila está vazia')

    self.__head = self.__head.next
    self.__size -=1 
    return

     
  def __str__(self):
    saida = 'Fila: ['
    p = self.__head

    while p != None:
      saida += f'{p.date}'
      p = p.next

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())
  

if __name__ == '__main__':
  f1 = FilaEncadeada()

  f1.inserir(10)
  f1.inserir(20)
  f1.inserir(30)
  f1.inserir(40)
  print(f1)
  f1.remover()
  print(f1)
  f1.remover()
  print(f1)



