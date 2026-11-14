import tkinter as tk
from tkinter import messagebox

from animal import Cachorro, Gato
from pessoa import Adotante, Voluntario
from ong import ONG


class interface:
    def __init__(self):
        #Nome aleatório, podem trocar aqui depois
        self.ong = ONG("Doação do Luizão")

        #Tela principal
        self.janela = tk.Tk()
        self.janela.title("Sistema de Adocao - " + self.ong.nome)
        self.janela.geometry("350x300")

        #Cria um texto na parte de cuma da janela
        titulo = tk.Label(self.janela, text="=== Sistema de Adocao - " + self.ong.nome + " ===")
        titulo.pack(pady=10)

        #Primeiros botoes chamando as devidas funcoes
        tk.Button(self.janela, text="1 - Cadastrar animal", width=35, command=self.cadastrar_animal).pack(pady=3)
        tk.Button(self.janela, text="2 - Cadastrar adotante", width=35, command=self.cadastrar_adotante).pack(pady=3)
        tk.Button(self.janela, text="3 - Cadastrar voluntario", width=35, command=self.cadastrar_voluntario).pack(pady=3)
        tk.Button(self.janela, text="4 - Listar animais disponiveis", width=35, command=self.listar_animais_disponiveis).pack(pady=3)
        #Fiz essa para nós não termos que ficar cadastrando no meio do sprint e dar tempo de apresentar
        tk.Button(self.janela, text="5 - Carregar dados prontos", width=35, command=self.carregar_exemplos).pack(pady=3)
        tk.Button(self.janela, text="0 - Sair", width=35, command=self.janela.destroy).pack(pady=10)

    def executar(self):
        self.janela.mainloop()

    # Cadastros dos animais
    def cadastrar_animal(self):
        #Isso abre a janela secundaria
        tela = tk.Toplevel(self.janela)
        tela.title("Cadastrar Animal")
        tela.geometry("300x380")

        #Cada tk.label cria o texto, e cada ent cria a entrada de texto
        tk.Label(tela, text="Especie (cachorro/gato):").pack()
        ent_especie = tk.Entry(tela)
        ent_especie.pack()

        tk.Label(tela, text="Codigo (numero):").pack()
        ent_codigo = tk.Entry(tela)
        ent_codigo.pack()

        tk.Label(tela, text="Nome:").pack()
        ent_nome = tk.Entry(tela)
        ent_nome.pack()

        tk.Label(tela, text="Idade (numero):").pack()
        ent_idade = tk.Entry(tela)
        ent_idade.pack()

        tk.Label(tela, text="Porte (pequeno/medio/grande):").pack()
        ent_porte = tk.Entry(tela)
        ent_porte.pack()

        tk.Label(tela, text="Vacinado? (s/n):").pack()
        ent_vacinado = tk.Entry(tela)
        ent_vacinado.pack()

        tk.Label(tela, text="Castrado? (s/n):").pack()
        ent_castrado = tk.Entry(tela)
        ent_castrado.pack()

        #Função para salvar o que foi escrito
        def salvar():
            try:
                especie = ent_especie.get().strip().lower()
                if especie not in ["cachorro", "gato"]:
                    raise ValueError("Especie deve ser cachorro ou gato.")

                codigo = int(ent_codigo.get().strip())
                if codigo < 0:
                    raise ValueError("O codigo nao pode ser negativo.")

                nome = ent_nome.get().strip()
                idade = int(ent_idade.get().strip())
                porte = ent_porte.get().strip().lower()

                vac_txt = ent_vacinado.get().strip().lower()
                cas_txt = ent_castrado.get().strip().lower()
                if vac_txt not in ["s", "n"] or cas_txt not in ["s", "n"]:
                    raise ValueError("Digite 's' ou 'n' para vacinado e castrado.")

                vacinado = (vac_txt == "s")
                castrado = (cas_txt == "s")

                if especie == "cachorro":
                    animal = Cachorro(codigo, nome, idade, porte, vacinado, castrado)
                else:
                    animal = Gato(codigo, nome, idade, porte, vacinado, castrado)

                #Manda o animal pra ser cadastrado
                self.ong.cadastrar_animal(animal)
                messagebox.showinfo("Sucesso no cadastro de ", nome )
                tela.destroy()
            #O except pra calcular os erros, inclusive caso tenha algum das funcoes que foram chamadas
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Salvar", command=salvar).pack(pady=10)

    def cadastrar_adotante(self):
        tela = tk.Toplevel(self.janela)
        tela.title("Cadastrar Adotante")
        tela.geometry("300x300")

        tk.Label(tela, text="Nome:").pack()
        ent_nome = tk.Entry(tela)
        ent_nome.pack()

        tk.Label(tela, text="CPF:").pack()
        ent_cpf = tk.Entry(tela)
        ent_cpf.pack()

        tk.Label(tela, text="Telefone:").pack()
        ent_telefone = tk.Entry(tela)
        ent_telefone.pack()

        tk.Label(tela, text="Renda mensal:").pack()
        ent_renda = tk.Entry(tela)
        ent_renda.pack()

        tk.Label(tela, text="Moradia (casa/apartamento):").pack()
        ent_moradia = tk.Entry(tela)
        ent_moradia.pack()

        def salvar():
            try:
                nome = ent_nome.get().strip()
                cpf = ent_cpf.get().strip()
                if cpf == "":
                    raise ValueError("Sem CPF.")
                telefone = ent_telefone.get().strip()
                renda = int(ent_renda.get().strip())
                moradia = ent_moradia.get().strip().lower()

                adotante = Adotante(nome, cpf, telefone, renda, moradia)
                self.ong.cadastrar_adotante(adotante)
                messagebox.showinfo("Sucesso no cadastro")
                tela.destroy()
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Salvar", command=salvar).pack(pady=10)

    def cadastrar_voluntario(self):
        tela = tk.Toplevel(self.janela)
        tela.title("Cadastrar Voluntario")
        tela.geometry("300x220")

        tk.Label(tela, text="Nome:").pack()
        ent_nome = tk.Entry(tela)
        ent_nome.pack()

        tk.Label(tela, text="CPF:").pack()
        ent_cpf = tk.Entry(tela)
        ent_cpf.pack()

        tk.Label(tela, text="Telefone:").pack()
        ent_telefone = tk.Entry(tela)
        ent_telefone.pack()

        def salvar():
            try:
                nome = ent_nome.get().strip()
                cpf = ent_cpf.get().strip()
                if cpf == "":
                    raise ValueError("Sem cpf.")
                telefone = ent_telefone.get().strip()

                voluntario = Voluntario(nome, cpf, telefone)
                self.ong.cadastrar_voluntario(voluntario)
                messagebox.showinfo("Sucessono cadastro")
                tela.destroy()
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Salvar", command=salvar).pack(pady=10)


    def listar_animais_disponiveis(self):
        animais = self.ong.buscar_animais()
        self.mostrar_animais(animais)

    #Funcao para mostrar o que foi puxado da ing pelo buscar animais
    def mostrar_animais(self, animais):
        #Caso existam 0 animais
        if len(animais) == 0:
            messagebox.showinfo("Animais", "Nenhum animal encontrado.")
            return
        texto = ""
        #Esse for é para abrir apenas uma janela para todos os animais
        for animal in animais:
            texto = texto + self.texto_animal(animal) + "\n"
        messagebox.showinfo("Animais Disponiveis", texto)

    def texto_animal(self, animal):
        especie = animal.especie()
        #Essas duas são booleanas, dai fiz assim
        vacinado = "sim" if animal.vacinado else "nao"
        castrado = "sim" if animal.castrado else "nao"

        return (f"{animal.codigo} - {animal.nome} - {especie}, {animal.idade} anos, "
                f"porte {animal.porte}, vacinado: {vacinado}, castrado: {castrado}")


    def carregar_exemplos(self):
        try:
            self.ong.cadastrar_animal(Cachorro(101, "Zeus", 3, "grande", True, True))
            self.ong.cadastrar_animal(Cachorro(102, "Pipoca", 1, "pequeno", True, False))
            self.ong.cadastrar_animal(Gato(201, "Destruidor de mundos", 2, "pequeno", True, True))
            self.ong.cadastrar_animal(Gato(202, "caju", 5, "medio", False, True))

            self.ong.cadastrar_adotante(Adotante("Ana", "12312312312", "43998373196", 3500, "casa"))
            self.ong.cadastrar_adotante(Adotante("Bruno", "22222222222", "43998373197", 2800, "apartamento"))

            self.ong.cadastrar_voluntario(Voluntario("Luizao", "33333333333", "41999990003"))

            messagebox.showinfo("Exemplos carregados.")
        except (ValueError, TypeError) as erro:
            messagebox.showerror("Erro", str(erro))


if __name__ == "__main__":
    interface().executar()