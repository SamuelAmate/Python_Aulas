class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1= Cliente("Samuel", "11999999999")
conta=Conta(6565,c1.get_nome,0,1000)

conta.depositar(400)
conta.saque(110)
conta.extrato()