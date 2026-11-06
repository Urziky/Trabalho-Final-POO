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

