import menu3


class UserInput():
             
        def asKAndReturnSearchTerm():
                return input('Digite um termo do Wikipedia ')
        
        def asKAndReturnPrefix():
                m = menu3.Menu(True)
                prefix = ["Quem é", "O que é",  "A historia de"]
                c = m.menu("Por favor selecione o prefixo", prefix, "Ou escolha, 'q' para sair ")
                return prefix[c - 1]