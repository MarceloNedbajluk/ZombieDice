import random
class Dado:
    # inicio_getters (constantes que representam as siglas de cada face)
    @property
    def face_tiro(self):
        self._TIR = "T"
        return self._TIR

    @property
    def face_passos(self):
        self._PAS = "P"
        return self._PAS

    @property
    def face_cerebro(self):
        self._CER = "C"
        return self._CER

    @property
    def cor_dado_facil(self):
        self._COR_1 = "verde"
        return self._COR_1

    @property
    def cor_dado_intermediario(self):
        self._COR_2 = "amarelo"
        return self._COR_2

    @property
    def cor_dado_dificil(self):
        self._COR_3 = "vermelho"
        return self._COR_3
    # fim_getters

    def __init__(self,faces:tuple, cor:str, id):
        # inicializa o objeto tomando as faces e a cor da classe filha e o id será a posição
        # que o objeto ocupa na conformação inicial da lista em que foi inserido
        self._faces = faces
        self._id = id
        self._cor = cor

    def lancar(self):
        # escolhe uma posição na string que compõe as faces do dado
        return random.choice(self._faces)

    #inicio_geters (para as propriedades de cada objeto)
    @property
    def id(self):
        return self._id

    @property
    def cor(self):
        return self._cor
    #fim_geters

# todas as classes filhas de Dado possuem a mesma estrutura apresentada a seguir
class Dado_Verde (Dado):
    # construtor da classe
    def __init__(self, id:int):
        # dispõe as faces dentro da tupla segundo o padrão comentado ao final da linha
        self.__facesVerde = (self.face_cerebro, self.face_passos, self.face_cerebro, self.face_tiro, self.face_passos, self.face_cerebro)# 'CPCTPC'
        # atribui a cor segundo a classe filha
        self.__cor = self.cor_dado_facil
        # sobreescreve a inicialização da superclasse
        super(Dado_Verde, self).__init__(self.__facesVerde,self.__cor,id)

    def lancar(self):
        # sobreescreve o método correspondente na superclasse
        return super(Dado_Verde, self).lancar()

class Dado_Amarelo (Dado):

    def __init__(self,id:int):
        self.__facesAmarelo = (self.face_tiro, self.face_passos, self.face_cerebro, self.face_tiro, self.face_passos, self.face_cerebro)# 'TPCTPC'
        self.__cor = self.cor_dado_intermediario
        super(Dado_Amarelo, self).__init__(self.__facesAmarelo,self.__cor,id)

    def lancar(self):
        return super(Dado_Amarelo, self).lancar()

class Dado_Vermelho (Dado):

    def __init__(self, id:int):
        self.__facesVermelho = (self.face_tiro, self.face_passos, self.face_tiro, self.face_cerebro, self.face_passos, self.face_tiro)# 'TPTCPT'
        self.__cor = self.cor_dado_dificil
        super(Dado_Vermelho, self).__init__(self.__facesVermelho,self.__cor,id)

    def lancar(self):
        return super(Dado_Vermelho, self).lancar()

