from abc import ABC, abstractmethod


#O ProcessoAdocao avisa sobre mudanças de etapa sem precisar saber
# como a notificação será tratada ou exibida.
class ObservadorProcesso(ABC):
    @abstractmethod
    def atualizar(self, processo, etapa):
        pass


class NotificadorAdotante(ObservadorProcesso):

    #Guarda as mensagens de aviso
    def __init__(self):
        self.__notificacoes = []

    @property
    def notificacoes(self):
        return self.__notificacoes.copy()

    def ultima_notificacao(self):
        if not self.__notificacoes:
            return None
        return self.__notificacoes[-1]

    def atualizar(self, processo, etapa):
        mensagem = (
            f"Aviso para {processo.adotante.nome}: "
            f"processo {processo.codigo} ({processo.animal.nome}) "
            f"esta na etapa '{etapa}'."
        )
        self.__notificacoes.append(mensagem)