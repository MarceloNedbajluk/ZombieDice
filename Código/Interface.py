import os

class Interface:

    def _limpar_tela(self):

        os.system("cls")

    def _tela_continuar(self):

        input('Pressione Enter para continuar\n')

class Interface_Jogo (Interface):

    def __limpar_tela(self):

        super()._limpar_tela()

    def __tela_continuar(self):

        super()._tela_continuar()

    def __opcao_sair(self):

        print (f'{0:<0}{"SAIR":^30}')

    def __opcao_voltar(self):

        print (f'{0:<0}{"VOLTAR":^30}')

    def tela_inicial(self):
        #Interface inicial do jogo para o usuário
        self.__limpar_tela()
        #inicia a variável que irá captar as respostas do usuário
        resposta = -1
        #centralizar
        #inicia a lista que conterá as strings que serão apresentadas na tela
        opcao = []
        #adciona as strings dentro da lista opção
        opcao.append(f'INICIAR')
        opcao.append(f'DIFICULDADE')
        opcao.append(f'INSTRUÇÕES')

        #estrutura while que repete enquanto a reposta é inválida
        #quando a resposta for válida, ela é retornada pela função
        while resposta < 0 or resposta > len(opcao):
            #estrutura For para imprimir as opções ao usuáio
            for indice in range(0,len(opcao)):

                    print (f'{indice+1:<0}{opcao[indice]:^30}')

            self.__opcao_sair()

            try:

                resposta = int(input())

                if resposta < 0 or resposta > len(opcao):
                    print("Opção inválida.\n")
                else:
                    return resposta
                    break

            except:

                print('Caracter inválido.\n')

            self.__tela_continuar()


    def tela_dificuldade(self):
        #inicia a variável que conterá as strings a serem impressas
        niveis_dificuldade = []
        #adiciona as strings à lista
        niveis_dificuldade.append('Muito fácil')
        niveis_dificuldade.append('Fácil')
        niveis_dificuldade.append('Intermediário')
        niveis_dificuldade.append('Difícil')
        niveis_dificuldade.append('Muito Difícil')
        #inicia a variável que conterá a resposta
        resposta = -1
        #itera enquanto a resposta for inválida
        while (resposta < 0 or resposta > len(niveis_dificuldade)):
            self.__limpar_tela()
            #imprime as strings na estrutura For
            print(f'Selecione o nível de dificuldade:\n')

            for item in range(0,len(niveis_dificuldade)):

                print(f'{item+1:<0}{niveis_dificuldade[item]:^30}')

            print('\n')
            self.__opcao_voltar()
            try:

                resposta = int(input())
                if resposta < 0 or resposta > len(niveis_dificuldade):
                    print("Resposta inválida.\n")
                    self.__limpar_tela()
                else:
                    return resposta

            except:

                print("Caracter inválido.\n")

    def tela_instrucoes(self):
        self.__limpar_tela()
        print('Você sorteará três dados e, em seguida, os lançará. Caso possua dados com a face PASSOS de jogada anterior, eles serão contabilizados para a soma dos três dados e serão lançados novamente.\n\n')
        print('Lembre-se de que:\n\nOs dados verdes possuem uma quantidade maior de faces tipo Cérebro...\n\nOs dados vermelhos estão repletos de tiros!\n\nOs amarelos, por fim, são balanceados.')
        #   mais instruções aqui...
        print('\n')
        self.__tela_continuar()

    def tela_quantidade_jogadores(self):
        #   itera tentativas de alimentar a var quantidadeJogadores disparando mensagens
        #   ao usuário para indicar onde está o erro, se houver.
        resposta = -1
        while resposta < 2 or resposta > 6:
            self.__limpar_tela()
            try:

                resposta = int(input(f'Qual é a quantidade de jogadores (entre 2 e 6)?\n'))

                if resposta < 2 or resposta > 6:

                    print("Quantidade inválida.\n")

                else:

                    return resposta
                    break

            except:

                print("Caracter inválido!\n")

    def tela_nome(self, indice:int):
        while True:

            self.__limpar_tela()
            try:

                resposta = str(input(f'Qual é o nome do {indice}º zumbi?\n'))
                return resposta
                break

            except:

                print('O nome deve ser composto por letras.')
                self.__tela_continuar()

class Interface_Rodada(Interface):

    def __limpar_tela(self):

        super()._limpar_tela()

    def __tela_continuar(self):

        super()._tela_continuar()

    def frase_apos_sorteio(self, nome: str):
        self.__limpar_tela()
        #   imprime a frase indicando quem começará o jogo
        print(f'\n{str.upper(nome)}, você começará a caçada por cérebros!!!\n')
        self.__tela_continuar()
        self.__limpar_tela()

    def tela_empate(self):

        print ("Os zumbis ...")

    def tela_ranking_rodada(self, ranking:list):

        self.__limpar_tela()

        print('PLACAR DA RODADA')

        for nome, pontuacao in ranking:

            print(f'{str.upper(nome)}: {pontuacao}')

        self.__tela_continuar()

    def tela_ranking_final(self, ranking:list):

        self.__limpar_tela()
        print('PLACAR FINAL')

        i = 1
        for nome, pontuacao in ranking:

            print(f'{i}° - {str.upper(nome)}: {pontuacao}')
            i += 1

        self.__tela_continuar()

class Interface_Turno(Interface):

    def __limpar_tela(self):

        super()._limpar_tela()

    def __tela_continuar(self):

        super()._tela_continuar()

    def tela_jogar_novamente(self, cerebros: int, tiros: int, passos: int):
        # procedimento que pergunda ao jogador se ele deseja continuar o turno e retorna um valor booleano
        # inicializa a variável reposta
        resposta = ''
        # define as constantes que representam as respostas possíveis
        SIM = "S"
        NAO = "N"
        # define a constante que mensagem que será disparada em caso de erro ou dígito inválido
        MSG_ERRO = "Digite somente as letras " + SIM + " ou " + NAO + "."+'\n'
        # itera enquanto a resposata for diferente das constantes admitidas
        while not((resposta == SIM) or (resposta == NAO)):
            self.__limpar_tela()
            # printa o status do turno para o jogador
            print(f"Até aqui você tem {cerebros} cérebros, {tiros} tiros e {len(passos)} passos!")
            try:
                resposta = (input(f"Deseja continuar? " + SIM + "/" + NAO + "\n"))
            except:
                print(MSG_ERRO)
            # converte a respostas para maiúsculo
            resposta = str.upper(resposta)
            if not(resposta == SIM or resposta == NAO):
                print(MSG_ERRO)
                self.__tela_continuar()
        # retorna valor booleano de acordo com a resposta fornecida
        if resposta == NAO:
            return False
        else:
            return True

    def tela_passo(self,indice:int):

        print(f'Sua {indice}° vítima fugiu!')
        self.__tela_continuar()

    def tela_tiro(self,indice:int):

        print(f'Sua {indice}° vítima atirou em você!')
        self.__tela_continuar()

    def tela_cerebro(self,indice:int):

        print(f'Sua {indice}° vítima sucumbiu!')
        self.__tela_continuar()

    def tela_tres_tiros(self):

        print(f'{"Você levo três tiros...":^30}\n{"E perdeu os cérebros que havia conseguido neste turno!":^30}\n')
        self._tela_continuar()

    def tela_inicio(self, nome:str):

        self.__limpar_tela()
        print(f'{str.upper(nome)}, é a sua vez!\n')
        self.__tela_continuar()

    def tela_dados_no_pote(self, quantidade:int):

        if quantidade > 1:
            d = "dados"
        else:
            d = "dado"

        self.__limpar_tela()
        print(f'Há {quantidade} {d} no pote.')
        self._tela_tirar_dados()

    def _tela_tirar_dados(self):

        input('Pressione Enter para tirar os dados\n')

    def _tela_lancar_dados(self):

        self.__limpar_tela()
        input('Pressione Enter para lançar os dados\n')

    def tela_escolher_vitima(self):

        self.__limpar_tela()
        input('Prepare-se para escolher suas vítimas!')

    def tela_informar_dado_lancado(self,indice:int,cor:str):

        self.__limpar_tela()
        print(f'O {indice}° dado é {cor}\n')
        self._tela_continuar()

    def tela_dados_tirados(self, lista:list):

        self.__limpar_tela()
        print(f'Seus dados:\n{lista[0][0]}: {lista[0][1]}\n{lista[1][0]}: {lista[1][1]}\n{lista[2][0]}: {lista[2][1]}\n\n')
        self.__tela_continuar()

    def tela_saldo_remanescente(self, lista:list):

        self.__limpar_tela()
        print(f'Seu saldo da jogada anterior:\n{lista[0][0]}: {lista[0][1]}\n{lista[1][0]}: {lista[1][1]}\n{lista[2][0]}: {lista[2][1]}\n\n')
        self.__tela_continuar()

    def tela_empate(self, * nome):
        pass
