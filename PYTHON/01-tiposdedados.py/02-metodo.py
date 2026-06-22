#soma
num1 = input('Informe o primerio número:')
num2 = input('Informe o segundo número:')

soma= int(num1) + int(num2)
subtracao= int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto= int(num1) % int(num2)
multiplicacao= int(num1) * int(num2)
potenciacao= int(num1) ** int(num2)

print(soma)
print(subtracao)
print(divisao)
print(moduloresto)
print(multiplicacao)
print(potenciacao)

# o comando tupe retorna do tipo da variável
print(type(num1))
print(type(soma))

#Calcular área
lado1 =  input('infrome o primeiro lado:')
lado2 =  input('infrome o segundo lado:')

nomecompleto = input( 'Informe o seu nome completo: ')
# função len retorno a quantidade de caractres de uma variável
print( ' 1. quantidade de caracteres:', len(nomecompleto))

#  metodos utlizados:
# upper = transforma um texto em maiusculo
# lower = trasnforma um texto em minusculo
# capitalize = somente a primeira letra em maiusculo
print('2. Nome em maiusculo:', nomecompleto.upper())
print('3. Nome em minusculo:', nomecompleto.lower())
print('4. Primeira letra em maiusculo:', nomecompleto.capitalize())

 



