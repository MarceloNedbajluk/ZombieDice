
class Jogador:
    def __init__(self,nome:str):
        # o construtor da classe exige o nome do jogador e inicia a variável _cerebros com o valor 0
        self._nome = nome
        self._cerebros = 0

    def soma_pontos(self, valor:int):
        # método utilizado para alterar o valor do atributo cérebro
        self._cerebros += valor

# inicioGetters
    @property
    def nome(self):
        return self._nome

    @property
    def cerebros(self):
        return self._cerebros
    # como não é desejável que a quantidade de cérebros ou o nome sejam alterados diretamente, os atributos não possuem setters
# fimGetters&Setters

