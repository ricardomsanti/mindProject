



class Line:
    
    
    valor_resposta = ""
    
    def __init__(self, name, lista1 = {}):
        self.name = name
        self.lista1 = lista1
    
    def consulta(self, lista1):
        for x, y in self.lista1.items():
            valor_resposta = input(x)
            lista1.update({ x : valor_resposta})
        return lista1
    
    
    
#-----------------------------------------------------------------------------------------
valor_resposta = ""
l_mag = Line(name = "Maginificacao", lista1 = { "Você sente que pode haver uma emoção muito forte contribuindo para o que você está passando e pensando no momento? Se sim, não importa se ela \n" +
                "é positiva ou negativa. Por favor, digite 1 para sim ou 0 para não. \n"  : valor_resposta})



consulta = l_mag.consulta(lista1)




