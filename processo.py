from etapaProcesso import Triagem

class RegistroEtapa:
    def __init__(self, nome_etapa, voluntario, data):
        self._nome_etapa = nome_etapa
        self._voluntario = voluntario
        self._data = data

    def mostrar_registro(self):
        return (f"Data: {self._data} | Etapa: {self._nome_etapa} | "
                f"Responsavel: {self._voluntario._nome}")

class ProcessoAdocao:
    def __init__(self, codigo, adotante, animal, voluntario):
        self._codigo = codigo
        self._adotante = adotante
        self._animal = animal
        self._etapa_atual = Triagem()#Triagem é a primeira etapa, mas pode ser alterada se preferirem
        self._historico = []

        #Ja deixa indisponivel quando o processo comeca
        self._animal._disponivel = False

    def avancar_etapa(self, voluntario, data):
        nova_etapa = self._etapa_atual.proxima_etapa()

        self._etapa_atual = nova_etapa

        novo_registro = RegistroEtapa(self._etapa_atual._nome_etapa, voluntario, data)