#loopd.py
for i in range(1,6):
    print(i)

frutas = ["maça","banana","uva"]
for fruta in frutas:
    print(fruta)

#loop for com continue (pula o 5)
for j in range(1,11):
    if j ==5:
        continue
    print(j)

#loop for com break (para no 4)
for l in range(1,11):
    if l ==5:
        break
    print(l)

#usando o continue e break juntos 
for n in range(1,11):
    if n == 5:
        continue #pula o numero 5
    print(n)

    if n == 9:
        break # para o loop quando chega no 8
print(n)

#loop while
contador = 1
 
while contador <= 100:
    print(contador)
    contador += 1 # incremento

    texto = ""

while texto != "sair":
    texto = input("Digite algo (ou 'sair' para parar:): ")

   #loop com try e except
while True:
    try:
        n= int(input("Digite um número: "))
        print(n)
        break
    except ValueError:
        if input("Tentar novamente? (s/n): ").lower() !=  's':
            break


    