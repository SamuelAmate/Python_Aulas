#Funcao basica
def mensagem1():
    print("Esta é a mensagem 1")
    
    
def mensagem2():
    print("Esta é a mensagem 2")
    
    
mensagem1()

texto =  mensagem2()
print(texto)

#media de notas com funções

def lernotas():
    nota = float(input("Digite a nota: "))
    return nota


def resultado(nota1,nota2):
    media = (nota1 + nota2) / 2
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media} Resultado: ', end=' ')
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
        
        
a = lernotas()
b = lernotas()
resultado(a,b)
        