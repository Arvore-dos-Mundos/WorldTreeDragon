


class Iniciativa:
    def __init__(self):
        self.list_nome = []
        self.list_iniciativa = []
    
    def adicionar(self, _nome, _iniciativa):
        self.list_nome.append(_nome)
        self.list_iniciativa.append(_iniciativa)
    
    def mostrar(self):
        mensagem = ""
        for x in range(len(self.list_nome)):
            mensagem += f"ID: {x} - {self.list_nome[x]} - INICIATIVA: {self.list_iniciativa[x]}\n"     
        return mensagem