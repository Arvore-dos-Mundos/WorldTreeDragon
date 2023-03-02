class Iniciativa:
    def __init__(self):
        self.list_nome = []
        self.list_iniciativa = []
    
    def adicionar(self, nome, iniciativa):
        self.list_nome.append(nome)
        self.list_iniciativa.append(iniciativa)
    
    def mostrar(self):
        mensagem: str
        for x in range(len(self.list_name)):
            mensagem += f"ID: {x} - {self.list_name[x]} - INICIATIVA: {self.list_iniciativa[x]}"
        
        return mensagem