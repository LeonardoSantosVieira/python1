numero = int(input( ' Informe um numero:'))

resultado = int(numero % 2) # % significa resto ou seja o numero que sobre  na divisão

print( ' se o resultado for 0 é par e se for 1 é ímpar,o resultado é:', resultado)
input('Digite ENTER para continuar')
# if é usado para tomada de decisão2
if resultado == 0:
    resultado = ' O numero é par ' 
else: resultado = 'O numero é ímpar' 
print(resultado)

input('Digite ENTER para continuar')
from os import system, name 
system('cls') if(name == 'nt') else system('clear')

#entrada da nota
nota = float(input("digite a nota do estudante: "))

# Verificação da situação
if nota >= 7:
    print('aprovado')
elif nota >= 5:
    print('recuperação')
else:
    print('reprovado')
