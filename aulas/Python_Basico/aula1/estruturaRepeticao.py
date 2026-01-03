# For básico
for x in range(10):
    print(f'Valor de x é {x}')
    
#Definindo valor inicial
for x in range(5,10):
    print(f'Valor de x é {x}')

#For em orden decrescente
for x in range(10,0,-1):
    print(f'Valor de x é {x}')
    
#While básico
y = 1;
while y < 10:
    print(f'Valor de y é {y}')
    y += 1
    
#Media de valores usando while
qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor >= 0:
    soma = soma + valor
    qtd += 1
    valor = float(input("Digite um valor: "))
    
media = soma / qtd
print(f'\n Total da soma : {soma}')
print(f'Quantidade de valores somados: {qtd}')
print(f'Média dos valores: {media}')