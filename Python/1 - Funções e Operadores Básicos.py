# Função é um bloco organizado de codigos que pode ser executada várias vezes por meio de um comando predefinido.
# Usando a palavra chave def seguida do nome função e em  parenteses os parametros de entrada e fechado com dois ponto :
# em seguida o bloco com o código que a função sera atribuida ao ser chamada.
# def nome_da_função(parametros):
#       bloco de código que é executado quando a função é chamada.
# Toda variável que está fora da função é chamada de variável global, que é utilizada em todo o código.
# Variável local é aquela que está no escopo apenas da função.

a = int(input('Primeiro número : '))
b = int(input('Segundo número : '))


def soma(a, b):
    return a + b


resultsoma = soma(a, b)
print('O resultado da soma é:', resultsoma)


# return é utilizado em funções simples aritméticas pois quando a função é chamada, retorna com os valores da operações.

def multiplicação(a, b):
    return a * b


multi = multiplicação(a, b)
print('O resultado da multiplicação é:', multi)

# A função pode ser usada tanto em operações de matemática quanto em frases.
nome = input('Qual seu nome? ')


def ola(nome):
    print('Seja Bem-vindo', nome, '!')


ola(nome)

# A função evita repetição e torna mais fácil a leitura , correção e teste do código.

##################################################################
# Operadores básicos:
# +  : adição de números , e concanetação de strings
# -  : subtração
# *  : multiplicação , pode ser usado em multiplicação de strings.
# /  : divisão (divisão normal)
# // : divisão inteira (descarta o valor depois da virgula)
# %  : retorna o resto da divisão
# ** : potência
# =  : atribuição de valor a variaveis.
# == : comparação de igualdade retornando verdadeiro ou falso
# != : diferente da igualdade
# <  : menor que
# >  : maior que
# <= : menor ou igual ao valor
# <= : maior ou igual ao valor
###################################################################
# A concanetação é o processo de juntar duas ou mais sequencias de strings
# Um dos métodos é por meio da adição (+) que é preciso converter números em strings e há muito repetição em abrir e fechar aspas e virgula.
print(nome + ' a soma é ' + str(resultsoma) + ' e a multiplicação é ' + str(multi))

# Método '{} , .format()' substitui as chaves pelos parametros entre parenteses do .format transformando em string a função aritmética e organizando em ordem sequencial os parametros.
# os valores dentro dos parenteses de .format podem ser alternados com a enumeração sendo dentro das chaves com o primeiro parametro sendo 0 até a quantidade de parametros -1.
print('{} a soma é {} e a multiplicação é {}'.format(nome, resultsoma, multi))

# fstring é uma forma de transformar o os paramentros dentros das chaves por meio do prefixo f : (f' texto {} texto')
print(f'tá aqui o teste {nome}')

####################################################################

# a, b, c = input(), input(), input() Pede para o usuário 3 vezes consecutivas para inserir uma variavel e atribuindo a letra consecutivamente.
# Vai ser transformado em string devido a falta de formatação.
# coloquei um texto nos inputs para não se perder.
a, b, c = input('primeira palavra : '), input('segunda : '), input('terceira : ')
# Com a inserção de 'a, b, c = input(), input(), input()' vou escrever os resultados.
print(a, b, c)


