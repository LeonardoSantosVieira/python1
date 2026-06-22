# O que é CSV?
'''CSV é a sigla para Comma-Separated Values (Valores Separados por Vírgula).
É um formato de arquivo simples usado para armazenar e organizar dados em forma de tabela (como planilhas).'''
#Para que serve o CSV?
'''Ele é utilizado para:
Armazenar dados tabulares (linhas e colunas)
Trocar informações entre sistemas (Excel, bancos de dados, softwares)
Importar e exportar dados de forma simples'''
 
import csv
 
listaprodutos = [
    ['produto', 'quantidade', 'valor'],
    ['computador', '2', '1999.99'],
    ['camera', '10', '79.99'],
    ['microfone', '7', '39.99']
]
 
#Escrita
with open('listaprodutos.csv' , 'w', newline='') as arquivo:
    csv_writer = csv.writer(arquivo, delimiter=';')
 
    for produto in listaprodutos:
        csv_writer.writerow(produto)
        print(produto)

#Leitura
'''
with open('listaprodutos.csv', 'r') as arquivo:
    csv_writer = csv.reader(arquivo, delimiter=';')
    for line in csv_writer:
        print(line)
'''

#Lê o que ja existe no arquivo
produtos_existentes = set()

try:
    with  open('listaprodutos.csv', 'r') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            produtos_existentes.add(tuple(linha))   # transforma em tupla para comparação
except FileNotFoundError:   
    pass    #se o arquivo ainda não existe

# Agora grava só os que não existem - apend / atualização
with open('listaprodutos.csv', 'a', newline='')as  arquivo:
    writer = csv.writer(arquivo,delimiter=';')

    for produto in listaprodutos[1:]: #ignora o cabeçalho
        if tuple(produto) not in produtos_existentes:
            writer.writerow(produtos)
            print(produto)