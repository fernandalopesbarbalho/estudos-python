#tuplas: usam (), cada elemento pode ser de tipo diferente (str, int, float). não se muda seu conteúdo e utiliza fatias para imprimir
#dicionário
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
dicionario = dict(zip(lista1, lista2))
print(dicionario[1]) #usa a "chave" para retornar seu valor correspondente

dicionario[4] = 'd' #adiciona novo item
print(dicionario[4])

dicionario.update({5: 'e'}) #adiciona novo item com método
print(dicionario[5])

print(len(dicionario)) #retorna quantos pares

print(dicionario.keys()) #imprime as chaves
print(dicionario.values()) #imprime os valores
print(dicionario.items()) #imprime os itens

del dicionario[3] #remove o item
print(dicionario)

print(dicionario.popitem()) #remove o último item e imprime
