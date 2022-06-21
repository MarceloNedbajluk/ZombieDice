from Dado import Dado_Verde, Dado_Vermelho, Dado_Amarelo
from Turno import Turno
from collections import namedtuple
import random
from Interface_Grafica import Interface_Rodada

class Rodada:

    def __init__(self, dificuldade: int):
        #   inicia o objeto tomando como parâmetro a dificuldade definida anteriormente
        #   e a lista de jogadores, também criada em Jogo
        #   inicia as listas que serão utilizadas dentro da classe
        self.__dados = []
        self.ranking = []
        #   inicia o dicionário que armazenará o par nome/pontuação
        self.placar = {}
        #   função que instanciará os dados dentro da lista de dados
        self.__criar_dados(dificuldade)
        self.__interface = Interface_Rodada()

    def iniciar_rodada(self, jogadores: list):
        #   procediemnto que dará início à rodada
        self.jogadores_do_turno = jogadores
        #   informa os nomes dos jogadores ao placar
        self.__inicia_placar()
        #   inica a variável que controlará a continuidade do procedimento iniciar_rodada
        encerraRodada = False
        #   variável indiceJogador recebe o retorno da função que sorteará o primeiro jogador
        self.indiceJogador = self.__sortear_primeiro_jogador(len(self.jogadores_do_turno))
        #   função que imprime a frase com o nome do jogador sorteado
        self.__interface.frase_apos_sorteio(self.jogadores_do_turno[self.indiceJogador].nome)
        #   itera enquanto a variável de controle é negativa
        while encerraRodada == False:
            #   inicia um novo ciclo
            #   indiceTurno = 0
            for indiceTurno in range(1,len(jogadores)+1):
                novoTuno = Turno()
                #   inicia o turno com o jogador
                self.jogadores_do_turno[self.indiceJogador].soma_pontos(novoTuno.iniciar_turno(self.__dados, self.jogadores_do_turno[self.indiceJogador].nome))
                #   destrói a variável
                del novoTuno
                #   soma a pontuação atualizada do jogador do turno ao placar
                self.placar[self.jogadores_do_turno[self.indiceJogador].nome] = self.jogadores_do_turno[self.indiceJogador].cerebros
                #   verifica se o índice do jogador, incrementado em +1, é menor que total de jogadores
                if self.indiceJogador + 1 <= len(self.jogadores_do_turno) - 1:
                    self.indiceJogador += 1
                #   se for igual, ele é zerado
                else:
                    self.indiceJogador = 0
            #   procedimento para verificar se há vencedor ou empate após o término do ciclo
            encerraRodada = self.__conferir_pontuacao()
            #   se a rodada for continuar, imprime o placar da rodada na tela
            if encerraRodada == False:

                self.__interface.tela_ranking_rodada(sorted(self.placar.items(), key=lambda Linha: Linha[1], reverse=True))

        #   imprime o ranking na tela
        self.__interface.tela_ranking_final(sorted(self.ranking, key=lambda Linha: Linha[1], reverse= True))
        #   limpa a lista de dados
        del self.__dados

    def __criar_dados(self, dificuldade: int):
        #   define a quantidade de cada tipo de dado de acordo com o nível de dificulade
        if dificuldade == 1:

            quantidadeVerde = 8
            quantidadeAmarelo = 3
            quantidadeVermelho = 2

        elif dificuldade == 2:

            quantidadeVerde = 6
            quantidadeAmarelo = 4
            quantidadeVermelho = 3

        elif dificuldade == 3:

            quantidadeVerde = 4
            quantidadeAmarelo = 5
            quantidadeVermelho = 4

        elif dificuldade == 4:

            quantidadeVerde = 3
            quantidadeAmarelo = 4
            quantidadeVermelho = 6

        elif dificuldade == 5:

            quantidadeVerde = 2
            quantidadeAmarelo = 3
            quantidadeVermelho = 8

        #   instancia a quantidade definida de dados
        indice_id = 0
        for indice in range(0, quantidadeVerde):
            self.__dados.append(Dado_Verde(indice_id))
            indice_id+=1

        for indice in range(0, quantidadeAmarelo):
            self.__dados.append(Dado_Amarelo(indice_id))
            indice_id+=1

        for indice in range(0, quantidadeVermelho):
            self.__dados.append(Dado_Vermelho(indice_id))
            indice_id+=1

    def __inicia_placar(self):
        #   itera a lista de jogadores do turno
        for jogador in self.jogadores_do_turno:
            #   acrescenta o nome do jogador ao dicionário como uma chave e o valor padrão 0
            self.placar.setdefault(jogador.nome, 0)

    def __sortear_primeiro_jogador(self, totalJogadores: int):
        #   inicia a variável que conterá a lista que estão os índices dos jogadores a srem sorteados
        sorteia = []
        #   adiciona os valores que representarão o índice dos jogadores na variável sorteia
        for i in range(0, totalJogadores):
            sorteia.append(i)
        #   retorna o valor obtido com choice
        return random.choice(sorteia)

    def __conferir_pontuacao(self):
        #   inicializa a lista que armazenerá os valores iguais ou maiores que 13
        treze_ou_mais = []
        #   itera a lista de jogadores
        for i in range(0,len(self.jogadores_do_turno)):
            #   se o jogador tem 13 ou mais cérebros
            if self.jogadores_do_turno[i].cerebros >= 13:
                #   a quantidade que possui é registrada na lista
                treze_ou_mais.append(self.jogadores_do_turno[i].cerebros)
        #   após a coleta de dados ocorre a análise
        #   se a lista for fazia, a função será falsa
        if len(treze_ou_mais) == 0:
            return False

        #   se a lista contiver apenas um membro, ocorrerá
        #   o ranqueamento e a função retornará True
        elif len(treze_ou_mais) == 1:
            self.__rankear_jogadores(False, 0)
            return True

        #   se a lista contiver mais que um membro, ocorrerá
        #   seu ordenamento decrescente e a comparação entre
        #   os valores das duas primeiras posições; caso sejam
        #   iguais, chama o ranqueamento informando a posição
        #   em que houve empate e retorna False, senão, chama
        #   o ranqueamento e retorna True.
        elif len(treze_ou_mais) > 1:
            treze_ou_mais = sorted(treze_ou_mais, reverse = True)
            if treze_ou_mais[0] == treze_ou_mais[1]:
                self.__rankear_jogadores(True, treze_ou_mais[0])
                return False
            else:
                self.__rankear_jogadores(False, 0)
                return True

    def __rankear_jogadores(self, empate:bool, pontuacao_empate:int):
        #   nomeia a tupla Linha
        Linha = namedtuple("Linha", ["nome", "pontuacao"])
        #   variável para acessar o índice do jogador
        i = 0
        #   vairável que controla a iteração
        continua = True
        #   itera a lista de jogadores do turno
        while continua:
            #   confere se a iteração chegou ao último item da lista
            if i == len(self.jogadores_do_turno) - 1:
                continua = False
            #   se empate for true e a pontuação do jogador for igual àquela em que houve o empate,
            #   não há preenchimento do ranking e o jogador permanece na lista
            if not (empate and self.jogadores_do_turno[i].cerebros == pontuacao_empate):
                #   acrescenta o nome e a pontuação do jogador ao ranking
                self.ranking.append(Linha(nome=self.jogadores_do_turno[i].nome, pontuacao=self.jogadores_do_turno[i].cerebros))
                #   remove o jogador da lista
                self.jogadores_do_turno.remove(self.jogadores_do_turno[i])
            else:
                i += 1
        #   ordena o ranking a partir da pontuação em ordem decrescente
        self.ranking = sorted(self.ranking, key= lambda Linha:Linha.pontuacao, reverse=True)


