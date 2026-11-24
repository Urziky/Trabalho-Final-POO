from logica.animal import Cachorro, Gato

#classe responsável por criar os animais de acordo com a espécie
#caso alguma outra especie fosse adicionada, ao invés de alterar o código de varios arquivos só precisa alterar esse.
class CriaAnimal:

    @staticmethod
    #a função chama o construtor de acordo com a especie passada.
    def criar_animal(especie, codigo, nome, idade,
                     porte, vacinado, castrado):

        #antes essa parte ficava na interface mas agora foi movida pra cá
        if especie == "cachorro":
            return Cachorro(
                codigo, nome, idade, porte, vacinado, castrado
            )

        elif especie == "gato":
            return Gato(
                codigo, nome, idade, porte, vacinado, castrado
            )

        else:
            raise ValueError("Espécie não suportada.")