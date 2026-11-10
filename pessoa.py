
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self._cpf = cpf
        self.telefone = telefone

    #getters e setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome inválido.")
        self._nome = valor.strip()

    #cpf não possui setter porque ele serve como identificador da pessoa
    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Telefone inválido.")
        self._telefone = valor.strip()


class Adotante(Pessoa):
    def __init__(self, nome, cpf, telefone, renda, moradia):
        super().__init__(nome, cpf, telefone)
        self.renda = renda
        self.moradia = moradia

    #getters e setters
    @property
    def renda(self):
        return self._renda

    @renda.setter
    def renda(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("Renda inválida.")
        self._renda = valor

    @property
    def moradia(self):
        return self._moradia

    @moradia.setter
    def moradia(self, valor):
        if valor not in ("casa", "apartamento"):
            raise ValueError("Moradia inválida, deve ser casa ou apartamento.")
        self._moradia = valor


class Voluntario(Pessoa):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)
