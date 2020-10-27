import PySimpleGUI as sg
import bots
from bots import *
import random

from Bot import Bot  # model
from BotView import BotView
from BotImportView import BotImportView
from BotExportView import BotExportView
from BotDAO import BotDAO

# junta todos os módulos em uma lista
botsLista = []
for name in bots.__all__:
    module = locals()[name]
    newBot = module.NewBot(name)
    botsLista.append(newBot)

firstBot = random.choice(botsLista)


class BotController:
    def __init__(self, botChosen=firstBot):
        self.telaBot = BotView(self, "Sistema ChatBot")
        self.telaImport = BotImportView(self, "Importar ChatBot")
        self.telaExport = BotExportView(self, "Exportar ChatBot")

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
                self.handleExport()

            elif event == "Importar":
                self.handleImport()

            elif event == "Novo":
                self.handleNew()

            # comando do bot
            else:
                respostaBot = self.botChosen.executa_comando(event)
                self.telaBot.update_layout(respostaBot)

        self.telaBot.fim()

    def handleImport(self):
        container = self.telaImport.tela_bot()

        rodando = True
        while rodando:
            event, values = self.telaImport.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == "Importar":
                import_input = values["import_input"]

                if (not import_input.endswith(".pkl")):
                    import_input += ".pkl"

                self.botSave = BotDAO(import_input)
                botsSaved = self.botSave.get_all()

                value = None
                for k, v in enumerate(botsSaved):
                    value = v

                if len(botsSaved) == 0:
                    self.telaImport.update_layout(
                        'Não há dados salvos nesse arquivo')
                    self.botSave = None
                else:
                    self.telaImport.fim()
                    self.botChosen = value
                    self.telaBot.fim()
                    self.inicia()

    def handleExport(self):
        container = self.telaExport.tela_bot()

        rodando = True
        while rodando:
            event, values = self.telaExport.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == "Exportar":
                export_input = values["export_input"]

                if (not export_input.endswith(".pkl")):
                    export_input += ".pkl"

                self.botSave = BotDAO(export_input)
                botsSaved = len(self.botSave.get_all())

                if botsSaved == 0:
                    self.botSave.add(self.botChosen)
                    self.telaExport.fim()
                else:
                    self.telaExport.update_layout(
                        'Impossível salvar o bot. Já existe um bot salvo.')

    def handleNew(self):
        self.telaBot.fim()
        self.botChosen = botsLista[random.randint(0, len(botsLista) - 1)]
        self.inicia()
