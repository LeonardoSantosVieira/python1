frutas= ["maça","banana","uva"]
print(frutas)

#ver primeiro elemnto da lista
print(frutas[0])

#retornando demais elemntos no seu index 
print(frutas[1])
print(frutas[2])

#modificando
frutas[1]= "laranja" 
print(frutas)

#adiocionar= append
frutas.append("pêra")
print(frutas)

#adicionar no começo da lista = .insert(numero,"objeto")
frutas.insert(0,"abacaxi")
print(frutas)

#removendo itens
frutas.remove("uva")
print(frutas)

#tamanho da lista "len" faz a contagem 
numeros = [1,2,4,3]
print(len(numeros))

#ordenar
numeros.sort()
print(numeros)

#inverter
numeros.reverse()
print(numeros)

#verificar se exite
print(2 in numeros)

#adicionando vários elementos
numeros =[10,20,30] + numeros 
print(numeros)

#percorrer com for 
for n in numeros:
    print(n)
