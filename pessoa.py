class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

class Adotante(Pessoa):

    def __init__(self, nome, cpf, telefone,
                 renda, moradia):
        super().__init__(nome, cpf, telefone)

        self._renda = renda
        self._moradia = moradia

class Voluntario(Pessoa):

    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

