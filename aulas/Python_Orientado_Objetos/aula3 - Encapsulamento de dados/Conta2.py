class Conta2:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = 0
        self._limite = 0
        
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