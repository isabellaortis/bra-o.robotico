'''# exercício 7

import random

numero_sortedo = random.randint(0,1000) 

for tentativas in range(1, 11):
    palpite = int(input("seu palpite:"))
    
    if palpite == numero_sortedo:
        print("parabéns! acertou")
    
    elif palpite < numero_sortedo:
        dica = print("maior") 
    
    else:
        dica = print("menor") 
        
print(f"errou! o valor sorteado é {numero_sortedo}")
print(f"acabaram as tentativas! o numero sorteado era {numero_sortedo}")

# exercício 8

n = int(input("Digite quantas Tabuadas Deseja Mostrar: "))

for i in range(1, n + 1):
        for j in range(1, 11):
            print(f"{i} * {j}={i*j}", end= '')
            print()
            
# exercício 10

def desenhar_caixa(n, m):
   
    if n <= 0 or m <= 0:
        print("Número de linhas e colunas devem ser positivos.")
        return


    caixa = []

   
    caixa.append(['m']  * m)


    for _ in range(n - 2):
        caixa.append(['n'] + [' '] * (m - 2) + ['n'])

  
    if n > 1:
        caixa.append(['m'] * m)


    for linha in caixa:
        print(''.join(linha))


n = int(input("coloque o número de linhas desejadas para n: "))
m = int(input("coloque o número de colunas desejadas para m: "))


desenhar_caixa(n, m)

# exercício 11

import random

L = [random.randint(1, 100) for _ in range(50)]

print(L)

# exercício 12

L = [i ** 2 for i in L]

L_squared = [i ** 2 for i in L]

# exercício 13

count = len([i for i in L if i > 50])

count = 0
for i in L:
    if i > 50:
        count += 1 

# exercício 14

import random
L =[]
quantos = int(input("Quantos numeros serão digitados? "))
for i in range(quantos):
    num= random.randint(1,10)
    L.append(num)
print (L)
nmrs1 = 0
nmrs2 = 0 
nmrs3 = 0
nmrs4 = 0
nmrs5 = 0
nmrs6 = 0 
nmrs7 = 0 
nmrs8 = 0 
nmrs9 = 0 
nmrs10 = 0
for j in range(len(L)):
    if L[j] == 1:
        nmrs1 += 1
    elif L[j] == 2:
        nmrs2 += 1
    elif L[j] == 3:
        nmrs3 += 1
    elif L[j] == 4:
        nmrs4 += 1
    elif L[j] == 5:
        nmrs5 += 1
    elif L[j] == 6:
        nmrs6 += 1
    elif L[j] == 7:
        nmrs7 += 1
    elif L[j] == 8:
        nmrs8 += 1
    elif L[j] == 9:
        nmrs9 += 1
    else:
        nmrs10 += 1
print(f"Há {nmrs1} numeros 1, {nmrs2} numeros 2, {nmrs3} numeros 3, {nmrs4} numeros 4, {nmrs5} numeros 5, {nmrs6} numeros 6, {nmrs7} numeros 7, {nmrs8} numeros 8, {nmrs9} numeros 9 e {nmrs10} numeros 10")
  
        

# exercício 15

L = [...*,]  

L_sorted = sorted(L)

print("Dois maiores elementos:", L_sorted[-1], L_sorted[-2])
print("Dois menores elementos:", L_sorted[0], L_sorted[1])

L1 = [i for i in range(50)]

L2 = [i ** 2 for i in range(1, 51)]

L3 = []
for i in range(26):
    letter = chr(ord('a') + i)
    L3.append(letter * (i + 1)) 
    
 # exercício 16
    
# 1. Uma lista que contenha os inteiros de 0 a 49

lista_inteiros = []
for i in range(50):
    lista_inteiros.append(i)
print(lista_inteiros)

# 2. Uma lista contendo os quadrados dos inteiros de 1 a 50

lista_quadrados = []
for i in range(1, 51):
    lista_quadrados.append(i ** 2)
print(lista_quadrados)

# 3. A lista [ ’a’, ’bb’, ’ccc’, ’dddd’, ... ] que termina com 26 cópias da letra z

lista_letras = []
for i in range(1, 27):
    letra = chr(96 + i)
    lista_letras.append(letra * i)
print(lista_letras)

# exercício 17

string_vazia = ""*10
print (string_vazia)
18
caracX= "X"*100
print(caracX)
19
milOi= "Oi"*1000
print(milOi)	# 1. Uma lista que contenha os inteiros de 0 a 49
lista_inteiros = []
for i in range(50):
    lista_inteiros.append(i)
print(lista_inteiros)

# 2. Uma lista contendo os quadrados dos inteiros de 1 a 50
lista_quadrados = []
for i in range(1, 51):
    lista_quadrados.append(i ** 2)
print(lista_quadrados)

# 3. A lista [ ’a’, ’bb’, ’ccc’, ’dddd’, ... ] que termina com 26 cópias da letra z
lista_letras = []
for i in range(1, 27):
    letra = chr(96 + i)
    lista_letras.append(letra * i)
print(lista_letra)

# exercício 18

X_string = 'X' * 100

print(X_string)'''
    
# exercício 19

Oi_string = 'Oi ' * 1000

print(Oi_string)