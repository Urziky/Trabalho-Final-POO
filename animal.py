
from abc import ABC


class Animal(ABC):
    def __init__(self, codigo, nome, idade, porte,
                 vacinado, castrado):
        self._codigo = codigo
        self._nome = nome
        self._idade = idade
        self._porte = porte
        self._vacinado = vacinado
        self._castrado = castrado
        self._disponivel = True

    #codigo não possui setter para impedir que o valor seja alterado depois de criado
    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome inválido.")
        self._nome = valor.strip()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor < 0:
            raise ValueError("Idade inválida.")
        self._idade = valor

    @property
    def porte(self):
        return self._porte

    @porte.setter
    def porte(self, valor):
        if valor not in ("pequeno", "medio", "grande"):
            raise ValueError("Porte inválido.")
        self._porte = valor

    @property
    def vacinado(self):
        return self._vacinado

    @vacinado.setter
    def vacinado(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("Vacinado deve ser booleano.")
        self._vacinado = valor

    @property
    def castrado(self):
        return self._castrado

    @castrado.setter
    def castrado(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("Castrado deve ser booleano.")
        self._castrado = valor

    #os "setters" de disponivel, são reservar e liberar.
    @property
    def disponivel(self):
        return self._disponivel

    def reservar(self):
        if not self._disponivel:
            raise ValueError("Animal já está reservado.")
        self._disponivel = False

    def liberar(self):
        self._disponivel = True


class Cachorro(Animal):
    def __init__(self, codigo, nome, idade, porte,
                 vacinado, castrado):
        super().__init__(codigo, nome, idade, porte,
                         vacinado, castrado)


class Gato(Animal):
    def __init__(self, codigo, nome, idade, porte,
                 vacinado, castrado):
        super().__init__(codigo, nome, idade, porte,
                         vacinado, castrado)

