# Dictionary é uma estrutura de dados que guarda informações em pares de chaves e valores. Enquanto chaves são imutáveis os valores podem ser tanto mutaveis ou imutaveis.
# O Dictionary é usado para ser acessado por um nome chave, sendo muito mais eficiente do que buscar por um valor.
dados = { 'nome': 'carlos', 'idade': 23 }
print(dados)
# Unpacking com * e **, com apenas * antes do dictionary pegamos so a palavra chave.
# Com ** pegamos a palavra chave e valores em pares, é usado frequentemente em fusão de dictonarys ou para passar a palavra chave em outras funções.
# chave sendo a primeira palavra antes de igual dentro do dictionary.
dados2 = {'sobrenome': 'henrique', 'idade': 24}
print(*dados)
fusão = {**dados, **dados2} # o dado idade foi sobescrito com o novo dado, e fundiu os pares de palavra chave e valor diferentes.
print(fusão)
# def nome_idade(nome, idade):
#    print(f'{nome} tem {idade} anos')
# nome_idade(**dados)
# .split separa tudo entre espaço funcionam em lista tbm
# slicing 'start:stop:step', :

#FUNDAMENTOS DE DICIONÁRIOS EM PYTHON

# Dicionários é uma forma de organizar em pares informações chave e de valor.
# As chaves são informações imutáveis e únicas e valores são mutáveis que podem ser
# alteradas. É usada devido a velocidade de busca e inserção de elementos em grandes
# bancos de dados.
# Dicionários são definidos com uma palavra definida o símbolo de igual e entre
# o símbolo chaves, os dados em pares separados por dois pontos,
# ou pode ser utilizada o constructo ‘dict()’com pares separadores por virgula.
# Em caso de um valor-chave estiver duplicado, o valor dado por último será usado
# como único.
# As formas mais comuns de se interagir com um dicionário são ‘.get(Chave)’
# Para conseguir o valor da chave sem acarretar um erro de chave ‘KeyError’, caso a
# chave solicitada não exista aparece apenas nenhum ‘none’. Uma forma de extrair
# todas as chaves ‘.keys()’ e valores ‘.values()’. Os dois valores ‘.item()’ que retorna
# em forma de lista as chaves e valores em tuplas.
# É possível atualizar o valor em uma chave com a palavra definida e entre
# colchetes a chave, após isso o sinal de igual e o seu novo valor, assim como apagar
# uma lista completa com ‘.clear()’ e deletar apenas um par com ’del’ palavra definida
# e entre colchetes a chave.
