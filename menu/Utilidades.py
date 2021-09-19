import os
def limparTerminal():
    if os.name == "posix":
        os.system("clear")
    else: os.system("cls")
# limparTerminal
