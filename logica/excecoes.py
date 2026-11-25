
class AnimalJaCadastradoError(ValueError):
    """Erro ao tentar cadastrar o animal, já existe um animal com esse código."""
    pass


class ProcessoFinalizadoError(ValueError):
    """Erro ao tentar avançar ou recusar um processo que já foi aprovado ou recusado."""
    pass
