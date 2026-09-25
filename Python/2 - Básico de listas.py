import random
# lista é definida por um agrupamento de itens, ela facilita o agrupamento de várias informações e logo o armazenamento desses dados.
# é definida com nome da lista e sinal de atribuição = e os itens entre colchetes [] e separados por virgula.

nome_lista = ['item1', 'item2', 'item3', 'item4']
print(nome_lista)

# a lista pode ser concanetada com outra lista para não interferimos na primeira lista.
nome_lista2 = ['item5', 'item6', 'item7']
todas_lista = nome_lista + nome_lista2
print(todas_lista)
# a lista também pode ser multiplicada com o sinal de * e a quantidade.
# com a palavra nome da lista.append podemos adicionar um item de forma mais fácil sem precisar altera a lista inicial.
todas_lista.append('super_item')
print(todas_lista)

# a lista é indexada sendo a busca de acordo com os itens sequencialmente, o item inicial é buscado com 0 até o tamanho da lista -1 entre colchetes[]
print(nome_lista2[0])

# indexação pode ser ao contrária começando pelo -1.
print(todas_lista[-1])

# podemos tambem contar quantos itens possui dentro de uma lista com len() por sua vez para ser printada precisa ser transformada em string.
print(str(len(nome_lista2)))

# também depois de muito adicionar podemos remover com .remove sendo o antonimo de .append. sem precisar alterar a lista inicial.
nome_lista.remove('item4')
print(nome_lista)
print(todas_lista) # essa remoção também impactaria em todas as listas la atras.

# a funcionalidade .pop remove e retorna o valor selecionado.
#teste
teste = nome_lista2.pop(1)
print(teste + 'ta aqui o teste do pop')

# se eu quiser fazer uma remoção por indexação? possui a funcionalidade del nome da lista entre colchetes []
del nome_lista2[0]
print(nome_lista2)

# também posso zerar a lista com a funcionalidade . clear apos nome da lista
nome_lista2.clear()
print(nome_lista2)

# porem realizando . clear em uma lista que havia sido somada com outra lista não realiza alteração na soma anterior.
print(todas_lista)

# é possivel inserir com . insert na lista por meio de indexação
nome_lista.insert(0,'item_Bom')
print(nome_lista)
# outras funcionalidades .sort() ordena por ordem sequencial númerica ou para strings em ordem lexicografica que seria de acordo com o dicionario.
# .reverse ela inverte a ordem da lista ao contrario. o ultimo sendo o primeiro item e sequencialmente ao contrario.
# .count conta quando itens iguais possui naquela lista
# teste
x = int(input('Escolha um número de 1 a 8 para saber o seu item!'))
print(todas_lista[x-1])

# slice é
palavra = 'hacker'
# entre colchetes [inicio:fim:salto]

#teste
d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(random.choice(d20))
#tive que fazer import random