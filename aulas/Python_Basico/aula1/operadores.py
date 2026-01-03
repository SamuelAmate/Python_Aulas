#Operadores Aritméticos

soma = 10 + 5
print(soma)

subtracao = 10 - 5
print(subtracao)

multiplicacao = 10 * 5
print(multiplicacao)

divisaoReal = 10 / 5
print(divisaoReal)

divisaoInteira = 10 // 3
print(divisaoInteira)

exponenciacao = 2 ** 3
print(exponenciacao)

modulo = 10 % 3
print(modulo)

#Operadores Relacionais - Retornam True ou False

igual = 10 == 5
print(igual)

diferente = 10 != 5
print(diferente)

maior = 10 > 5
print(maior)

menor = 10 < 5
print(menor)

maiorIgual = 10 >= 5
print(maiorIgual)

menorIgual = 10 <= 5
print(menorIgual)

#Operadores Lógicos - São utilizados para combinar expressões lógicas, retornando True ou False

#Operador AND - retorna true se ambas as expressões forem verdadeiras
#Operador OR - retorna true se pelo menos uma das expressões for verdadeira
#Operador NOT - inverte o resultado da expressão, se for true retorna false e vice-versa
#Exemplos

A = 5
B = 10
C = 20

print(A > B and C > B) #And - False
print(A < B and C > B) #And - True

print(A > B or C < B)  #Or - False
print(A > B or C > B)  #Or - True

print(not(A < B and C > B))  #Not - False
print(not(A > B and C > B))  #Not - True