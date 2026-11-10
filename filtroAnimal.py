from animal import Animal, Cachorro, Gato


class FiltroAnimal:
    """Guarda os criterios usados na busca de animais da ONG."""

    def __init__(self, especie=None, porte=None, vacinado=None, castrado=None):

        # Um criterio igual a None significa que ele nao sera aplicado.
        especies_validas = {"cachorro", "cao", "gato"}

        #verifica se os parametros passados sao validos
        if especie is not None:
            if not isinstance(especie, str):
                raise TypeError("Especie deve ser um texto.")

            especie = especie.strip().lower()

            if especie not in especies_validas:
                raise ValueError("Especie deve ser cachorro ou gato.")

        if porte is not None:
            if not isinstance(porte, str):
                raise TypeError("Porte deve ser um texto.")

            porte = porte.strip().lower()

            if porte not in ("pequeno", "medio", "grande"):
                raise ValueError("Porte invalido.")

        if vacinado is not None and not isinstance(vacinado, bool):
            raise TypeError("Vacinado deve ser booleano(true ou false).")

        if castrado is not None and not isinstance(castrado, bool):
            raise TypeError("Castrado deve ser booleano(true ou false).")

        self._especie = especie
        self._porte = porte
        self._vacinado = vacinado
        self._castrado = castrado

    #getters
    @property
    def especie(self):
        return self._especie

    @property
    def porte(self):
        return self._porte

    @property
    def vacinado(self):
        return self._vacinado

    @property
    def castrado(self):
        return self._castrado

    def corresponde(self, animal):
        """Retorna True quando o animal atende a todos os criterios."""

        #verifica se o animal é uma instancia da classe Animal
        if not isinstance(animal, Animal):
            raise TypeError("E necessario informar um animal.")
        
        if self._especie in ("cachorro", "cao"):
            if not isinstance(animal, Cachorro):
                return False
            
        elif self._especie == "gato":
            if not isinstance(animal, Gato):
                return False

        if self._porte is not None and animal.porte.lower() != self._porte:
            return False
        if self._vacinado is not None and animal.vacinado != self._vacinado:
            return False
        if self._castrado is not None and animal.castrado != self._castrado:
            return False

        return True
