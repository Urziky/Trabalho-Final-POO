from abc import ABC, abstractmethod

from logica.excecoes import ProcessoFinalizadoError


#padrao State: cada etapa é um estado do processo de adoção
#o ProcessoAdocao guarda a etapa atual e pergunta pra ela o que fazer,
#assim cada etapa decide se pode avançar ou ser recusada
class Etapa(ABC):
    def __init__(self, nome_etapa):
        self.__nome_etapa = nome_etapa

    @property
    def nome_etapa(self):
        return self.__nome_etapa

    #verifica se foi finalizada ou não a etapa
    def finalizada(self):
        return False

    #cada etapa diz qual é a proxima
    @abstractmethod
    def proxima_etapa(self):
        pass

    #por padrao qualquer etapa em andamento pode ser recusada,
    #só Aprovado e Recusado mudam isso
    def recusar(self):
        return Recusado()


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

    #processo aprovado nao tem proxima etapa
    def proxima_etapa(self):
        raise ProcessoFinalizadoError("O processo ja foi aprovado, nao tem proxima etapa.")

    #e tambem nao pode mais ser recusado, o animal ja foi adotado
    def recusar(self):
        raise ProcessoFinalizadoError("O processo ja foi aprovado, nao pode ser recusado.")


class Recusado(Etapa):
    def __init__(self):
        super().__init__("Recusado")

    def finalizada(self):
        return True

    #processo recusado nao tem proxima etapa
    def proxima_etapa(self):
        raise ProcessoFinalizadoError("O processo foi recusado, nao tem proxima etapa.")

    #nao da pra recusar duas vezes
    def recusar(self):
        raise ProcessoFinalizadoError("O processo ja foi recusado.")
