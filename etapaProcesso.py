
class Etapa:
    def __init__(self, nome_etapa):
        self._nome_etapa = nome_etapa

class Triagem(Etapa):
    def __init__(self):
        super().__init__("Triagem")

    def proxima_etapa(self):
        return Entrevista() 

class Entrevista(Etapa):
    def __init__(self):
        super().__init__("Entrevista")

    def proxima_etapa(self):
        return Visita()

class Visita(Etapa):
    def __init__(self):
        super().__init__("Visita")

    def proxima_etapa(self):
        return Aprovado()

#tenho que fazer a logica de aprovado e recusado ainda, mas defini as proximas etapas so pra saberem qual vai depois de qual
#(Ou mudarem se quiserem)
class Aprovado(Etapa):
    def __init__(self):
        super().__init__("Aprovado")

class Recusado(Etapa):
    def __init__(self):
        super().__init__("Recusado")