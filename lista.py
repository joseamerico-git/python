frutas = ['abacaxi', 'melão' , 'pessêgo', 'limão']
legumes = ['mandioca','abobora','nhâme']

print(frutas)
print(legumes)

print(frutas+legumes)

print('Adicionando graviola')

# Insere item no final da lista
frutas.append('Graviola')
print(frutas)

# remove o ultimo elemento 
print('Removendo a graviola...')
frutas.pop()
print(frutas)
# Insere um elemento
frutas.insert(2,'Uva')
print(frutas)
#frutas.clear()
#print (frutas)
print(frutas)
#Contagem dos índices da lista
print(len(frutas))
# Inverte os itens da lista
frutas.reverse()
print(frutas)
# Ordena a lita 
frutas.sort()
print(frutas)




