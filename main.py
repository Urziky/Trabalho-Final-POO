from datetime import date

from animal import Cachorro, Gato
from pessoa import Adotante, Voluntario
from filtroAnimal import FiltroAnimal
from ong import ONG


# Toda a parte de input e print fica aqui no Main
class Main:
    def __init__(self):
        self.ong = ONG("Patinhas do Bem")
        self.proximo_codigo_processo = 1

    def executar(self):
        print("=== Sistema de Adocao - " + self.ong.nome + " ===")

        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opcao: ").strip()

            if opcao == "0":
                print("Saindo...")
                break

            # os erros das regras de negocio vem da ONG como excecao,
            # aqui so mostramos a mensagem pro usuario
            try:
                if opcao == "1":
                    self.cadastrar_animal()
                elif opcao == "2":
                    self.cadastrar_adotante()
                elif opcao == "3":
                    self.cadastrar_voluntario()
                elif opcao == "4":
                    self.listar_animais_disponiveis()
                elif opcao == "5":
                    self.buscar_animais_com_filtro()
                elif opcao == "6":
                    self.abrir_processo()
                elif opcao == "7":
                    self.avancar_processo()
                elif opcao == "8":
                    self.recusar_processo()
                elif opcao == "9":
                    self.listar_processos()
                elif opcao == "10":
                    self.ver_historico()
                elif opcao == "11":
                    self.carregar_exemplos()
                else:
                    print("Opcao invalida.")
            except (ValueError, TypeError) as erro:
                print("Erro: " + str(erro))

    def mostrar_menu(self):
        print()
        print("1 - Cadastrar animal")
        print("2 - Cadastrar adotante")
        print("3 - Cadastrar voluntario")
        print("4 - Listar animais disponiveis")
        print("5 - Buscar animais com filtro")
        print("6 - Abrir processo de adocao")
        print("7 - Avancar etapa de um processo")
        print("8 - Recusar processo")
        print("9 - Listar processos")
        print("10 - Ver historico de um animal ou adotante")
        print("11 - Carregar dados de exemplo")
        print("0 - Sair")

    # cadastros

    def cadastrar_animal(self):
        especie = self.ler_opcao("Especie (cachorro/gato): ", ["cachorro", "gato"])
        codigo = self.ler_inteiro("Codigo: ")
        nome = self.ler_texto("Nome: ")
        idade = self.ler_inteiro("Idade: ")
        porte = self.ler_opcao("Porte (pequeno/medio/grande): ", ["pequeno", "medio", "grande"])
        vacinado = self.ler_sim_nao("Vacinado? (s/n): ")
        castrado = self.ler_sim_nao("Castrado? (s/n): ")

        if especie == "cachorro":
            animal = Cachorro(codigo, nome, idade, porte, vacinado, castrado)
        else:
            animal = Gato(codigo, nome, idade, porte, vacinado, castrado)

        self.ong.cadastrar_animal(animal)
        print(nome + " cadastrado.")

    def cadastrar_adotante(self):
        nome = self.ler_texto("Nome: ")
        cpf = self.ler_texto("CPF: ")
        telefone = self.ler_texto("Telefone: ")
        renda = self.ler_decimal("Renda mensal: ")
        moradia = self.ler_opcao("Moradia (casa/apartamento): ", ["casa", "apartamento"])

        adotante = Adotante(nome, cpf, telefone, renda, moradia)
        self.ong.cadastrar_adotante(adotante)
        print(adotante.papel() + " " + nome + " cadastrado.")

    def cadastrar_voluntario(self):
        nome = self.ler_texto("Nome: ")
        cpf = self.ler_texto("CPF: ")
        telefone = self.ler_texto("Telefone: ")

        voluntario = Voluntario(nome, cpf, telefone)
        self.ong.cadastrar_voluntario(voluntario)
        print(voluntario.papel() + " " + nome + " cadastrado.")

    # animais

    def listar_animais_disponiveis(self):
        animais = self.ong.buscar_animais()
        self.mostrar_animais(animais)

    def buscar_animais_com_filtro(self):
        print("Aperte Enter para nao usar o filtro.")
        especie = input("Especie (cachorro/gato): ").strip()
        porte = input("Porte (pequeno/medio/grande): ").strip()
        vacinado = self.ler_sim_nao_ou_vazio("Somente vacinados? (s/n): ")
        castrado = self.ler_sim_nao_ou_vazio("Somente castrados? (s/n): ")

        # campo vazio vira None, que no FiltroAnimal significa "nao filtrar"
        if especie == "":
            especie = None
        if porte == "":
            porte = None

        filtro = FiltroAnimal(especie, porte, vacinado, castrado)
        animais = self.ong.buscar_animais(filtro)
        self.mostrar_animais(animais)

    def mostrar_animais(self, animais):
        if len(animais) == 0:
            print("Nenhum animal encontrado.")
            return
        for animal in animais:
            print(self.texto_animal(animal))

    def texto_animal(self, animal):
        # cada animal sabe a propria especie, nao precisa de if
        especie = animal.especie()

        vacinado = "sim" if animal.vacinado else "nao"
        castrado = "sim" if animal.castrado else "nao"

        return (f"[{animal.codigo}] {animal.nome} - {especie}, {animal.idade} ano(s), "
                f"porte {animal.porte}, vacinado: {vacinado}, castrado: {castrado}")

    # processos 

    def abrir_processo(self):
        animais = self.ong.buscar_animais()
        adotantes = self.ong.listar_adotantes()
        voluntarios = self.ong.listar_voluntarios()

        if len(animais) == 0 or len(adotantes) == 0 or len(voluntarios) == 0:
            print("Precisa ter pelo menos um animal disponivel, um adotante e um voluntario.")
            return

        print("Adotantes:")
        for i, adotante in enumerate(adotantes):
            print(f"{i + 1} - {adotante.nome} (CPF {adotante.cpf})")
        adotante = adotantes[self.ler_indice(len(adotantes))]

        print("Animais disponiveis:")
        for i, animal in enumerate(animais):
            print(f"{i + 1} - {self.texto_animal(animal)}")
        animal = animais[self.ler_indice(len(animais))]

        voluntario = self.escolher_voluntario()

        processo = self.ong.abrir_processo(self.proximo_codigo_processo,
                                           adotante, animal, voluntario)
        self.proximo_codigo_processo += 1
        print(f"Processo {processo.codigo} aberto. Etapa atual: {processo.etapa_atual.nome_etapa}")

    def avancar_processo(self):
        processo = self.escolher_processo()
        if processo is None:
            return
        voluntario = self.escolher_voluntario()

        processo.avancar_etapa(voluntario, self.data_de_hoje())
        print(f"Processo {processo.codigo} agora esta na etapa {processo.etapa_atual.nome_etapa}")

    def recusar_processo(self):
        processo = self.escolher_processo()
        if processo is None:
            return
        voluntario = self.escolher_voluntario()

        processo.recusar(voluntario, self.data_de_hoje())
        print(f"Processo {processo.codigo} recusado.")

    def listar_processos(self):
        processos = self.ong.consultar_processos()
        if len(processos) == 0:
            print("Nenhum processo aberto.")
            return
        for processo in processos:
            print(self.texto_processo(processo))

    def ver_historico(self):
        tipo = self.ler_opcao("Ver historico de (animal/adotante): ", ["animal", "adotante"])

        if tipo == "animal":
            codigo = self.ler_inteiro("Codigo do animal: ")
            processos = []
            for processo in self.ong.consultar_processos():
                if processo.animal.codigo == codigo:
                    processos.append(processo)
        else:
            cpf = self.ler_texto("CPF do adotante: ")
            processos = []
            for processo in self.ong.consultar_processos():
                if processo.adotante.cpf == cpf:
                    processos.append(processo)

        if len(processos) == 0:
            print("Nenhum processo encontrado.")
            return

        for processo in processos:
            print(self.texto_processo(processo))
            if len(processo.historico) == 0:
                print("   (sem registros)")
            for registro in processo.historico:
                print("   " + registro.mostrar_registro())

    def texto_processo(self, processo):
        return (f"Processo {processo.codigo}: {processo.adotante.nome} -> "
                f"{processo.animal.nome} | etapa: {processo.etapa_atual.nome_etapa}")

    def escolher_processo(self):
        processos = self.ong.consultar_processos()
        if len(processos) == 0:
            print("Nenhum processo aberto.")
            return None

        print("Processos:")
        for i, processo in enumerate(processos):
            print(f"{i + 1} - {self.texto_processo(processo)}")
        return processos[self.ler_indice(len(processos))]

    def escolher_voluntario(self):
        voluntarios = self.ong.listar_voluntarios()
        print("Voluntario responsavel:")
        for i, voluntario in enumerate(voluntarios):
            print(f"{i + 1} - {voluntario.nome}")
        return voluntarios[self.ler_indice(len(voluntarios))]

    # dados de exemplo (pra demonstracao) 

    def carregar_exemplos(self):
        self.ong.cadastrar_animal(Cachorro(101, "Thor", 3, "grande", True, True))
        self.ong.cadastrar_animal(Cachorro(102, "Pipoca", 1, "pequeno", True, False))
        self.ong.cadastrar_animal(Gato(201, "Mingau", 2, "pequeno", True, True))
        self.ong.cadastrar_animal(Gato(202, "Frajola", 5, "medio", False, True))

        self.ong.cadastrar_adotante(Adotante("Ana Souza", "11111111111", "41999990001", 3500, "casa"))
        self.ong.cadastrar_adotante(Adotante("Bruno Lima", "22222222222", "41999990002", 2800, "apartamento"))

        self.ong.cadastrar_voluntario(Voluntario("Carla Mendes", "33333333333", "41999990003"))

        print("Exemplos carregados: 4 animais, 2 adotantes e 1 voluntario.")

    # leitura do teclado

    def ler_texto(self, mensagem):
        texto = input(mensagem).strip()
        while texto == "":
            print("Campo obrigatorio.")
            texto = input(mensagem).strip()
        return texto

    def ler_inteiro(self, mensagem):
        while True:
            try:
                numero = int(input(mensagem))
                if numero >= 0:
                    return numero
                print("O numero nao pode ser negativo.")
            except ValueError:
                print("Digite um numero inteiro.")

    def ler_decimal(self, mensagem):
        while True:
            try:
                # aceita virgula ou ponto (ex: 2500,50)
                numero = float(input(mensagem).replace(",", "."))
                if numero >= 0:
                    return numero
                print("O valor nao pode ser negativo.")
            except ValueError:
                print("Digite um numero valido.")

    def ler_opcao(self, mensagem, opcoes):
        resposta = input(mensagem).strip().lower()
        while resposta not in opcoes:
            print("Opcao invalida.")
            resposta = input(mensagem).strip().lower()
        return resposta

    def ler_sim_nao(self, mensagem):
        resposta = self.ler_opcao(mensagem, ["s", "n"])
        return resposta == "s"

    def ler_sim_nao_ou_vazio(self, mensagem):
        resposta = self.ler_opcao(mensagem, ["s", "n", ""])
        if resposta == "":
            return None
        return resposta == "s"

    def ler_indice(self, quantidade):
        # o usuario digita de 1 ate quantidade, mas a lista comeca no 0
        while True:
            try:
                numero = int(input("Numero: "))
                if 1 <= numero <= quantidade:
                    return numero - 1
            except ValueError:
                pass
            print(f"Digite um numero entre 1 e {quantidade}.")

    def data_de_hoje(self):
        return date.today().strftime("%d/%m/%Y")


if __name__ == "__main__":
    Main().executar()
