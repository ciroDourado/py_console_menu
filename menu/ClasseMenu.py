from menu.Utilidades   import limparTerminal
from menu.ClasseOpcoes import Opcoes
from menu.ClasseOpcao  import Opcao

class Menu:
    # atributos
    # |> opcoes      : Opcoes
    # |> botaoDeSaida: string

    def __init__(self):
        self.opcoes       = Opcoes()
        self.botaoDeSaida = ""
    # construtor


    def adicionar(self, botao, descricao, funcao):
        opcao = Opcao(descricao, funcao)
        self.opcoes.adicionar(botao, opcao)
    # adicionar


    def botaoSair(self, botao):
        self.botaoDeSaida = botao
    # botaoSair


    def ehBotaoSair(self, botao):
        return self.botaoDeSaida == botao
    # ehBotaoSair


    def loop(self):
        limparTerminal()

        while (True):
            textoMenu = f"{self.opcoes} \nDê a opção: "
            botao     = input(textoMenu)
            limparTerminal()

            if ( self.ehBotaoSair(botao) ):
                break
            else: self.verificar(botao)
        # while
    # loop


    def verificar(self, opcao):
        if ( self.opcoes.ehValida(opcao) ):
            self.opcoes.executar(opcao)
        else: print("Essa opção é inválida\n")
    # verificar
# fim class Menu
