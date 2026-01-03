codigo = 10
salario = 1500
nome = "Samuel"
situacao = True
tipo = type(codigo)

print(tipo)
print(salario)

print("Código: ", codigo, "Nome: ", nome, "Salário: ", salario, "Situação: ", situacao) #Concatenação com ,
print("Código: " + str(codigo) + " Nome: " + nome + " Salário: " + str(salario) + " Situação: " + str(situacao)) #Concatenação com +
print(f"Código: {codigo} Nome: {nome} Salário: {salario} Situação: {situacao}")  #Concatenação com f"" - String Formatada  
