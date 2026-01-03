# open() - é utilizada para abrir arquivos, w (write) escreve no arquivo, close fecha o arquivo
arquivo = open("teste.txt", "w")

arquivo.write("Curso Python\n")
arquivo.write("Funções\n")

arquivo.close()

#read - faz a leitura de todo o conteúdo do arquivo
leitura = open("teste.txt", "r")
print (leitura.read())
leitura.close()

#modo de leitura
# r - abre o arquivo para leitura, o arquivo ja deve existir
# r+ - abre o arquivo para leitura e escrita
# w - abre o arquivo somente para escrita, se o arquivo ja existir, ele apaga o conteudo anterior, se não cria um arquivo novo
# w+ - abre o arquivo para escrita e leitura, apagando o conteudo anterior
# a - abre o arquivo para escrita mas no final do arquivo, não apaga o conteudo anterior
# a+ - abre o arquivo para leitura e para escrita no final do arquivo
