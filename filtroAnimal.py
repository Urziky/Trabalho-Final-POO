from animal import Cachorro, Gato


class FiltroAnimal:
    """Guarda os criterios usados na busca de animais da ONG."""

    def __init__(self, especie=None, porte=None, vacinado=None, castrado=None):
        # Um criterio igual a None significa que ele nao sera aplicado.
        especies_validas = {"cachorro", "cao", "cao", "gato"}
        if especie is not None:
            especie = especie.strip().lower()
            if especie not in especies_validas:
                raise ValueError("Especie deve ser cachorro ou gato.")

        self._especie = especie
        self._porte = porte.strip().lower() if porte is not None else None
        self._vacinado = vacinado
        self._castrado = castrado

    def corresponde(self, animal):
        """Retorna True quando o animal atende a todos os criterios."""
        if self._especie in ("cachorro", "cao", "cao"):
            if not isinstance(animal, Cachorro):
                return False
        elif self._especie == "gato":
            if not isinstance(animal, Gato):
                return False

        if self._porte is not None and animal._porte.lower() != self._porte:
            return False
        if self._vacinado is not None and animal._vacinado != self._vacinado:
            return False
        if self._castrado is not None and animal._castrado != self._castrado:
            return False

        return True
