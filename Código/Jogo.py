from Jogador import Jogador
from Rodada import Rodada
from Interface_Grafica import Interface_Jogo
class Jogo:

    def __init__ (self):
        #Valor default da dificuldade
        self.dificuldade = 3
        self.quantidadeJogadores = 0
        self.jogadores = []
        resposta = -1
        self.interface = Interface_Jogo()
        #Assim que a variável é inicializada, ocorre a chamada da função tela_inicial em que
        #é possível definir a dificuldade, iniciar o jogo ou fechar a aplicação

        while True:
            resposta = self.interface.tela_inicial()
            #resposta = self.tela_inicial()
            #Se a resposta for 1, chama o procedimento iniciar_jogo
            if resposta == 1:

                self.iniciar_jogo()

            #Se a resposta for 2, a variável dificuldade receberá o retorno da função
            #tela_dificuldade
            elif resposta == 2:

                self.dificuldade = self.interface.tela_dificuldade()

            elif resposta == 3:

                self.interface.tela_instrucoes()

            elif resposta == 0:

                exit()

    def iniciar_jogo(self):
        #   O procedimento iniciar_jogo começa pela definição da quantidade de jogadores
        self.definir_jogadores()
        #   E, em seguida, chama o construtor de Rodada passando como parâmetro
        #   a dificuldade e a lista de jogadores
        r = Rodada(self.dificuldade)
        r.iniciar_rodada(self.jogadores)

        del r
        del self.jogadores

    def definir_jogadores(self):
        #   itera tentativas de alimentar a var quantidadeJogadores disparando mensagens
        #   ao usuário para indicar onde está o erro, se houver.
        self.quantidadeJogadores = self.interface.tela_quantidade_jogadores()
        #   quantidadeJogadores controla as iterações do For enquanto este instancia
        #   objetos de Jogador dentro da lista
        for indice in range(1,self.quantidadeJogadores + 1):

            nome = self.interface.tela_nome(indice)
            #   INSERIR procedimento para verificar se o nome já foi cadastrado
            self.jogadores.append(Jogador(nome))

    def opcao_sair(self):

        print (f'{0:<0}{"SAIR":^30}')

    def opcao_voltar(self):

        print (f'{0:<0}{"VOLTAR":^30}')



