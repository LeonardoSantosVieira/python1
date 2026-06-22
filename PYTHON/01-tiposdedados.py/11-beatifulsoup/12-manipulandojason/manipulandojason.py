import json

with open('dados.json', 'r', encoding = 'utf-8') as arquivo:
    dados = json.load(arquivo)

    print(dados)
    print(dados['nome'])

    #convertendo json em str 
    texto = json.dumps(dados, indent=4, ensure_ascii=False)
    print(texto)

#convertendo o str em json
pessoaNova = '{"primeronome":  "Vânia", "idade": 50}'

dados = json.loads(pessoaNova)
print(dados)

# atulizando
with open('dados.json', 'r', encoding = 'utf-8') as arquivo:
    dados = json.load(arquivo)

dados['idade'] = 35 # alteração

with open('dados.json', 'w', encoding = 'utf-8') as arquivo:
    json.dump(dados,arquivo,indent=4,ensure_ascii=False)