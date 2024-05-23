#imprimir com final diferente
print("meu nome é", end=" ")
print("fernanda")

#imprimir com separador
print("meu", "nome", "é", "fernanda", sep="-")

#imprimir aspas
print("fernanda \"lopes\"")

#imprimir várias linhas
print("""eu
sou
a 
fernanda""")

#modificando strings
frase = "fernanda lopes"
print(frase.upper()) #letra maiúscula
print(frase.lower()) #letra miniscula
print(frase.capitalize()) #1º letra da 1º palavra maiúscula
print(frase.title()) #todas as 1º letras maiúsculas

frase = "eu sou a fernanda"
lista = frase.split(' ') #dividir input em lista
print(lista)
novaFrase = '-'.join(lista) #transforma a lista em um "texto"
print(novaFrase)
novaFrase = frase.replace("fernanda", "joana") #substitui alguma palavra
print(novaFrase)
print(frase.count('a')) #conta quantos 'a' a str possui
print(frase.find('f')) #retorna a posição do 'f' na str

frase = "fernanda01"
print(frase.isalnum()) #retorna se str é formada por letras e/ou números
print(frase.isalpha()) #retorna se str é formada por letras
print(frase.isnumeric()) #retorna se str é formada por números
print(frase.startswith("fer")) #retorna se str inicia com "fer"
print(frase.endswith('1')) #retorna se str é termina com '1'
frase = " fernanda01 "
print(frase.strip()) #retira espaços do começo e final
