#Imprimir números de 1 a 10:
for i in range(1,11):
    print(i)

#Imprimir números de 10 a 1 (ordem decrescente):    
for i in range(10, 0 -1):
    print(i)

 
#Imprimir números pares de 1 a 20:   
for i in range(2,21,2):
    print(i)

 #imprimir números ímpares de 1 a 20:
for i in range (1, 21, 2):
    print(i)   


#Imprimir múltiplos de 5 de 1 a 50:    
for i in range(5, 51, 5):
    print(i)


#Imprimir números de 1 a 100, substituindo múltiplos de 3 por "Fizz":
for i in range(1, 101):
    if i % 3 == 0:
        print("fizz")
    else:
        print(i)


#Imprimir números de 1 a 100, substituindo múltiplos de 5 por "Buzz":        
for i in range(1,101):
    if i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Imprimir números de 1 a 100, substituindo múltiplos de 3 e 5 por "FizzBuzz":
for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("fizz")
    elif i % 3 == 0:
        print("buzz") 
    else:
        print(i)


#Calcular a soma dos números de 1 a 100:
soma = 0
for i in range(1, 101):
    soma += i
print(soma)                         


#Calcular a soma dos números pares de 1 a 100:
soma=0
for i in range(2, 10, 2):
    soma += i
print(soma)

#Calcular a soma dos números ímpares de 1 a 100:
soma = 0
for i in range(1, 101, 2):
    soma += i 
print(soma)


#Imprimir a tabuada do 5 (de 1 a 10):
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

    
#Imprimir a tabuada de um número fornecido pelo usuário:
num = int(input("Digite um numero:")) 
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
#Imprimir todas as tabuadas de 1 a 10:
for i in range(1, 11):
    for j in range(1, 11):
        print(f" {i} x {j} = {i * j}")
    print()


#Imprimir os quadrados dos números de 1 a 10:
for i in range(1, 11):
    print(i ** 2)

#Imprimir os cubos dos números de 1 a 10:
for i in range(1, 11):
    print(i ** 3)

#Calcular o fatorial de um número:
num = int(input("Digite um número"))
fatorial = 1 
for i in range(1, num + 1):
    fatorial *= i
print(f"fatorial de {num} é {fatorial}") 


#Imprimir os números de 1 a 100, parando ao encontrar o número 50:
for i in range(1,  101):
    if i == 50:
        break
    print(i)



#Imprimir os números de 1 a 100, pulando os múltiplos de 7:
for i in range(1, 101):
    if i % 7 == 0:
        continue
    print(i)

#Imprimir os números de 1 a 100, substituindo números que contêm o dígito 3 por "Três":
for i in range (1, 101):
    if '3' in str(i):
        print("três")
    else:
        print(i)

#Imprimir números de 1 a 10 usando while:    
i = 1
while i <= 10:
    print(i)
    i += 1

#Imprimir números de 10 a 1 usando while:
i = 10
while i >= 1:
    print(i)
    i-=1

#Imprimir números pares de 1 a 20 usando while:
i=2
while i <= 20:
    print(i)
    i += 2
#Imprimir números ímpares de 1 a 20 usando while:
i = 1
while i <= 20:
    print(i)
    i += 2

#Calcular a soma dos números de 1 a 100 usando while:
soma = 0 
i = 1
while i <= 100:
    soma += i
    i += 1
print(soma)


#Calcular a soma dos números pares de 1 a 100 usando while:
soma = 0
i = 2
while i <= 100:
    soma += i
print(soma)

#Calcular a soma dos números ímpares de 1 a 100 usando while:
soma = 0 
i = 1
while i <= 100:
    soma += i
    i += 2
print(soma)

#Imprimir a tabuada do 5 usando while:
i = 1
while i <= 10:
    print(f"5 x {i} = {5 * i}")
    i +=1

#Imprimir a tabuada de um número fornecido pelo usuário usando while:   
num = int(input("digite um número:"))
i = 1 
while i <= 10:
    print(f"{num} x {i} = {num * i}")

#Imprimir os números de 1 a 100, parando ao encontrar o número 50 usando while:
i = 1 
while i <= 100:
    if i == 50:
        break
    print(i)
    i= 1
#Imprimir os números de 1 a 100, pulando os múltiplos de 7 usando while:
i = 1 
while i <= 100:
    if i % 7 == 0:
        i += 1 
        continue
    print(i)
    i += 1
#Imprimir os números de 1 a 100, substituindo múltiplos de 3 por "Fizz" usando while:
i = 1
while i <= 100:
    if i % 3 == 0:
        print("fizz")
    else:
        print(i)
    i += 1
#Imprimir os números de 1 a 100, substituindo múltiplos de 5 por "Buzz" usando while:
i = 1
while i <= 100:
    if i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
#Imprimir os números de 1 a 100, substituindo múltiplos de 3 e 5 por "FizzBuzz" usando while
i = 1  
while i <= 100:
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else:
        print(i)
    i =+ 1

#Calcular o fatorial de um número usando while:
num = int (input("Digite um número: "))
fatorial = 1 
i = 1
while i <= num:
    fatorial *= i
    i += 1

print(f"Fatorial de {num} é {fatorial}")                                       



    




                
