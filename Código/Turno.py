import copy
import random
from Dado import *
from collections import namedtuple
from Interface import Interface_Turno

class Turno:

    def __init__(self):
        # ao instanciar a classe, as variáveis são iniciadas
        # lista que armazena todos os dados ao começo do turno
        self.dadosTurno = []
        # lista que armazena os três dados utilizados na jogada
        self.dadosDaVez = []
        # lista que armazena somente os dados tirados com a face Passos
        self.dadosPassos = []
        # lista que armazena todos os dados já tirados
        self.dadosJaTirados = []
        # lista que controla o índice dos dados com face Passos
        self.indice_passos = []
        # variáveis que controlam a pontuação do turno
        self.tiros = 0
        self.cerebros = 0
        #variável que fornece, a partir de Dado, os valores das faces dos dados
        dado_generico=Dado("","",1)
        #vairáveis de Turno são informadas
        self.const_tiro = dado_generico.face_tiro
        self.const_passo = dado_generico.face_passos
        self.const_cerebro = dado_generico.face_cerebro
        self.const_cor_facil= dado_generico.cor_dado_facil
        self.const_cor_intermediario= dado_generico.cor_dado_intermediario
        self.const_cor_dificil= dado_generico.cor_dado_dificil
        #destrói a variável
        del dado_generico
        self.__interface = Interface_Turno()
        # variável que controlará a continuidade do turno
        self._encerrarTurno = False

    def iniciar_turno(self, dados_passagem: list, nome:str):
        # interface pela qual a Rodada inicia um novo turno
        # os dados fornecidos pela Rodada são copiados para uma lista da classe
        self.dadosTurno = copy.deepcopy(dados_passagem)
        #   tela que antecipa o lançamento de dados
        self.__interface.tela_inicio(nome)
        # itera enquanto a variável de controle for falsa
        while self._encerrarTurno == False:
            #  tela para tirar dados
            self.__interface.tela_escolher_vitima()
            #  tira a quantidade (dados-passos)
            self._tirar_dados()
            #   tela para informar ao usuário quais foram os dados tirados
            self.__interface.tela_dados_tirados(self._dados_por_cor())
            #   iteração para lançar e conferir os dados da vez
            for self.dadoAtual in self.dadosDaVez:
                #  tela para expor ao usuário qual dado será lançado
                self.__interface.tela_informar_dado_lancado(self.dadosDaVez.index(self.dadoAtual)+1,self.dadoAtual.cor)
                #  lança e confere cada dado na lista de dados tirados
                self._confere_face(self.dadoAtual.lancar(), self.dadosDaVez.index(self.dadoAtual) + 1)
                if self._encerrarTurno == True:
                    break
            # verifica se o turno será encerrado
            if self._encerrarTurno == False:
                # imprime a pergunta para o jogador e, se preferir continuar...
                if self.__interface.tela_jogar_novamente(self.cerebros,self.tiros, self.indice_passos):
                    # dá início à rotina de organização dos dados
                    self._organiza_dados()
                    # tela que informa o saldo de dados oriundos da jogada anterior
                    self.__interface.tela_saldo_remanescente(self._dados_por_cor())
                else:
                    # senão, encerra o turno
                    self._encerrarTurno = True
        # quando ocorre a saída do loop controlado pela variável encerrarTurno, ocorre o retorno do cerebros acumulados
        return self.cerebros

    def _tirar_dados(self):
        # realiza o sorteio de um dado na variável dadosTurno e transfere para dadosDaVez
        # a quantidade é (3 - dadosDaVez), pois esta lista pode ser não vazia dada a presença
        # de dado tirados com a face Passos em jogadas anteriores
        self.__interface.tela_dados_no_pote(len(self.dadosTurno))
        teto = 3 - len(self.dadosDaVez)
        for indiceTirados in range(0, teto):
            if len(self.dadosTurno) > 0:
                dadoSorteado = random.choice(self.dadosTurno)
            else:
                # se len(self.dadosTurno) < dados para completar 3, é preciso tirar os dados de outro lugar;
                dadoSorteado = random.choice(self.dadosJaTirados)
                # se os dadosTurno terminaram, o turno também encerra
                self._encerrarTurno = True
            # transfere o dado de uma lista para outra
            # da esquerda para a direita:
            # o método index fornece o índice do dadoSorteado dentro da lista dadosTurno
            # o índice é utilizado como parâmetro para pop saber qual será o objeto
            # retirado de dadosTurno e apanhado pelo método append de dadosDaVez
            self.dadosDaVez.append(self.dadosTurno.pop(self.dadosTurno.index(dadoSorteado)))

    def _confere_face(self, face: str, idx_vitima:int):

        if face == self.const_cerebro:
            self.cerebros += 1
            self.__interface.tela_cerebro(idx_vitima)

        elif face == self.const_passo:
            # se a face for Passos, o índice do dado em dadosJaTirados é armanado para que, ao final da jogada, ele seja
            # armazenado em outra lista
            self.indice_passos.append(self.dadoAtual.id)
            self.__interface.tela_passo(idx_vitima)

        elif face == self.const_tiro:
            self.__interface.tela_tiro(idx_vitima)
            self.tiros += 1
            if self.tiros == 3:
                self._encerrarTurno = True
                self.cerebros = 0
                self.__interface.tela_tres_tiros()

    def _organiza_dados(self):
        #PROBLEMA: AO ITERAR DADOS DA VEZ COM DADO, QUANDO ALGUM OBJETO É EXTRAÍDO DE DADOS DA VEZ, A CONTAGEM FICA ATRAPALHADA
        # lista que receberá o valor booleano a fim de controlar a transferência dos dados
        # o primeiro passo é verificar se ocorreram dados com a face Passos; se sim, seus índices são identificados
        # para que permaneçam em DadosDaVez
        if len(self.indice_passos) > 0:
            i = 0
            continua = True
            while continua:

                if i == len(self.dadosDaVez) - 1:
                    continua = False

                if self.indice_passos.__contains__(self.dadosDaVez[i].id):
                    i += 1

                else:
                    self.dadosJaTirados.append(self.dadosDaVez.pop(i))

            self.indice_passos.clear()

        else:

            for repete in range(0,len(self.dadosDaVez)):

                self.dadosJaTirados.append(self.dadosDaVez.pop(0))

    def _dados_por_cor(self):
        verde = 0
        amarelo = 0
        vermelho = 0
        # a iteração percorre todos os dados da lista e confere as cores
        for dado in self.dadosDaVez:
            if str.upper(dado.cor) == str.upper(self.const_cor_facil):
                verde+=1
            elif str.upper(dado.cor) == str.upper(self.const_cor_intermediario):
                amarelo+=1
            elif str.upper(dado.cor) == str.upper(self.const_cor_dificil):
                vermelho+=1
        # organiza os dados em tuplas
        tupla_cor1 = (self.const_cor_facil, verde)
        tupla_cor2 = (self.const_cor_intermediario, amarelo)
        tupla_cor3 = (self.const_cor_dificil, vermelho)
        # organiza as tuplas em lista
        retorno = [tupla_cor1,tupla_cor2,tupla_cor3]
        # retorna a lista
        return retorno

