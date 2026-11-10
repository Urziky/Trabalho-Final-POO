from datetime import date

from etapaProcesso import Triagem, Recusado, Aprovado


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
    def __init__(self, codigo, adotante, animal, voluntario, data=None):
        self.__codigo = codigo
        self.__adotante = adotante
        self.__animal = animal
        self.__etapa_atual = Triagem()  # todo processo comeca na triagem
        self.__historico = []

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

    #caso a data nao seja passada, sera definida como a data de hoje
    def avancar_etapa(self, voluntario, data=None):

        #verificação caso a etapa ja tenha sido finalizada.
        if self.__etapa_atual.finalizada():
            raise ValueError("Esse processo ja foi finalizado.")

        #define a data do registro da nova etapa, caso nao seja passada a data, define como a data de hoje.
        if data is None:
            data = date.today().strftime("%d/%m/%Y")

        
        # se a etapa atual for Aprovado ou Recusado, proxima_etapa() da erro
        self.__etapa_atual = self.__etapa_atual.proxima_etapa()

        self.__registrar(voluntario, data)
        # quando chega em Aprovado o animal continua indisponivel (foi adotado)
    
    #o valor de dta padrão foi definido como none para que caso a data não seja informada ela seja definida como a data de hoje.
    def recusar(self, voluntario, data=None):
        if self.__etapa_atual.finalizada():
            raise ValueError("Esse processo ja foi finalizado.")

        if data is None:
            data = date.today().strftime("%d/%m/%Y")

        self.__etapa_atual = Recusado()
        self.__registrar(voluntario, data)

        # recusou, entao o animal volta a poder ser adotado
        self.__animal.liberar()

    def __registrar(self, voluntario, data):

        registro = RegistroEtapa(self.__etapa_atual.nome_etapa, voluntario, data)
        self.__historico.append(registro)

