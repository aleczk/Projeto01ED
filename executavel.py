from listaEncadeada import ListaEncadeada
from pilhaEncadeada import PilhaEncadeada
from filaEncadeada import FilaEncadeada
from musica import Musica
from modulo.shutil import print_centralizado


if __name__ == "__main__":
    print()
    print_centralizado('Saudações da equipe COVID-19!')
    print_centralizado('Este programa trabalhará com as 100 maiores músicas brasileiras segundo a Rolling Stones Brasil.')
    print_centralizado('Para facilidade de visualização, com o uso da biblioteca panda só pegamos as 51 (uma boa ideia) primeiras músicas.')
    print_centralizado('Os dados da lista são, em ordem normal: Colocação no Ranking, Música, Banda ou Intérprete, Compositores e Ano.')
    input("\nPressione ENTER para iniciar...")
    
    print_centralizado('Início da classe Lista Encadeada.')
    print_centralizado('Serão ADICIONADOS todos os dados sobre as músicas a seguir.')
    input("\nPressione ENTER para continuar...")


############################### LISTA ENCADEADA
    lista = ListaEncadeada()

    with open("musicas.csv", "r", encoding="utf8") as arq:
        musicas = arq.readlines()
        for i in range(len(musicas)):
            colocacao, nome, banda, compositor, ano = musicas[i].split(";")
            ano = ano.strip("\n")
            musica = Musica(colocacao, nome, banda, compositor, ano)
            lista.inserir(i + 1, musica)
        print(lista)

    print_centralizado('Inserção completa. Próximo passo: REMOÇÃO.')
    print_centralizado('A remoção será feita, respectivamente, nas posicoes: 1, 51 e 5')
    input("\nPressione ENTER para continuar...")

    lista.remover(51)
    lista.remover(5)
    lista.remover(1)

    print(lista)

    print_centralizado('Remoção completa. Próximo passo: Checar se está vazio, caso não, imprimir o tamanho.')
    input("\nPressione ENTER para continuar...")

    if lista.vazia():
        print_centralizado('A lista está vazia.')
    else:
        print_centralizado(f'A lista possui tamanho: {lista.tamanho()}')
        print_centralizado('A lista NÃO está vazia')

    print_centralizado('Checagem completa. Próximo passo: MOSTRAR ELEMENTO')
    print_centralizado('Será mostrado o elemento 10')
    input("\nPressione ENTER para continuar...")

    print_centralizado(f'{lista.elemento(7)}')

    print_centralizado('Elemento mostrado. Próximo passo: ORDENAR')
    print_centralizado('A ordenação será feita pelo ano de lançamento')
    input("\nPressione ENTER para continuar...")

    lista.ordena()
    print(lista)

    print_centralizado('Elemento mostrado. Próximo passo: BUSCAR')
    print_centralizado('Serão buscadas as músicas do cantor Geraldo Vandré')
    input("\nPressione ENTER para continuar...\n")

    print_centralizado(f'{lista.buscar("Geraldo Vandré")}')

    print_centralizado('Busca feita. FIM DA LISTA ENCADEADA. Próximo passo: PILHA ENCADEADA')
    input("\nPressione ENTER para continuar...")

################################ PILHA ENCADEADA
    print_centralizado('Início da classe Pilha Encadeada.')
    print_centralizado('Serão ADICIONADOS os dados das primeiras 5 músicas.')
    input("\nPressione ENTER para continuar...")

    pilha = PilhaEncadeada()

    with open("musicas.csv", "r", encoding="utf8") as arq:
        musicas = arq.readlines()
        for i in range(5):
            colocacao, nome, banda, compositor, ano = musicas[i].split(";")
            ano = ano.strip("\n")
            musica = Musica(colocacao, nome, banda, compositor, ano)
            pilha.inserir(musica)
            print(pilha)
        

    print_centralizado('Inserção completa. Próximo passo: REMOÇÃO.')
    input("\nPressione ENTER para continuar...")

    for i in range(2):
        pilha.remover()
        print(pilha)
        i += 1

    print_centralizado('Remoção completa. Próximo passo: Checar se está vazio, caso não, imprimir o tamanho.')
    input("\nPressione ENTER para continuar...")

    if pilha.vazia():
        print_centralizado('A pilha está vazia.')
    else:
        print_centralizado(f'A pilha possui tamanho: {pilha.tamanho()}')
        print_centralizado('A pilha NÃO está vazia')

    print_centralizado('Checagem completa. Próximo passo: MOSTRAR ELEMENTO')
    input("\nPressione ENTER para continuar...\n")

    print_centralizado(f'{pilha.elemento()}')

    print_centralizado('Elemento mostrado. FIM DA PILHA ENCADEADA. Próximo passo: FILA ENCADEADA')
    input("\nPressione ENTER para continuar...")

################################ FILA ENCADEADA
    print_centralizado('Início da classe Fila Encadeada.')
    print_centralizado('Serão ADICIONADOS os dados das primeiras 10 músicas.')
    input("\nPressione ENTER para continuar...")

    fila = FilaEncadeada()

    with open("musicas.csv", "r", encoding="utf8") as arq:
        musicas = arq.readlines()
        print(fila)
        for i in range(10):
            colocacao, nome, banda, compositor, ano = musicas[i].split(";")
            ano = ano.strip("\n")
            musica = Musica(colocacao, nome, banda, compositor, ano)
            fila.inserir(musica)
            print(fila)
        

    print_centralizado('Inserção completa. Próximo passo: REMOÇÃO.')
    input("\nPressione ENTER para continuar...")

    for i in range(4):
        fila.remover()
        print(fila)
        i += 1

    print_centralizado('Remoção completa. Próximo passo: Checar se está vazio, caso não, imprimir o tamanho.')
    input("\nPressione ENTER para continuar...")

    if fila.vazia():
        print_centralizado('A fila está vazia.')
    else:
        print_centralizado(f'A fila possui tamanho: {fila.tamanho()}')
        print_centralizado('A fila NÃO está vazia')

    print_centralizado('Checagem completa. Próximo passo: MOSTRAR ELEMENTO')
    input("\nPressione ENTER para continuar...")

    print_centralizado(f'{fila.elemento()}')

    print_centralizado('Elemento mostrado. FIM DA FILA ENCADEADA\n')
    print_centralizado('FIM DO PROGRAMA!')
    input("\nPressione ENTER para ENCERRAR...")