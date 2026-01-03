class Cliente:
    def __init__(self, nome, idade):
        
        self._nome = nome
        self.idade = idade
        
    #Get
    def get_nome(self):
        return self._nome
    
    #Set
    def set_nome(self, nome):
        self._nome = nome
