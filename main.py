# main.py - è o ponto de entrada principal do projeto. Ponto de início do programa onde estamos importando a biblioteca gráfica "tkinter"
# estamos importando as classes do meu projeto contidas nos módulos (view, model, controller)
from tkinter import Tk
from view import View
from model import Model
from controller import Controller

# Criando a instância do Model
modelo = Model()

# Criando a instância do Controller, passando o modelo
controle = Controller(modelo)

# Criando a instância da View, passando o master, o controller e o model
janela = Tk()
app = View(janela, controle, modelo)

# Iniciando o loop principal
janela.mainloop()