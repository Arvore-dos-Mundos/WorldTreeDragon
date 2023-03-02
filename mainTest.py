from objectClass import Iniciativa

arroz = Iniciativa()

arroz.adicionar("Ferh", 32)
arroz.adicionar("Ferh2", 12)
arroz.adicionar("Ferh3", 52)
arroz.adicionar("Ferh4", 72)

mensagem = arroz.mostrar()

print(mensagem)