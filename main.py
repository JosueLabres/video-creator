import menu3


class start():
    def __init__(self):
        searchTerm = self.asKAndReturnSearchTerm()
        prefix = self.asKAndReturnPrefix()
        print(prefix)

    def asKAndReturnSearchTerm(self):
        return input('Digite um termo do Wikipedia ')
    
    def asKAndReturnPrefix(self):
        m = menu3.Menu(True)
        prefix = ["Quem é", "O que é",  "A historia de"]
        c = m.menu("Por favor selecione o prefixo", prefix, "Ou escolha, 'q' para sair ")
        return prefix[c - 1]

start()
