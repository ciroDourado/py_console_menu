__Um simples menu__
# Para amantes de terminal :)
<br>
<br>
O package menu foi pensado em facilitar a criação de menus, 
**sem que o programador tenha de se preocupar em criar várias condicionais de if elses**
ou tentar se aventurar em usar um dicionário ou hashmap para fazer a relação entre opção e função.
<br>
<br>
No fim, o código fica mais limpo e expansível, e toda a lógica de loop fica escondida na "caixinha" do objeto menu.

## Como utilizar
<br>
Passo a passo simplificado: 
<br>
|> baixe o repositório [*]
<br>
|> salve a pasta 
**menu**
na raiz do seu projeto
<br>
|> importe a classe menu, instancie um objeto e inicialize [**]
<br>
<br>

[*]

```
git clone git@github.com:ciroDourado/py_console_menu.git
```
[**]

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