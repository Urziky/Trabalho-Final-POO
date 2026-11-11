from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.__cpf = cpf
        self.telefone = telefone

    #getters e setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome inválido.")
        self.__nome = valor.strip()

    #cpf não possui setter porque ele serve como identificador da pessoa
    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Telefone inválido.")
        self.__telefone = valor.strip()

    #cada subclasse informa o papel da pessoa na ONG (polimorfismo)
    @abstractmethod
    def papel(self):
        pass


class Adotante(Pessoa):
    def __init__(self, nome, cpf, telefone, renda, moradia):
        super().__init__(nome, cpf, telefone)
        self.renda = renda
        self.moradia = moradia

    #getters e setters
    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("Renda inválida.")
        self.__renda = valor

    @property
    def moradia(self):
        return self.__moradia

    @moradia.setter
    def moradia(self, valor):
        if valor not in ("casa", "apartamento"):
            raise ValueError("Moradia inválida, deve ser casa ou apartamento.")
        self.__moradia = valor

    def papel(self):
        return "Adotante"


class Voluntario(Pessoa):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

    def papel(self):
        return "Voluntario"
