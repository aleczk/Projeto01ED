class Musica:
    def __init__(self, colocacao, nome, banda, compositor, ano):
        self.__colocacao = colocacao
        self.__nome = nome
        self.__banda = banda
        self.__ano = ano
        self.__compositor = compositor
    
    @property
    def colocacao(self):
        return self.__colocacao

    @colocacao.setter
    def colocacao(self, novaColocacao):
        self.__colocacao = novaColocacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def banda(self):
        return self.__banda

    @banda.setter
    def banda(self, novaBanda):
        self.__nome = novaBanda
    
    @property
    def compositor(self):
        return self.__compositor

    @compositor.setter
    def compositor(self, novoCompositor):
        self.__compositor = novoCompositor
        
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno


    def __repr__(self):
        return f'[{self.__colocacao}, {self.__nome}, {self.__banda}, {self.__compositor}, {self.__ano}]\n'
