from BaseView import BaseView
import PySimpleGUI as sg


class BotSelectView(BaseView):
    def __init__(self, controlador, windowName, botsLista):
        super().__init__(controlador, windowName)
        self.botsLista = botsLista

    def tela_bot(self):
        linha0 = [sg.Text("Escolha um bot de sua preferência")]
        linha1 = []

        for i in range(0, len(self.botsLista)):
            linha1.append(sg.Button(self.botsLista[i].nome, key=i))

        self.container = [linha0, linha1]
        self.window = sg.Window(
            self.windowName, self.container, font=("Helvetica", 14))
