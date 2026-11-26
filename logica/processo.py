from datetime import date

from logica.etapaProcesso import Triagem
from logica.observer import ObservadorProcesso

class RegistroEtapa:
    def __init__(self, nome_etapa, voluntario, data):
        self.__nome_etapa = nome_etapa
        self.__voluntario = voluntario
        self.__data = data

    #getters
    @property
    def nome_etapa(self):
        return self.__nome_etapa

    @property
    def voluntario(self):
        return self.__voluntario

    @property
    def data(self):
        return self.__data

    def mostrar_registro(self):
        return (f"Data: {self.__data} | Etapa: {self.__nome_etapa} | "
                f"Responsavel: {self.__voluntario.nome}")


class ProcessoAdocao:
    def __init__(self, codigo, adotante, animal, voluntario, data=None, observadores=None):
        self.__codigo = codigo
        self.__adotante = adotante
        self.__animal = animal
        self.__etapa_atual = Triagem()  # todo processo comeca na triagem
        self.__historico = []
        self.__observadores = []

        if observadores is not None:
                for observador in observadores:
                    self.adicionar_observador(observador)
                    
        # se nao passar a data, usa a de hoje
        if data is None:
            data = date.today().strftime("%d/%m/%Y")

        # o animal fica reservado enquanto o processo estiver aberto
        self.__animal.reservar()

        # ja registra a triagem com o voluntario que abriu o processo
        self.__registrar(voluntario, data)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def adotante(self):
        return self.__adotante

    @property
    def animal(self):
        return self.__animal

    @property
    def etapa_atual(self):
        return self.__etapa_atual

    @property
    def historico(self):
        return self.__historico.copy()

    def adicionar_observador(self, observador):
        if not isinstance(observador, ObservadorProcesso):
            raise TypeError("O observador deve herdar de ObservadorProcesso.")
        if observador not in self.__observadores:
            self.__observadores.append(observador)

    def remover_observador(self, observador):
        if observador in self.__observadores:
            self.__observadores.remove(observador)


    def avancar_etapa(self, voluntario, data=None):

        data = self.__obter_data(data)

        # padrao State: quem decide a proxima etapa é a etapa atual,
        # se ela for Aprovado ou Recusado lança ProcessoFinalizadoError
        self.__etapa_atual = self.__etapa_atual.proxima_etapa()

        self.__registrar(voluntario, data)

    #o valor de dta padrão foi definido como none para que caso a data não seja informada ela seja definida como a data de hoje.
    def recusar(self, voluntario, data=None):

        data = self.__obter_data(data)

        #mesma ideia do avancar, a etapa atual decide se pode ser recusada
        self.__etapa_atual = self.__etapa_atual.recusar()
        self.__registrar(voluntario, data)

        # recusou, entao o animal volta a poder ser adotado
        self.__animal.liberar()

    def __obter_data(self, data):
        if data is None:
            return date.today().strftime("%d/%m/%Y")
        return data

    def __registrar(self, voluntario, data):

        registro = RegistroEtapa(self.__etapa_atual.nome_etapa, voluntario, data)
        self.__historico.append(registro)

        self.__notificar_observadores()

    def __notificar_observadores(self):
        for observador in self.__observadores:
            observador.atualizar(self, self.__etapa_atual.nome_etapa)