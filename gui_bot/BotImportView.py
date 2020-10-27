from BaseView import BaseView
import PySimpleGUI as sg


class BotImportView(BaseView):
    def __init__(self, controlador, windowName):
        super().__init__(controlador, windowName)

    def tela_bot(self):
        linha0 = [sg.Text('Importar arquivo: '), sg.InputText(
            '', key="import_input", size=(50, 1))]
        linha1 = [sg.Text('', key="mensagem", size=(50, 1))]

        linha2 = [sg.Button('Importar')]

        # colocar em um container e gerar a UI
        self.container = [linha0, linha1, linha2]
        self.window = sg.Window(
            self.windowName, self.container, font=("Helvetica", 14))

    def update_layout(self, mensagem):
        self.window.Element('mensagem').Update(mensagem)
