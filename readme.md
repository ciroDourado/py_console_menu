__Um simples menu__
# Para amantes de terminal :)
<br>
O package menu foi pensado em facilitar a criação de menus, <strong>sem que o programador tenha de se preocupar em criar várias condicionais de if elses</strong> ou tentar se aventurar em usar um dicionário ou hashmap para fazer a relação entre opção e função.
<br>
<br>
No fim, o código fica mais limpo e expansível, e toda a lógica de loop fica escondida na "caixinha" do objeto menu.
<br>
## Como utilizar
<br>
Passo a passo simplificado: 
<br>
|> baixe o repositório [*]
<br>
|> salve a pasta <strong>menu</strong> na raiz do seu projeto
<br>
|> importe a classe menu, instancie um objeto e inicialize [**]
<br>
<br>

[*]
<strong>

```
git clone git@github.com:ciroDourado/py_console_menu.git
```

</strong>
[**]
<strong>

```
from menu.ClasseMenu import Menu

...
meuMenu = Menu()
meuMenu.adicionar("Tecla", "Descrição", callback)
meuMenu.adicionar("Frase", "Descrição", callback)
meuMenu.botaoSair("Tecla ou frase")
...
meuMenu.loop() 
```

</strong>
<br>

## Exemplo
<br>
Imagine que temos de fazer um sistema de cadastro, com um menu que apresente algumas opções ao usuário (como cadastrar novo usuário, excluir cadastro, exibir dados, e por aí vai).
<br>
<br>
Normalmente começaríamos escrevendo funções que realizam cada uma das coisas, então:
<strong>

```
def cadastrar():
	print("Cadastrando...\n")
	# toda a lógica por trás desta função

def exibir():
	print("Exibindo...\n")
	# toda a lógica por trás desta função

def excluir():
	print("Excluindo...\n")
	# toda a lógica por trás desta função
```

</strong>
Feito isso, agora você se vê na parte mais importante do programa: criar a interface para o nosso querido usuário.
<br>
<br>
O intuitivo seria começar com um while infinito, onde dentro teriam alguns prints para mostrar as opções, um input para esperar uma opção do usuário, e um punhado de if's e else's para controlar o fluxo do programa.
<br>
<br>
É rápido, é simples, mas há um preço: à medida que o programa cresce, surgem mais opções, e com isso a chance de algo dar errado aumenta.
<br>
<br>
Um cenário: você escolheu usar números inteiros para selecionar cada opção, então a cada input você faz uma conversão.
<br>
O que pode dar errado? O usuário não dar um número, isso faria o programa quebrar.
<br>
O que pode ser trabalhoso para você?
A cada opção a mais, você teria de ajustar a verificação de números válidos, sem contar que teria de adicionar mais condicionais no punhado de if's, e mais prints para a opção do menu.
<br>
Fora de questão.
<br>
<br>
Outro cenário: bom, você viu que usar inteiros não dá muito certo, então abaixa um pouco o nível para receber inputs em texto. Isso facilita o tratamento de erros por parte do usuário, mas abre outro leque de situações.
<br>
O que pode continuar sendo trabalhoso? Isso também não resolve a questão do programa ficar poluído com mais um punhado de prints e condicionais.
<br>
Igualmente fora de questão.
<br>
<br>
Numa criação de menu, nós deveríamos nos preocupar apenas com o fluxo das coisas, e não em verificar o que pode dar errado. Isso toma um tempo preciosíssimo.
<br>
<br>
É aqui que entra o papel deste package: você apenas faria uma ligação entre opção, texto a ser apresentado, e a função que deve fazer algo acontecer.
<br>
<br>
Ao invés de:
<strong>

```
while (True):
	print("opcao 1")
	print("opcao 2")
	print("opcao 3")
	...
	print("X para sair")
	
	opcao = input("De uma opcao")
	if opcao == "1":
		funcao_1()
	else if opcao == "2":
		funcao_2()
	else if opcao == "3":
		funcao_3()
	...
	else if opcao == "X":
		break
	else:
		print("opcao invalida")
```

</strong>
Faça:
<strong>

```
menu = Menu()
menu.adicionar("1", "opcao 1", funcao_1)
menu.adicionar("2", "opcao 2", funcao_2)
menu.adicionar("3", "opcao 3", funcao_3)
...
menu.adicionar("X", "X para sair", None)

menu.botaoSair("X")
menu.loop()
```

</strong>
Ou, adaptando ao nosso exemplo inicial:
<strong>

```
from menu.ClasseMenu import Menu

def cadastrar():
	print("Cadastrando...\n")
	# toda a lógica por trás desta função

def exibir():
	print("Exibindo...\n")
	# toda a lógica por trás desta função

def excluir():
	print("Excluindo...\n")
	# toda a lógica por trás desta função

menu = Menu()
menu.adicionar("1", "Cadastrar novo cliente" , cadastrar)
menu.adicionar("2", "Exibir dados do cliente", exibir   )
menu.adicionar("3", "Excluir cadastro"       , excluir  )
menu.adicionar("X", "Sair do programa"       , None     )
menu.botaoSair("X")

menu.loop()
```

</strong>
![](/readme/exemplo.png)
