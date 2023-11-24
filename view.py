# view.py
from tkinter import * # Será utilizado para a criação gráfica. 
from tkinter import ttk #ttk para widgets temáticos mais amigáveis, modernos.
from tkinter import messagebox # para mensagens nas caixas de diálogos
from tkinter import filedialog # para diálogos de arquivos e diretórios
from tkcalendar import Calendar, DateEntry # Biblioteca Calendar utiliado para o calendário, DataEntry utilizado para a inserção da data.
from controller import Controller #faz parte do projeto.
from model import Model # #faz parte do projeto.
import os # operações com o sistema operacional
from PIL import Image, ImageTk # Biblioteca que trabalha com imagem
from tkinter import PhotoImage # é uma classe que exibe imagens em elementos gráficos

### Criando a Classe View
class View:
    def __init__(self, master, controller, model):
        self.master = master # Nome da minha janela principal
        self.master.title("") # Não deixe o nome da janela visível
        self.master.geometry("1043x453") #tamanho da janela
        self.master.configure(background="#B3CDE0") # cor da janela azul
        self.master.resizable(width=False, height=False) # a Janela não pode ser redimensionada pelo usuário
        

        self.controller = controller # a Classe view tera acesso ao controller
        self.model = model # # a Classe view tera acesso ao model
        
        # Adiciona o atributo self.frame_rodape
        self.frame_rodape = None


        self.image_path = "python.png"  # Inserindo a imagem do python e definindo o caminho. 
        self.image = self.load_image() # load = carrega a imagem e armazena o resultado em self.image

                      
    
        # Chama create_widgets após self.frame_rodape ser inicializado
        self.create_widgets()
        
    # Criando a Função para a imagem do Python inserida na parte gráfica (widgets)
    def load_image(self):
        try:
            original_image = Image.open(self.image_path) # Imagem é aberta utilizando a biblioteca Pillow (image.open)
            resized_image = original_image.resize((30, 30))  # redimensionando a imagem conforme a necessidade
            return ImageTk.PhotoImage(resized_image) # a imagem é convertida para que o Tkinter possa entender, este é o metodo que ele entende.
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}") # tratamento de execessão caso não conseguisse carregar a imagem. 
            return None
        
       
    # Criando as funções para as cores - Fazem parte  dos Atributos dos meus objetos. 
    def create_widgets(self): #Aqui esta sendo chamado uma função para a criação de widgets (interfaces gráficas com o tkinter)
        # Cores utilizadas
        co0 = "#8B9DC3"  # Cinza claro
        co1 = "#feffff"  # Branco
        co2 = "#715464"  # Verde escuro
        co3 = "#38576b"  # Azul escuro
        co4 = "#000000"  # Preta
        co5 = "#e06636"  # Laranja escuro
        co6 = "#005B96"  # Azul claro
        co7 = "#FB2E01"  # Vermelho claro
        co8 = "#263238"  # Azul acinzentado
        co9 = "#D7C6CF"  # Cinza azulado
        c10 = "#D7C6CF"  # Rosa Palido
        c11 = "#007F6E"  # Verde Forte
        c12 = "#666547"  # Verde Musgo
        
        #### Criando todos os Frames###     
        self.frame_cima = Frame(self.master, width=310, height=50, bg=co2, relief='flat') # será um subframe: tamanho, cor de fundo, borda
        self.frame_cima.grid(row=0, column=0) # linha e coluna de posicionamento

        self.frame_baixo = Frame(self.master, width=310, height=403, bg=co9, relief='flat') # subframe (tamanho. cor fundo, borda)
        self.frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1) #linha, coluna, posição norte, sul, leste, oeste, espaçamento hor/vertic. 

        self.frame_direita = Frame(self.master, width=588, height=403, bg=co1, relief='flat') 
        self.frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) #rowspan quantidade de linha que ele vai atingir
                       
        # Criado um Frame chamado 'frame_rodape' dentro do Frame chamado 'frame_direita', com fundo 'co1' e relevo 'flat'.       
        self.frame_rodape = Frame(self.frame_direita, bg=co1, relief='flat') 
        self.frame_rodape.grid(row=1, column=0, sticky=NSEW) #posição de linha e coluna e se espandindo para todos os lados

        # Criado rótulos (Labels) para informações específicas dentro do 'frame_rodape', com texto, fonte, fundo e cor configurados.
        self.l_faculdade = Label(self.frame_rodape, text='Faculdade: Cesusc', font=("Ivy 8 bold"), bg=co1, fg=co3)
        self.l_disciplina = Label(self.frame_rodape, text='Disciplina: Análise. Prob. Log. Computacional', font=("Ivy 8 bold"), bg=co1, fg=co3)
        self.l_professor = Label(self.frame_rodape, text='Professor: Roberto F. Fernandes', font=("Ivy 8 bold"), bg=co1, fg=co3)
        self.l_aluno = Label(self.frame_rodape, text='Aluno: Mario Chostak', font=("Ivy 8 bold"), bg=co1, fg=co3)

        # Configura a posição dos rótulos na grade dentro do 'frame_rodape', na linha 2 e colunas 0 a 3, com preenchimento e margens específicos.
        self.l_faculdade.grid(row=2, column=0, padx=5, pady=(0, 0))
        self.l_disciplina.grid(row=2, column=1, padx=5, pady=(0, 0))
        self.l_professor.grid(row=2, column=2, padx=5, pady=(0, 0))
        self.l_aluno.grid(row=2, column=3, padx=5, pady=(0, 0))

             
        # criação do rótulo (Label) Cadastro de clientes com as suas configurações.
        self.app_nome = Label(self.frame_cima, text='Cadastro de Clientes', anchor=NW, font=("Ivy 13 bold"), bg=co2, fg=co1, relief='flat')
        self.app_nome.place(x=10, y=15) # posição do rótulo utilizando o método place. 

        self.tree = None

        # Foi criado as entradas (Entry) para diferentes campos de informação dentro do 'frame_baixo'.
        # Configura a largura, justificação, tipo de relevo e outras características específicas para cada entrada.
        self.e_nome = Entry(self.frame_baixo, width=45, justify='left', relief='sunken')
        self.e_email = Entry(self.frame_baixo, width=45, justify='left', relief='sunken')
        self.e_telefone = Entry(self.frame_baixo, width=45, justify='left', relief='sunken')
        self.e_cal = DateEntry(self.frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=4, year=2023, locale='pt_BR')
        self.e_cpf = Entry(self.frame_baixo, width=20, justify='left', relief='sunken')
        self.e_assunto = Entry(self.frame_baixo, width=45, justify='left', relief='sunken')
        self.entry_search = Entry(self.frame_cima, width=20, justify='left', relief='sunken')
        
        # Criando os rótulo (nome, email....) no frame_baixo, com os respectivos nomes, ancorado no canto superior esquerdo.
        # Usando a fonte Ivy com tamanho 10 e negrito, fundo c10, texto co4 e relevo flat.
        self.l_nome = Label(self.frame_baixo, text='Nome *', anchor=NW, font=("Ivy 10 bold"), bg=c10, fg=co4, relief='flat')
        self.l_email = Label(self.frame_baixo, text='Email', anchor=NW, font=("Ivy 10 bold"), bg=c10, fg=co4, relief='flat')
        self.l_telefone = Label(self.frame_baixo, text='Telefone *', anchor=NW, font=("Ivy 10 bold"), bg=c10, fg=co4, relief='flat')
        self.l_cal = Label(self.frame_baixo, text='Data da inclusão *', anchor=NW, font=("Ivy 10 bold"), bg=c10, fg=co4, relief='flat')
        self.l_cpf = Label(self.frame_baixo, text='CPF', anchor=NW, font=("Ivy 10 bold"), bg=c10, fg=co4, relief='flat')
        self.l_assunto = Label(self.frame_baixo, text='Informações extras', anchor=NW, font=("Ivy 10 bold"), bg=c10, fg=co4, relief='flat')
        
        # Criando os botões e as suas configuações
        self.b_inserir = Button(self.frame_baixo, command=self.inserir, text='Inserir', width=10, font=("Ivy 9 bold"), bg=co6, fg=co1, relief='raised', overrelief='ridge')
        self.b_atualizar = Button(self.frame_baixo, command=self.atualizar, text='Atualizar', width=10, font=("Ivy 9 bold"), bg=c11, fg=co1, relief='raised', overrelief='ridge')
        self.b_confirmar = Button(self.frame_baixo, command=self.confirmar_atualizacao, text='Confirmar', width=10, font=("Ivy 9 bold"), bg=c12, fg=co1, relief='raised', overrelief='ridge')
        self.b_deletar = Button(self.frame_baixo, command=self.deletar, text='Deletar', width=10, font=("Ivy 9 bold"), bg=co7, fg=co1, relief='raised', overrelief='ridge')
      
        self.b_backup = Button(self.frame_baixo, command=self.backup, text='Backup', width=10, font=("Ivy 9 bold"), bg="#000000", fg="#feffff", relief='raised', overrelief='ridge') 
        self.b_restaurar = Button(self.frame_baixo, command=self.restaurar, text='Restaurar Backup', width=12, font=("Ivy 7 bold"), bg="#000000", fg="#feffff", relief='raised', overrelief='ridge', padx=5, pady=4)

        # Quais serão as posições dos labels e Entry utilizando o place. 
        self.l_nome.place(x=10, y=10)
        self.e_nome.place(x=15, y=40)
        self.l_email.place(x=10, y=70)
        self.e_email.place(x=15, y=100)
        self.l_telefone.place(x=10, y=130)
        self.e_telefone.place(x=15, y=160)
        self.l_cal.place(x=10, y=190)
        self.e_cal.place(x=15, y=220)
        self.l_cpf.place(x=160, y=190)
        self.e_cpf.place(x=160, y=220)
        self.l_assunto.place(x=15, y=260)
        self.e_assunto.place(x=15, y=290)

        # Quais serão as posições dos botões utilizando o place. 
        self.b_inserir.place(x=10, y=340)
        self.b_atualizar.place(x=110, y=340)
        self.b_confirmar.place(x=110, y=375)
        self.b_deletar.place(x=208, y=340)
        self.b_backup.place(x=10, y=375) 
        self.b_restaurar.place(x=205, y=375) 
        
        
        
        # Mostra a tabela na interface gráfica
        self.mostrar_tabela() 
        
        # Imagem do python onde estará localizada. 
        if self.image:
            self.image_label = Label(self.frame_cima, image=self.image, bg=co2)
            self.image_label.place(relx=0.80, rely=0.12, anchor=NW)
            self.image_label.lift()
                        
     
    ######## Chamando os Métodos##############
    def inserir(self): #Obtém os valores dos Entry e armazena em variaveis locais. 
        nome = self.e_nome.get() # .get() ele vem associado com o Entry que são os dados inseridos e recupera estes valores inseridos. 
        email = self.e_email.get()
        telefone = self.e_telefone.get()
        dia = self.e_cal.get()
        cpf = self.e_cpf.get()
        assunto = self.e_assunto.get()

        lista = [nome, email, telefone, dia, cpf, assunto] # Cria uma lista que contém os valores

        if nome == '':
            messagebox.showerror('Erro', 'O nome não pode ser vazio') # nome não pode estar vazio...
        elif telefone == '':
            messagebox.showerror('Erro', 'O telefone não pode ser vazio')
        elif dia == '':
            messagebox.showerror('Erro', 'O dia não pode ser vazio')
        else:
            self.controller.inserir(lista) # se tudo estiver ok, insere a lista
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!!!')

            # limpa os campos após a inserção ser bem concluída
            self.e_nome.delete(0, 'end') # excluir do indice "0" ao fim
            self.e_email.delete(0, 'end')
            self.e_telefone.delete(0, 'end')
            self.e_cal.delete(0, 'end')
            self.e_cpf.delete(0, 'end')
            self.e_assunto.delete(0, 'end')

            # atualiza a tabela após a inserção ser bem sucedida
            self.mostrar_tabela()

    def atualizar(self): 
        try: # Inicia o bloco para tratamento de exceções
            treev_dados = self.tree.focus() # ele irá pegar a linha que esta sendo focada, selecionada. 
            treev_dicionario = self.tree.item(treev_dados) #Obtem um dicionário que representa as informações do item (linha)
            tree_lista = treev_dicionario['values'] # obtem a lista de valores associados nesta linha

            global valor_id # Declara a variável valor_id
            valor_id = tree_lista[0] # define esta variável com o valor do primeiro elemento ID

            #Limpa os campos de entrada
            self.e_nome.delete(0, 'end')
            self.e_email.delete(0, 'end')
            self.e_telefone.delete(0, 'end')
            self.e_cal.delete(0, 'end')
            self.e_cpf.delete(0, 'end')
            self.e_assunto.delete(0, 'end')

            # prreenche os campos de entrada com os valores obtidos na Treeview. 
            self.e_nome.insert(0, tree_lista[1])
            self.e_email.insert(0, tree_lista[2])
            self.e_telefone.insert(0, tree_lista[3])
            self.e_cal.insert(0, tree_lista[4])
            self.e_cpf.insert(0, tree_lista[5])
            self.e_assunto.insert(0, tree_lista[6])

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def confirmar_atualizacao(self): # Obtém os valores nos campos de entrada
        try:
            nome = self.e_nome.get()
            email = self.e_email.get()
            telefone = self.e_telefone.get()
            dia = self.e_cal.get()
            cpf = self.e_cpf.get()
            assunto = self.e_assunto.get()

            # Obtem uma lista nos campos de entrada
            lista = [nome, email, telefone, dia, cpf, assunto, valor_id]

            # Tratamento dos dados
            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
                
            elif telefone == '':
                messagebox.showerror('Erro', 'O telefone não pode ser vazio')
            
            elif dia == '':
                messagebox.showerror('Erro', 'O dia não pode ser vazio')
                    
            else: # Chama o método 'atualizar' do objeto 'controller' passando a lista como argumento.
                self.controller.atualizar(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!!!')

                #Limpa os campos de entrada após atulização ser executada
                self.e_nome.delete(0, 'end')
                self.e_email.delete(0, 'end')
                self.e_telefone.delete(0, 'end')
                self.e_cal.delete(0, 'end')
                self.e_cpf.delete(0, 'end')
                self.e_assunto.delete(0, 'end')

                # Atualiza a tabela após a atualização bem-sucedida.
                self.mostrar_tabela()
                
        #Mensagem de erro
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def deletar(self):
        try:
            treev_dados = self.tree.focus() # obtem o item selecionado (item=linha selecionada)
            treev_dicionario = self.tree.item(treev_dados) # obtem um dicionário com as informações do item (linha)
            tree_lista = treev_dicionario['values'] # obtem a lista de valores associados ao item (linha)

            valor_id = [tree_lista[0]] # cria uma lista contendo o valor do primeiro campo = ID

            self.controller.deletar(valor_id) # Chama o metódo deletar passando a lista como argumento, no caso o ID. 
            messagebox.showinfo('Sucesso', 'Os dados foram excluídos da tabela com sucesso!!!')

            self.mostrar_tabela() # Atualiza a tabela após executado. 

        except IndexError: # Mensagem de erro
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    
    # Mostrar a Tabela
    def mostrar_tabela(self):
        if self.tree:       # verifica se ela existe e caso exista ela destroi para evitar duplicatas de elementos gráficos, desta forma tudo é novo. 
            self.tree.destroy()

        lista = self.controller.mostrar() # lista os dados a serem exibidos

        tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'CPF', 'Assunto'] # Define os cabeçalhos da tabela na frame da direita

        self.tree = ttk.Treeview(self.frame_direita, selectmode="extended", columns=tabela_head, show="headings") #extend permite que vc selecione varios itens, permite que vc passe a tabela para as colunas, headings pede para que ela exibe somente o cabeçalho. 

        vsb = ttk.Scrollbar(self.frame_direita, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.frame_direita, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set) # configurando as barras de rolagem para que sejam controladas
        self.tree.grid(column=0, row=0, sticky='nsew') #ajuste de barras de rolagem 
        vsb.grid(column=1, row=0, sticky='ns') #ajuste das barras de rolagem e posição norte/sul
        hsb.grid(column=0, row=2, sticky='ew')

        self.frame_direita.grid_rowconfigure(1, weight=1)
        self.frame_direita.grid_rowconfigure(2, weight=0)  # Ajuste das barras de rolagem. 
        self.tree.xview_moveto(0.0)
       

        self.frame_direita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"] #posições que os cabeçalhos da tabela ficarão
        h = [30, 170, 140, 100, 120, 50, 100] #as Colunas terão valores específicos
        n = 0

        for col in tabela_head:
            self.tree.heading(col, text=col.title(), anchor=CENTER)
            self.tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista: #Os dados da lista são inseridos na tabela, uma linha de cada vez.
            self.tree.insert('', 'end', values=item)

    # Função de backup
    def backup(self):
        # Abre uma janela de diálogo para escolher o local do backup
        destino = filedialog.askdirectory()

        # Verifica se o usuário selecionou um destino
        if destino:
            # Chama o método de backup do controlador
            self.controller.fazer_backup(destino)
            messagebox.showinfo('Sucesso', 'Backup realizado com sucesso!')

    def restaurar(self):
        # Abre uma janela de diálogo para escolher o arquivo de backup
        origem = filedialog.askdirectory()

        # Verifica se o usuário selecionou um arquivo de backup
        if origem:
            # Chama o método de restauração do controlador
            self.controller.restaurar_backup(origem)
            messagebox.showinfo('Sucesso', 'Restauração concluída com sucesso!')
            # Atualiza a tabela após a restauração
            self.mostrar_tabela()
