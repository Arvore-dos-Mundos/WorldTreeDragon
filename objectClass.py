class Iniciativa:
    def __init__(self):
        self.iniciativas = {}

    def adicionar(self, _nome, _iniciativa):
        self.list_nome.append(_nome)
        self.list_iniciativa.append(_iniciativa)

    def mostrar(self, chat_id):
        mensagem = ""
        iniciativas = sorted(self.iniciativas.get(chat_id, []), key=lambda x: x[1], reverse=True)
        for i, (nome, iniciativa) in enumerate(iniciativas):
            mensagem += "{:2d}  {:<10}  [{:2d}]\n".format(i, nome, iniciativa)
        if not mensagem:
            mensagem = "Não há iniciativas nesse chat."
        return mensagem

    def adicionar_iniciativa_chat(self, chat_id, nome, iniciativa):
        if chat_id not in self.iniciativas:
            self.iniciativas[chat_id] = []
        self.iniciativas[chat_id].append((nome, iniciativa))
        self.iniciativas[chat_id] = sorted(self.iniciativas[chat_id], key=lambda x: x[1])
        
    