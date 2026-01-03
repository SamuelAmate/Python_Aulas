class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1= Cliente("Samuel", "11999999999")
conta=Conta(6565,c1.nome,0,1000)

print(f"Titular: {conta.titular} - Numero da conta: {conta.numero} - Saldo: {conta.saldo} - Limite: {conta.limite}")