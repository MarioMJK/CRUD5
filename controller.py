# controller.py: estará desenvolvendo a coordenação entre a interface do usuário, a lógica de negócios, e as operações de manipulação de dados. 
# Age, como intermediário entre a lógica que esta contida no model com a interface gráfica contida na view. 

# Importando os Módulos: São partes da biblioteca padrão do python, sua funcionalidade esta relacionada com a interação com o sistema Operacional.
# Esta relacionada a manipulação de arquivos e operações de sistema de arquivos. 
# o Módulo "os" fornece uma interface com o sistema operacional utilizando funções como manipulação de diretórios, caminhos de arquivo.
# o Módulo "shutil" é uma extenção do "Os" fornece um conjunto de operações para manipular arquivos e diretórios. (cópia de arquivos, diretórios inteiros).
import os
import shutil

# iniciando a class controller, com uma instância no model como parâmetro. 
class Controller: 
    def __init__(self, model):
        self.model = model
        
# método para inserir informações no modelo
    def inserir(self, i):
        self.model.inserir_info(i)

# método para mostrar informações no modelo
    def mostrar(self):
        return self.model.mostrar_info()

# método para atualizar informações no modelo
    def atualizar(self, i):
        self.model.atualizar_info(i)

# método para deletar informações no modelo.
    def deletar(self, i):
        self.model.deletar_info(i)

# Método para fazer backup do banco de dados do modelo.
    def fazer_backup(self, destino):
        nome_arquivo_backup = "backup.db" # nome arquivo
        caminho_destino = os.path.join(destino, nome_arquivo_backup)  # caminho backup
        try:
            shutil.copy(self.model.db_file, caminho_destino) #cópia do banco de dados para o destino
            print(f"Backup realizado com sucesso: {caminho_destino}")
        except Exception as e: #mensagem de erro, caso de falha
            print(f"Erro ao fazer backup: {str(e)}")

    def restaurar_backup(self, origem):  # restaurando backup
        nome_arquivo_backup = "backup.db"
        caminho_origem = os.path.join(origem, nome_arquivo_backup) 
        try:
            shutil.copy(caminho_origem, self.model.db_file) # cópia do backup para o banco de dados.
            print(f"Backup restaurado com sucesso a partir de: {caminho_origem}") #Sucesso
        except Exception as e:
            print(f"Erro ao restaurar backup: {str(e)}") # erro em caso de falha