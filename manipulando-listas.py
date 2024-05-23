#separar um input/variável em lista
#linha = input("Escreva 5 letras: ")
linha = "a b c d e"
lista = linha.split() 
print(lista)

#gerar listas
lista = list(range(10)) #de 0 a 9
print(lista)
lista = list(range(2, 8)) #de 2 a 8
print(lista)
lista = list(range(2, 8, 3)) #de 2 a 8, mas com intervalo de 3 num
print(lista)

#imprimir lista numerada
lista = ['a', 'b', 'c', 'd']
for i in range(4):
    print(i, lista[i])

#contar itens em listas
lista1 = [1, 2, 3]
lista2 = []
lista3 = [lista1, lista2]
print(len(lista1), len(lista2), len(lista3))

#imprimir fatias de listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
print(lista[:]) #imprime todos os itens
print(lista[0]) #imprime o elemento da posição
print(lista[-1]) #imprime o último elemento
print(lista[1:3]) #imprime do elemento 2 ao 3
print(lista[:3]) #imprime do 0 ao 3
print(lista[2:]) #imprime do 3 ao -1 (último)

#métodos de listas
lista = [1, 2, 3, 4, 5]
lista.append(6) #adiciona o 6 ao final da lista
print(lista)
lista.insert(0, -1) #insere item -1 na posição 1
print(lista)

lista.sort(reverse=True) #decrescente, irrecuperável a lista original
print(lista)
lista.sort() #crescente, irrecuperável a lista original
print(lista)

print(sorted(lista, reverse=True)) #decrescente, não definitivo
print(sorted(lista)) #crescente, não definitivo

lista[0] = 1 #altera o num da posição 0 
print(lista)
lista[0] = lista[6] #copia o valor da posição 6 para a posição 0
print(lista)

print(len(lista)) #verifica o tamanho da lista
print(min(lista)) #menor item da lista
print(max(lista)) #maior item da lista
print(lista.count(6)) #conta quantos itens 6 existem na lista
print(lista.index(3)) #procura pelo item 3 e retorna sua posição
print(sum(lista)) #soma todos os items da lista

#métodos de remover itens
lista = [9, 8, 7, 6, 5]
del lista[1] #deleta o item da posição 1
print(lista)
lista.remove(6) #remove o item 6
print(lista)
lista.pop() #exclui o último item
print(lista)
lista.pop(0) #exclui item indicado na posição
print(lista)
lista.clear() #torna a lista vazia
print(lista)

#unir listas
lista1 = [1, 2, 3] #somando lista
lista2 = ['a', 'b', 'c']
lista3 = lista1 + lista2
print(lista3)

lista = [0, 1] #método extend
lista.extend([2, 3, 4])
print(lista)

lista1 = [1, 2, 3] #sublistas lista
lista2 = ['a', 'b', 'c']
lista3 = [lista1, lista2]
print(lista3)

#copiar uma lista
lista1 = [1, 2, 3] #lista1 e lista2 são objetos diferentes na memória com uso de fatiamento
lista2 = lista1[:]
print(lista2)

lista1 = [1, 2, 3]
lista2 = lista1.copy() #lista1 e lista2 são objetos diferentes na memória com uso de um método
print(lista2)

lista1 = [1, 2, 3] #lista1 e lista2 são o mesmo objeto na memória, lista2 não é uma nova lista, apenas uma referência
lista2 = lista1
print(lista2)
