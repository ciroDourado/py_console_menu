class Opcao:
    # atributos
    # |> descricao: string
    # |> funcao   : função

    def __init__(self, descricao, funcao):
        self.descricao = descricao
        self.funcao    = funcao
    # construtor


    def __str__(self):
        return self.descricao
    # como ele aparece no print()


    def executar(self):
        self.funcao()
    # executar
# fim class Opcao
