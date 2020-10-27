import PySimpleGUI as sg
import bots
from bots import *
import random

from Bot import Bot  # model
from BotView import BotView
from BotDAO import BotDAO

# junta todos os módulos em uma lista
botsLista = []
for name in bots.__all__:
    module = locals()[name]
    newBot = module.NewBot(name)
    botsLista.append(newBot)

firstBot = botsLista[random.randint(0, len(botsLista) - 1)]


class BotController:
    def __init__(self, botChosen=firstBot):
        self.telaBot = BotView(self)
        self.botSave = None
        self.botChosen = botChosen

    def inicia(self):
        container = self.telaBot.tela_bot(self.botChosen)

        # loop de eventos
        rodando = True
        while rodando:
            event, values = self.telaBot.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == "Exportar":
                pass

            elif event == "Importar":
                pass

            else:
                respostaBot = self.botChosen.executa_comando(event)
                self.telaBot.update_resposta_bot(respostaBot)

        self.telaBot.fim()
