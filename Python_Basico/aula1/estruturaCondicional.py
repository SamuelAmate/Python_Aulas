#Estrutura condicional simples
idade = int(input("Digite a idade da pessoa: "))

if idade > 18:
    print("A pessoa é maior de idade")
else:
    print("A pessoa é menor de idade")
    
A = input("Digite o valor de A: ")
B = input("Digite o valor de B: ")

if (A > B):
    aux = A;
    A = B;
    B = aux;
print("Após a troca, o valor de A é: ", A)
print("Após a troca, o valor de B é: ", B)

#Estrutura condicional composta
notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

mediafinal = (notaA + notaB) / 2

if mediafinal >= 7:
    print("O aluno foi aprovado com média final:", mediafinal)
else:
    print("O aluno foi reprovado com média final:", mediafinal)
    
    
#Estrutura idade composta
idade = int(input("Digite a idade da pessoa: "))

if idade > 18:
    print("A pessoa é maior de idade")
elif idade > 16:
    print("A pessoa é infanto juvenil")
else:
    print("A pessoa é menor de idade")