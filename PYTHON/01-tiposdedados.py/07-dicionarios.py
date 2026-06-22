pessoa = {
    "nome": "Ana" , 
    "idade": 30 
}   

print(pessoa)
print(pessoa["nome"])

#alterando valores
pessoa["idade"]= 31
print(pessoa)

#adicionando novo dado
pessoa["cidade"] = "São Paulo"
print(pessoa)

#removendo
del pessoa["idade"]
print(pessoa)
 
pessoaNova= {
"primeironome": "Valdirema", 
"idade": 50               
}
#Ver chaves 
print(pessoaNova.keys())

#Ver valores
print(pessoaNova.values())

#Ver chave e valor
print(pessoaNova.items())

#Verificar se chave existe
print("nome" in pessoaNova)
print("primeironome" in pessoaNova)

#Usar get 
print(pessoaNova.get("primeironome"))

#percorrer
for chave, valor in pessoaNova.items():
    print(chave, ":",valor)