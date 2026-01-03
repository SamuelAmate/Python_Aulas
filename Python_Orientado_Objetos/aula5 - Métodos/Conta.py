class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = 0
        self._limite = 0
        
    def depositar(self, valor):
        self._saldo += valor
        
    def extrato(self):
        print(f"Cliente: {self._titular} - Saldo: {self._saldo}")
        
    def saque(self, valor):
        if (self._saldo < valor):
            print("Saldo insuficiente para saque")
        else:
            self._saldo -= valor
        
        def get_saldo(self):
            return self._saldo
        
        def set_saldo(self, saldo):
            if (saldo<0):
                print("Saldo não pode ser negativo")
            else:
                self._saldo = saldo
                
                
        #Property
        @property
        def saldo(self):
            return self._saldo
        
        @saldo.setter
        def saldo(self, saldo):
            if (saldo<0):
                print("Saldo não pode ser negativo")
            else:
                self._saldo = saldo