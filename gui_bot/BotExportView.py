from BaseView import BaseView
import PySimpleGUI as sg


class BotExportView(BaseView):
    def __init__(self, controlador, windowName):
        super().__init__(controlador, windowName)

    def tela_bot(self):
        linha0 = [sg.Text('Exportar arquivo: '), sg.InputText(
            '', key="export_input", size=(50, 1))]
        linha1 = [sg.Text('', key="mensagem", size=(50, 1))]

        linha2 = [sg.Button('Exportar')]

        # colocar em um container e gerar a UI
        self.container = [linha0, linha1, linha2]
        self.window = sg.Window(
            self.windowName, self.container, font=("Helvetica", 14))

    def update_layout(self, mensagem):
        self.window.Element('mensagem').Update(mensagem)
