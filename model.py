# model.py
import sqlite3 # importanto módulo para interação com o banco de dados. 
import shutil #  Importando o módulo shutil para operações de manipulação de arquivos, utilizado para realizar o backup.
import os # Importando o módulo "os" para interagir com o sistema operacional.

class Model:
    def __init__(self):
        # Conectar ao banco de dados (SQLite neste caso)
        self.db_file = "database.db" #criando o nome do banco
        self.conn = sqlite3.connect(self.db_file) #conectando com o banco, canal de comunicação
        self.c = self.conn.cursor() # possibilita executar os comandos em SQL. 

        # Criar a tabela se ela não existir
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT,
                telefone TEXT NOT NULL,
                data_inclusao TEXT NOT NULL,
                cpf TEXT,
                informacoes_extras TEXT
            )
        ''')
        self.conn.commit() # confirmação de alterações com o banco de dados automaticamente. 

    def inserir_info(self, info): # inserir dados na tabela "clientes" e vai reservar espaços para cada argumento "?"
        self.c.execute("INSERT INTO clientes (nome, email, telefone, data_inclusao, cpf, informacoes_extras) VALUES (?, ?, ?, ?, ?, ?)", info)
        self.conn.commit()

    def mostrar_info(self):
        # Recuperar todos os dados da tabela
        self.c.execute("SELECT * FROM clientes") # Solicitando ao banco para mostrar toda a tabela
        data = self.c.fetchall() # após solicitado os dados da tabela, este comando nos mostra os dados solicitados
        return data

    def atualizar_info(self, info): # Atualizar dados na tabela com base no ID, SET expecifica qual coluna, ? placeholders (espaços reservados)
        self.c.execute("UPDATE clientes SET nome=?, email=?, telefone=?, data_inclusao=?, cpf=?, informacoes_extras=? WHERE id=?", info)
        self.conn.commit()

    def deletar_info(self, info): #Recebe uma lista chamada informação e deleta conforme o Id e após confirma com o commit
        # Deletar dados da tabela com base no ID
        self.c.execute("DELETE FROM clientes WHERE id=?", info)
        self.conn.commit()

    def fazer_backup(self, destino): # Copiar o arquivo do banco de dados para o diretório de destino
        try: #tentar
            shutil.copy(self.db_file, os.path.join(destino, "backup.db")) #shutil, copiar o arquivo do banco de dados e passo a ele o caminho completo para guardar este arquivo. 
            print(f"Backup realizado com sucesso: {os.path.join(destino, 'backup.db')}") #print
        except Exception as e:
            print(f"Erro ao fazer backup: {str(e)}") # caso de falha
