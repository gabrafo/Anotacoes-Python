# \n -> token de quebra de linha em sistemas LF (Linux)

# O comando sep="" ou sep='' serve para que possamos escolher o separador que o Python usará entre os argumentos ao exibir
# Neste exemplo, será impresso: 12 34
print(12, 34, sep= " ") # Passagem de mais de um argumento
# A função print sempre coloca um espaço entre os dois argumentos na hora de exibir
# Python também gera uma quebra de linha automaticamente, sem a necessidade do programador pedir

# O end serve para alterar o que estará sendo passado ao interpretador ao final do comando de print
# Pode ser uma quebra de linha (o que já é padrão em Python, sem necessidade de especificarmos) com o uso do \n ou \r a depender do SO
# Ou pode ser qualquer outro caractere, como uma #, por exemplo
# Neste exemplo será impresso: 44_45### e não haverá quebra de linha, pois eu pedi ao interpretador que o newline fosse substituído por ###
print(44, 45, sep= "_", end="###")

# Neste exemplo, será impresso: 56-78## e haverá quebra de linha
print(56, 78, sep= "-", end="##\n")

# Neste exemplo, será impresso: 29 48
print(29, 48)

