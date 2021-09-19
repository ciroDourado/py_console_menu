import menu
from menu.ClasseMenu import Menu

# criar um menu é super simples:
#
# primeiro, apenas defina as
# funções que cada opção executa

def cadastrar():
    print("Cadastrando...\n")

def exibir():
    print("Exibindo...\n")

def excluir():
    print("Excluindo...\n")


# em seguida, apenas instancie um
# objeto menu, e então, ligue cada opção
# com a função que ela deve executar
#
# por exemplo, a tecla 1 está associada
# à opção de realizar um cadastro
#
# daí, tudo o que tem de ser feito é dar
# um texto que vai representar aquela opção
# na tela, e a função que vai fazer alguma coisa


menuPrincipal = Menu()
menuPrincipal.adicionar("1", "Cadastrar", cadastrar)
menuPrincipal.adicionar("2", "Exibir"   , exibir   )
menuPrincipal.adicionar("3", "Excluir"  , excluir  )
menuPrincipal.adicionar("4", "Sair"     , None     )

menuPrincipal.botaoSair("4")

# aqui acima, o passo mais importante é definir
# qual das teclas será o botão de encerrar o menu
# nunca se esqueça de inicializar ele
#
# para executar o programa/menu, faça:

menuPrincipal.loop()
