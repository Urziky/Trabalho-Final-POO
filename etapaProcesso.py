class Etapa:
    def __init__(self, nome_etapa):
        self._nome_etapa = nome_etapa

    @property
    def nome_etapa(self):
        return self._nome_etapa

    #verifica se foi finalizada ou não a etapa
    def finalizada(self):
        return False

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

    def finalizada(self):
        return True

    #uma forma de proteção, caso alguem tente chamar a proxima etapa de um processo aprovado, que nao existe
    def proxima_etapa(self):
        raise ValueError("O processo ja foi aprovado.")


class Recusado(Etapa):
    def __init__(self):
        super().__init__("Recusado")

    def finalizada(self):
        return True

    #gera um erro caso alguem tente chamar a proxima etapa de um processo recusado, que nao existe
    def proxima_etapa(self):
        raise ValueError("O processo foi recusado.")
