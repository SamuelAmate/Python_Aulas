codigo = 10
salario = 1500
nome = "Samuel"
situacao = True
tipo = type(codigo)

#Int (inteiro) - %d ou %i
#Float ou Double (decimal) - %f 
#Long Int (inteiro longo) - %Id
#Float e Double (numero exponencial) - %e ou %E
#Char (um caractere) - %c
#Char (varios caracteres) - %s
#Octal (inteiro em formato octal) - %o
#Hexadecimal (inteiro em formato hexadecimal) - %x ou %X
#Boolean (True ou False) - %r

#Exemplo

print("Código: %d Nome: %s Salário: %.2f Situação: %r" % (codigo, nome, salario, situacao))