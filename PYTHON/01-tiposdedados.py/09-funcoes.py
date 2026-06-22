
#Função
def saudacao():
    print ("Olá, tudo bem?")
 
#acessando a função
saudacao()
 
#função com parâmetro
def saudacao(nome):
    print("Olá,", nome)
         
#Acessando a função
saudacao("Neymar")
 
#função de retorno
def soma (a, b):
    return a + b
 
resultado = soma(5, 3)
print(resultado)
 
def descontoA (valor1, desc):
    return
 
#try significa tentar
try:
    numero = int(input("Digite um número: "))
except:
    print("Você digitou algo inválido!")
 
#Try e Except usando Else e Finally juntos
try:
    numero = float(input("Digite um número: "))
except ValueError:
    print ("Erro: entrada inválida")
else:
    print ("Você digitou:", numero)
finally: # finally é como se fosse completar o else. É o que finaliza o programa
    print ("Programa finalizado")
 
 
#loop com try e except
while True:
    try:
        n = int(input("Digite um número: "))
        print(n)
        break
    except ValueError:
        if input ("tentar novamente? (s/n): ").lower() != 's':
            break
 
#Exemplo de função com try e except
def dividir (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
print (dividir(10, 2))
print (dividir (23,0))
 
'''Não é possível dividir por zero
porque essa operação não tem um valor
definido e é inválida em matemática.'''

#entrada do usuário
a = float(input("digite o primeiro número:  "))
b = float(input("digite o segundo número:   "))
print(dividir (a,b))


