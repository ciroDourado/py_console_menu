class Opcoes:
    # atributo:
    # |> opcoes: dict<string, Opcao>

    def __init__(self):
        self.opcoes = {}
    # construtor


    def __iter__(self):
        return self.opcoes.items()
    # como ele deve ser iterado num for
    # use assim
    #
    # opcoes = Opcoes()
    # opcoes.adicionar("1", " primeira opcao")
    # opcoes.adicionar("2", " segunda opcao")
    # for botao, opcao in opcoes:
    #     print(botao + opcao)
    # # vai printar "1 primeira opcao"
    # # vai printar "2 segunda opcao"


    def todas_as_opcoes(self):
        return self.__iter__()
    # apenas um __iter__ com nome mais bonito
    # use assim
    #
    # opcoes = Opcoes()
    # opcoes.adicionar("1", " primeira opcao")
    # opcoes.adicionar("2", " segunda opcao")
    # for botao, opcao in opcoes.todas_as_opcoes():
    #     print(botao + opcao)
    # # vai printar "1 primeira opcao"
    # # vai printar "2 segunda opcao"


    def __str__(self):
        texto = ""

        for botao, opcao in self.todas_as_opcoes():
            texto += f"{botao}. {opcao}\n"
        return texto
    # como ele aparece no print()
    # use assim
    #
    # opcoes = Opcoes()
    # opcoes.adicionar("1", "primeira opcao")
    # opcoes.adicionar("2", "segunda opcao")
    # print(opcoes)
    # # vai printar de uma vez
    # # "1. primeira opcao"
    # # "2. segunda opcao"


    def naoPossui(self, botao):
        return not botao in self.opcoes
    # naoPossui


    def ehValida(self, botao):
        return botao in self.opcoes
    # ehValida


    def atualizar(self, botao, opcao):
        self.opcoes[botao] = opcao
    # atualizar


    def adicionar(self, botao, opcao):
        if self.naoPossui(botao):
            self.opcoes[botao] = opcao
    # adicionar


    def executar(self, botao):
        self.opcoes[botao].executar()
    # executar
# fim class Opcoes
