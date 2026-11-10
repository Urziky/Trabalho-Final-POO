from datetime import date

from etapaProcesso import Triagem, Recusado, Aprovado


class RegistroEtapa:
    def __init__(self, nome_etapa, voluntario, data):
        self._nome_etapa = nome_etapa
        self._voluntario = voluntario
        self._data = data

    #getters
    @property
    def nome_etapa(self):
        return self._nome_etapa

    @property
    def voluntario(self):
        return self._voluntario

    @property
    def data(self):
        return self._data

    def mostrar_registro(self):
        return (f"Data: {self._data} | Etapa: {self._nome_etapa} | "
                f"Responsavel: {self._voluntario.nome}")


class ProcessoAdocao:
    def __init__(self, codigo, adotante, animal, voluntario, data=None):
        self._codigo = codigo
        self._adotante = adotante
        self._animal = animal
        self._etapa_atual = Triagem()  # todo processo comeca na triagem
        self._historico = []

        # se nao passar a data, usa a de hoje
        if data is None:
            data = date.today().strftime("%d/%m/%Y")

        # o animal fica reservado enquanto o processo estiver aberto
        self._animal.reservar()

        # ja registra a triagem com o voluntario que abriu o processo
        self._registrar(voluntario, data)

    @property
    def codigo(self):
        return self._codigo

    @property
    def adotante(self):
        return self._adotante

    @property
    def animal(self):
        return self._animal

    @property
    def etapa_atual(self):
        return self._etapa_atual

    @property
    def historico(self):
        return self._historico.copy()

    #caso a data nao seja passada, sera definida como a data de hoje
    def avancar_etapa(self, voluntario, data=None):

        #verificação caso a etapa ja tenha sido finalizada.
        if self._etapa_atual.finalizada():
            raise ValueError("Esse processo ja foi finalizado.")

        #define a data do registro da nova etapa, caso nao seja passada a data, define como a data de hoje.
        if data is None:
            data = date.today().strftime("%d/%m/%Y")

        
        # se a etapa atual for Aprovado ou Recusado, proxima_etapa() da erro
        self._etapa_atual = self._etapa_atual.proxima_etapa()

        self._registrar(voluntario, data)
        # quando chega em Aprovado o animal continua indisponivel (foi adotado)
    
    #o valor de dta padrão foi definido como none para que caso a data não seja informada ela seja definida como a data de hoje.
    def recusar(self, voluntario, data=None):
        if self._etapa_atual.finalizada():
            raise ValueError("Esse processo ja foi finalizado.")

        if data is None:
            data = date.today().strftime("%d/%m/%Y")

        self._etapa_atual = Recusado()
        self._registrar(voluntario, data)

        # recusou, entao o animal volta a poder ser adotado
        self._animal.liberar()

    def _registrar(self, voluntario, data):

        registro = RegistroEtapa(self._etapa_atual.nome_etapa, voluntario, data)
        self._historico.append(registro)

