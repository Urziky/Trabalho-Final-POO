from animal import Animal
from pessoa import Adotante, Voluntario
from processo import ProcessoAdocao
from filtroAnimal import FiltroAnimal


class ONG:
    """Centraliza cadastros, consultas e abertura de processos de adocao."""

    def __init__(self, nome):
        self._nome = nome
        self._animais = []
        self._adotantes = []
        self._voluntarios = []
        self._processos = []

    @property
    def nome(self):
        return self._nome

    
    def cadastrar_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("E necessario informar um animal.")
        
        if any(a.codigo == animal.codigo for a in self._animais):
            raise ValueError("Ja existe um animal com esse codigo.")
        
        self._animais.append(animal)

    def cadastrar_adotante(self, adotante):
        if not isinstance(adotante, Adotante):
            raise TypeError("E necessario informar um adotante.")
        
        if any(a.cpf == adotante.cpf for a in self._adotantes):
            raise ValueError("Esse CPF ja esta cadastrado como adotante.")
        
        self._adotantes.append(adotante)

    def cadastrar_voluntario(self, voluntario):
        if not isinstance(voluntario, Voluntario):
            raise TypeError("E necessario informar um voluntario.")
        
        if any(v.cpf == voluntario.cpf for v in self._voluntarios):
            raise ValueError("Esse CPF ja esta cadastrado como voluntario.")
        
        self._voluntarios.append(voluntario)

    def buscar_animais(self, filtro=None):
        """Lista apenas animais disponiveis; aplica um filtro, se informado."""
        if filtro is not None and not isinstance(filtro, FiltroAnimal):
            raise TypeError("O filtro deve ser um FiltroAnimal.")
        
        return [
            animal for animal in self._animais
            if animal.disponivel and (filtro is None or filtro.corresponde(animal))
        ]

    def abrir_processo(self, codigo, adotante, animal, voluntario):
        if any(p.codigo == codigo for p in self._processos):
            raise ValueError("Ja existe um processo com esse codigo.")
        
        if adotante not in self._adotantes:
            raise ValueError("O adotante nao esta cadastrado nesta ONG.")
        
        if animal not in self._animais:
            raise ValueError("O animal nao esta cadastrado nesta ONG.")
        
        if voluntario not in self._voluntarios:
            raise ValueError("O voluntario nao esta cadastrado nesta ONG.")
        
        if not animal.disponivel:
            raise ValueError("O animal ja esta em processo de adocao ou foi adotado.")

        processo = ProcessoAdocao(codigo, adotante, animal, voluntario)

        self._processos.append(processo)

        return processo

    def consultar_processos(self, animal=None, adotante=None):
        """Consulta processos por animal e/ou adotante, inclusive antigos."""

        return [
            processo for processo in self._processos
            if (animal is None or processo.animal is animal)
            and (adotante is None or processo.adotante is adotante)
        ]

    def listar_adotantes(self):
        return self._adotantes.copy()

    def listar_voluntarios(self):
        return self._voluntarios.copy()
