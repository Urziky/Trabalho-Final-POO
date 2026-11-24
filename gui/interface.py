import tkinter as tk
from tkinter import messagebox, ttk

from logica.animal import Cachorro, Gato
from logica.criarAnimal import CriaAnimal
from logica.pessoa import Adotante, Voluntario
from logica.ong import ONG
from logica.filtroAnimal import FiltroAnimal


class interface:
    def __init__(self):
    
        self.ong = ONG("Doação do Luizão")
        
        self.proximo_codigo_processo = 1
         
        #Tela principal
        self.janela = tk.Tk()
        self.janela.title("Sistema de Adoção - " + self.ong.nome)
        self.janela.geometry("430x540")
        
        #Cria um texto na parte de cuma da janela
        titulo = tk.Label(self.janela, text="Sistema de Adoção - " + self.ong.nome, font=("Arial", 16, "bold"))
        
        titulo.pack(pady=18)

        #Primeiros botoes chamando as devidas funcoes
        tk.Button(self.janela, text="1 - Cadastrar animal", width=38,
                  command=self.cadastrar_animal).pack(pady=4)
        tk.Button(self.janela, text="2 - Cadastrar adotante", width=38,
                  command=self.cadastrar_adotante).pack(pady=4)
        tk.Button(self.janela, text="3 - Cadastrar voluntário", width=38,
                  command=self.cadastrar_voluntario).pack(pady=4)
        tk.Button(self.janela, text="4 - Listar animais disponíveis", width=38,
                  command=self.listar_animais_disponiveis).pack(pady=4)
        tk.Button(self.janela, text="5 - Buscar animais com filtros", width=38,
                  command=self.buscar_animais_com_filtro).pack(pady=4)
        tk.Button(self.janela, text="6 - Abrir processo de adoção", width=38,
                  command=self.abrir_processo).pack(pady=4)
        tk.Button(self.janela, text="7 - Avançar ou recusar processo", width=38,
                  command=self.gerenciar_processo).pack(pady=4)
        tk.Button(self.janela, text="8 - Ver histórico dos processos", width=38,
                  command=self.ver_historico).pack(pady=4)
        tk.Button(self.janela, text="9 - Carregar dados de exemplo", width=38,
                  command=self.carregar_exemplos).pack(pady=4)
        tk.Button(self.janela, text="Sair", width=38,
                  command=self.janela.destroy).pack(pady=14)

    def executar(self):
        self.janela.mainloop()

    # Cadastros dos animais
    def cadastrar_animal(self):
    
        #Isso abre a janela secundaria
        tela = tk.Toplevel(self.janela)
        tela.title("Cadastrar animal")
        tela.geometry("320x390")

        #Cada tk.label cria o texto, e cada ent cria a entrada de texto
        tk.Label(tela, text="Espécie:").pack()
        ent_especie = ttk.Combobox(tela, values=["cachorro", "gato"], state="readonly")
        ent_especie.pack()

        tk.Label(tela, text="Código:").pack()
        ent_codigo = tk.Entry(tela)
        ent_codigo.pack()

        tk.Label(tela, text="Nome:").pack()
        ent_nome = tk.Entry(tela)
        ent_nome.pack()

        tk.Label(tela, text="Idade:").pack()
        ent_idade = tk.Entry(tela)
        ent_idade.pack()

        tk.Label(tela, text="Porte:").pack()
        ent_porte = ttk.Combobox(tela, values=["pequeno", "medio", "grande"], state="readonly")
        ent_porte.pack()

        tk.Label(tela, text="Vacinado?").pack()
        ent_vacinado = ttk.Combobox(tela, values=["sim", "não"], state="readonly")
        ent_vacinado.pack()

        tk.Label(tela, text="Castrado?").pack()
        ent_castrado = ttk.Combobox(tela, values=["sim", "não"], state="readonly")
        ent_castrado.pack()

        #Função para salvar o que foi escrito
        def salvar():
            try:
                especie = ent_especie.get()
                codigo = self.converter_inteiro(ent_codigo.get(), "Código")
                nome = ent_nome.get().strip()
                idade = self.converter_inteiro(ent_idade.get(), "Idade")
                porte = ent_porte.get()
                
                #juntei os ifs em um só já que coloquei o ttk.combobox
                if not especie or not porte or not ent_vacinado.get() or not ent_castrado.get():
                    raise ValueError("Preencha todos os campos.")

                vacinado = ent_vacinado.get() == "sim"
                castrado = ent_castrado.get() == "sim"

                #chama a função da fabrica de animais para criar o animal de acordo com a especie ao invés de ficar chamando o construtor direto, 
                #assim se no futuro for adicionado outra especie só precisa alterar a fabrica
                animal = CriaAnimal.criar_animal(
                especie, codigo, nome, idade,
                porte, vacinado, castrado
                )

                #Manda o animal pra ser cadastrado
                self.ong.cadastrar_animal(animal)
                messagebox.showinfo("Sucesso", f"{nome} foi cadastrado.")
                tela.destroy()

            #O except pra calcular os erros, inclusive caso tenha alguma das funcoes que foram chamadas
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Salvar", command=salvar).pack(pady=12)

    def cadastrar_adotante(self):
    
        tela = tk.Toplevel(self.janela)
        tela.title("Cadastrar adotante")
        tela.geometry("320x320")

        #juntei tudo em 1 for pra diminuir um pouco o código
        campos = {}
        #vai chamando o nome dos campos em ordem
        for rotulo in ["Nome", "CPF", "Telefone", "Renda mensal"]:
            tk.Label(tela, text=rotulo + ":").pack()
            campo = tk.Entry(tela)
            campo.pack()
            campos[rotulo] = campo
        
        #como a moradia só pode ser casa ou apartamento usei o ttk.combobox
        tk.Label(tela, text="Moradia:").pack()
        moradia = ttk.Combobox(tela, values=["casa", "apartamento"], state="readonly")
        moradia.pack()

        def salvar():
            try:
                adotante = Adotante(
                    campos["Nome"].get().strip(),
                    campos["CPF"].get().strip(),
                    campos["Telefone"].get().strip(),
                    self.converter_decimal(campos["Renda mensal"].get(), "Renda mensal"),
                    moradia.get()
                )
                self.ong.cadastrar_adotante(adotante)
                messagebox.showinfo("Sucesso", "Adotante cadastrado.")
                tela.destroy()
                
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Salvar", command=salvar).pack(pady=12)

    def cadastrar_voluntario(self):
    
        tela = tk.Toplevel(self.janela)
        tela.title("Cadastrar voluntário")
        tela.geometry("320x260")
        
        #mesmo esquema de usar 1 for para diminuir o código
        campos = {}
        for rotulo in ["Nome", "CPF", "Telefone"]:
            tk.Label(tela, text=rotulo + ":").pack()
            campo = tk.Entry(tela)
            campo.pack()
            campos[rotulo] = campo

        def salvar():
            try:
                voluntario = Voluntario(
                    campos["Nome"].get().strip(),
                    campos["CPF"].get().strip(),
                    campos["Telefone"].get().strip()
                )
                self.ong.cadastrar_voluntario(voluntario)
                messagebox.showinfo("Sucesso", "Voluntário cadastrado.")
                tela.destroy()
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Salvar", command=salvar).pack(pady=12)

  
    def listar_animais_disponiveis(self):
        animais = self.ong.buscar_animais()
        self.mostrar_animais(animais)

    #lista os animais porém usando o filtro
    def buscar_animais_com_filtro(self):
        tela = tk.Toplevel(self.janela)
        tela.title("Buscar animais com filtros")
        tela.geometry("330x300")
        
        tk.Label(tela, text="Espécie:").pack(pady=(10, 0))
        especie = ttk.Combobox(
            tela, values=["Todas", "cachorro", "gato"], state="readonly"
        )
        especie.set("Todas")
        especie.pack()

        tk.Label(tela, text="Porte:").pack(pady=(8, 0))
        porte = ttk.Combobox(
            tela, values=["Todos", "pequeno", "medio", "grande"], state="readonly"
        )
        porte.set("Todos")
        porte.pack()

        tk.Label(tela, text="Vacinado:").pack(pady=(8, 0))
        vacinado = ttk.Combobox(
            tela, values=["Todos", "Sim", "Não"], state="readonly"
        )
        vacinado.set("Todos")
        vacinado.pack()

        tk.Label(tela, text="Castrado:").pack(pady=(8, 0))
        castrado = ttk.Combobox(
            tela, values=["Todos", "Sim", "Não"], state="readonly"
        )
        castrado.set("Todos")
        castrado.pack()

        def buscar():
            try:
                especie_filtro = None if especie.get() == "Todas" else especie.get()
                porte_filtro = None if porte.get() == "Todos" else porte.get()
                vacinado_filtro = self.converter_filtro_booleano(vacinado.get())
                castrado_filtro = self.converter_filtro_booleano(castrado.get())

                filtro = FiltroAnimal(
                    especie_filtro, porte_filtro,
                    vacinado_filtro, castrado_filtro
                )
                animais = self.ong.buscar_animais(filtro)
                self.mostrar_animais(animais)
                tela.destroy()
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Buscar", command=buscar).pack(pady=16)
        
    #o int() sozinho mostra o erro em ingles (invalid literal for int...),
    #entao aqui a gente troca por uma mensagem em portugues
    def converter_inteiro(self, texto, campo):
        try:
            return int(texto.strip())
        except ValueError:
            raise ValueError(f"{campo} deve ser um número inteiro.")

    #mesma coisa do de cima, mas para numero com virgula (renda)
    def converter_decimal(self, texto, campo):
        try:
            #o replace é pq o python usa pontos para representar os numeros decimais
            return float(texto.strip().replace(",", "."))
        except ValueError:
            raise ValueError(f"{campo} deve ser um número, por exemplo 2500,00.")

    #transforma o "sim e não" em valores booleanos(true,false), e transforma o "todos" em none
    def converter_filtro_booleano(self, valor):
        if valor == "Todos":
            return None
        return valor == "Sim"

    #Funcao para mostrar o que foi puxado da ing pelo buscar animais
    def mostrar_animais(self, animais):
        tela = tk.Toplevel(self.janela)
        tela.title("Animais disponíveis")
        tela.geometry("780x350")

        colunas = ("codigo", "nome", "especie", "idade", "porte", "vacinado", "castrado")
        tabela = ttk.Treeview(tela, columns=colunas, show="headings")
        titulos = {
            "codigo": "Código", "nome": "Nome", "especie": "Espécie",
            "idade": "Idade", "porte": "Porte",
            "vacinado": "Vacinado", "castrado": "Castrado"
        }
        larguras = {"codigo": 65, "nome": 150, "especie": 100,
                    "idade": 55, "porte": 85, "vacinado": 85, "castrado": 85}

        for coluna in colunas:
            tabela.heading(coluna, text=titulos[coluna])
            tabela.column(coluna, width=larguras[coluna], anchor="center")

        tabela.pack(fill="both", expand=True, padx=10, pady=10)
        
        if not animais:
            tk.Label(tela, text="Nenhum animal encontrado.").pack(pady=5)
            
        else:
            for animal in animais:
                tabela.insert("", "end", values=(
                    animal.codigo,
                    animal.nome,
                    animal.especie(),
                    animal.idade,
                    animal.porte,
                    "Sim" if animal.vacinado else "Não",
                    "Sim" if animal.castrado else "Não"
                ))
            
    #tela da função de abrir processos 
    def abrir_processo(self):
        animais = self.ong.buscar_animais()
        adotantes = self.ong.listar_adotantes()
        voluntarios = self.ong.listar_voluntarios()

        if not animais or not adotantes or not voluntarios:
            messagebox.showwarning(
                "Dados insuficientes",
                "Cadastre pelo menos um animal disponível, um adotante e um voluntário."
            )
            return

        tela = tk.Toplevel(self.janela)
        tela.title("Abrir processo de adoção")
        tela.geometry("430x280")
        
        #as opçoes já estão pré-definidas para não ter q ficar escrevendo o nome, código, etc...
        tk.Label(tela, text="Animal disponível:").pack(pady=(12, 0))
        animal_combo = ttk.Combobox(
            tela,
            values=[f"{a.codigo} - {a.nome} ({a.especie()})" for a in animais],
            state="readonly", width=45
        )
        animal_combo.pack()
        animal_combo.current(0)

        tk.Label(tela, text="Adotante:").pack(pady=(8, 0))
        adotante_combo = ttk.Combobox(
            tela, values=[f"{a.nome} - CPF {a.cpf}" for a in adotantes],
            state="readonly", width=45
        )
        adotante_combo.pack()
        adotante_combo.current(0)
       
        
        tk.Label(tela, text="Voluntário responsável:").pack(pady=(8, 0))
        voluntario_combo = ttk.Combobox(
            tela, values=[f"{v.nome} - CPF {v.cpf}" for v in voluntarios],
            state="readonly", width=45
        )
        voluntario_combo.pack()
        voluntario_combo.current(0)

        def salvar():
            try:
                animal = animais[animal_combo.current()]
                adotante = adotantes[adotante_combo.current()]
                voluntario = voluntarios[voluntario_combo.current()]

                processo = self.ong.abrir_processo(
                    self.proximo_codigo_processo,
                    adotante,
                    animal,
                    voluntario
                )
                self.proximo_codigo_processo += 1

                messagebox.showinfo(
                    "Processo aberto",
                    f"Processo {processo.codigo} aberto com sucesso.\n"
                    f"Etapa atual: {processo.etapa_atual.nome_etapa}"
                )
                tela.destroy()
            except (ValueError, TypeError, IndexError) as erro:
                messagebox.showerror("Erro", str(erro))

        tk.Button(tela, text="Abrir processo", command=salvar).pack(pady=16)
    
    #tela de gerenciar processos, avançar/recusar
    def gerenciar_processo(self):
        processos = self.ong.consultar_processos()
        voluntarios = self.ong.listar_voluntarios()

        if not processos:
            messagebox.showinfo("Processos", "Nenhum processo foi aberto ainda.")
            return
        if not voluntarios:
            messagebox.showwarning("Voluntários", "Cadastre um voluntário primeiro.")
            return
        
        #ambos avançar/recusar eu deixei em uma tela
        tela = tk.Toplevel(self.janela)
        tela.title("Avançar ou recusar processo")
        tela.geometry("480x300")

        tk.Label(tela, text="Selecione o processo:").pack(pady=(12, 0))
        processo_combo = ttk.Combobox(
            tela,
            values=[
                f"Processo {p.codigo} - {p.adotante.nome} -> {p.animal.nome} "
                f"({p.etapa_atual.nome_etapa})"
                for p in processos
            ],
            state="readonly", width=55
        )
        processo_combo.pack()
        processo_combo.current(0)

        tk.Label(tela, text="Voluntário responsável:").pack(pady=(12, 0))
        voluntario_combo = ttk.Combobox(
            tela,
            values=[f"{v.nome} - CPF {v.cpf}" for v in voluntarios],
            state="readonly", width=45
        )
        voluntario_combo.pack()
        voluntario_combo.current(0)

        def obter_selecoes():
            indice_processo = processo_combo.current()
            indice_voluntario = voluntario_combo.current()
            if indice_processo < 0 or indice_voluntario < 0:
                raise ValueError("Selecione um processo e um voluntário.")
            return processos[indice_processo], voluntarios[indice_voluntario]

        def avancar():
            try:
                processo, voluntario = obter_selecoes()
                processo.avancar_etapa(voluntario)
                messagebox.showinfo(
                    "Processo atualizado",
                    f"Processo {processo.codigo} avançou para "
                    f"{processo.etapa_atual.nome_etapa}."
                )
                tela.destroy()
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        def recusar():
            try:
                processo, voluntario = obter_selecoes()
                #uma confirmação para não recusar um processo sem querer
                confirmar = messagebox.askyesno(
                    "Confirmar recusa",
                    f"Deseja realmente recusar o processo {processo.codigo}?"
                )
                if not confirmar:
                    return
                processo.recusar(voluntario)
                messagebox.showinfo(
                    "Processo recusado",
                    f"Processo {processo.codigo} recusado. "
                    f"O animal voltou a ficar disponível."
                )
                tela.destroy()
            except (ValueError, TypeError) as erro:
                messagebox.showerror("Erro", str(erro))

        botoes = tk.Frame(tela)
        botoes.pack(pady=22)
        tk.Button(botoes, text="Avançar etapa", command=avancar).pack(side="left", padx=8)
        tk.Button(botoes, text="Recusar processo", command=recusar).pack(side="left", padx=8)

    #tela do historico, em cima mostra os processos e embaixo as etapas do processo selecionado
    def ver_historico(self):
        processos = self.ong.consultar_processos()

        if not processos:
            messagebox.showinfo("Histórico", "Nenhum processo foi aberto ainda.")
            return

        tela = tk.Toplevel(self.janela)
        tela.title("Histórico dos processos")
        tela.geometry("620x480")

        #tabela dos processos, mesmo esquema da tabela de animais
        tk.Label(tela, text="Processos:").pack(pady=(10, 0))
        colunas = ("codigo", "adotante", "animal", "etapa")
        tabela_processos = ttk.Treeview(tela, columns=colunas, show="headings", height=6)
        titulos = {
            "codigo": "Processo", "adotante": "Adotante",
            "animal": "Animal", "etapa": "Etapa atual"
        }
        larguras = {"codigo": 80, "adotante": 180, "animal": 180, "etapa": 120}

        for coluna in colunas:
            tabela_processos.heading(coluna, text=titulos[coluna])
            tabela_processos.column(coluna, width=larguras[coluna], anchor="center")

        tabela_processos.pack(fill="x", padx=10, pady=5)

        for processo in processos:
            tabela_processos.insert("", "end", values=(
                processo.codigo,
                processo.adotante.nome,
                processo.animal.nome,
                processo.etapa_atual.nome_etapa
            ))

        #tabela do historico, ela muda conforme o processo que for clicado em cima
        tk.Label(tela, text="Histórico do processo selecionado:").pack(pady=(10, 0))
        colunas_historico = ("data", "etapa", "responsavel")
        tabela_historico = ttk.Treeview(tela, columns=colunas_historico, show="headings", height=6)
        titulos_historico = {"data": "Data", "etapa": "Etapa", "responsavel": "Responsável"}
        larguras_historico = {"data": 120, "etapa": 150, "responsavel": 200}

        for coluna in colunas_historico:
            tabela_historico.heading(coluna, text=titulos_historico[coluna])
            tabela_historico.column(coluna, width=larguras_historico[coluna], anchor="center")

        tabela_historico.pack(fill="x", padx=10, pady=5)

        def mostrar_registros(evento):
            #limpa a tabela antes de colocar os registros do outro processo
            for item in tabela_historico.get_children():
                tabela_historico.delete(item)

            selecionado = tabela_processos.selection()
            if not selecionado:
                return

            #a linha da tabela esta na mesma ordem da lista de processos
            processo = processos[tabela_processos.index(selecionado[0])]

            for registro in processo.historico:
                tabela_historico.insert("", "end", values=(
                    registro.data,
                    registro.nome_etapa,
                    registro.voluntario.nome
                ))

        #toda vez que clicar em um processo chama a funcao de cima
        tabela_processos.bind("<<TreeviewSelect>>", mostrar_registros)

        #ja deixa o primeiro processo selecionado pra tabela de baixo nao abrir vazia
        tabela_processos.selection_set(tabela_processos.get_children()[0])


    def carregar_exemplos(self):
        try:
            self.ong.cadastrar_animal(Cachorro(101, "Zeus", 3, "grande", True, True))
            self.ong.cadastrar_animal(Cachorro(102, "Pipoca", 1, "pequeno", True, False))
            self.ong.cadastrar_animal(Gato(201, "Destruidor de mundos", 2, "pequeno", True, True))
            self.ong.cadastrar_animal(Gato(202, "Caju", 5, "medio", False, True))

            self.ong.cadastrar_adotante(Adotante("Ana", "12312312312", "43998373196", 3500, "casa"))
            self.ong.cadastrar_adotante(Adotante("Bruno", "22222222222", "43998373197", 2800, "apartamento"))
            
            self.ong.cadastrar_voluntario(Voluntario("Luizão", "33333333333", "41999990003"))

            messagebox.showinfo("Sucesso", "Dados de exemplo carregados.")
        except (ValueError, TypeError) as erro:
            messagebox.showerror("Erro", str(erro))


if __name__ == "__main__":
    interface().executar()
