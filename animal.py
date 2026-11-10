
from abc import ABC


class Animal(ABC):
    def __init__(self, codigo, nome, idade, porte,
                 vacinado, castrado):
        self._codigo = codigo
        self.nome = nome
        self.idade = idade
        self.porte = porte
        self.vacinado = vacinado
        self.castrado = castrado
        self.__disponivel = True

    #codigo não possui setter para impedir que o valor seja alterado depois de criado
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome inválido.")
        self.__nome = valor.strip()

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor < 0:
            raise ValueError("Idade inválida.")
        self.__idade = valor

    @property
    def porte(self):
        return self.__porte

    @porte.setter
    def porte(self, valor):
        if valor not in ("pequeno", "medio", "grande"):
            raise ValueError("Porte inválido.")
        self.__porte = valor

    @property
    def vacinado(self):
        return self.__vacinado

    @vacinado.setter
    def vacinado(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("Vacinado deve ser booleano.")
        self.__vacinado = valor

    @property
    def castrado(self):
        return self.__castrado

    @castrado.setter
    def castrado(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("Castrado deve ser booleano.")
        self.__castrado = valor

    #os "setters" de disponivel, são reservar e liberar.
    @property
    def disponivel(self):
        return self.__disponivel

    def reservar(self):
        if not self.__disponivel:
            raise ValueError("Animal já está reservado.")
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True


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

