"""
DocString: String de documentação.
Python = Linguagem de Programação
Tipagem = Dinâmica/Forte
Tipagem dinâmica: O interpretador descobre o tipo de dado que está sendo passado a ele.

Tipo str: em Python, Strings são denominadas pelo uso de "str".
"""

# Não há diferença entre aspas duplas e simples para o interpretador
print("Gabriel Fagundes")
print('Gabriel Fagundes')

# Ao usar um tipo de aspas para abrir a String, obrigatoriamente você terá que o usar o mesmo tipo para fechar
# Mas nada impede que você use o outro tipo de aspas restante para colocá-lo como conteúdo dentro da String
# Isso evita o uso do caractér de escape do exemplo abaixo
print('Gabriel "Grafundes" versão 1')

# Uso de caractér de escape \" para que essas aspas não sejam confundidas com a de início/fim da String
print("Gabriel \"Gafrundes\" versão 2")

# O uso de "r" faz com que o interpretador mostre os caractéres de escape
print(r"Gabriel \"Gafrundes\" versão 3")