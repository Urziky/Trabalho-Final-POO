from abc import ABC, abstractmethod

class Etapa(ABC):
    def __init__(self, nome_etapa):
        self.__nome_etapa = nome_etapa

    @property
    def nome_etapa(self):
        return self.__nome_etapa

    #verifica se foi finalizada ou não a etapa
    def finalizada(self):
        return False

    @abstractmethod
    def proxima_etapa(self):
        pass

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
