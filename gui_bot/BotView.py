from BaseView import BaseView
import PySimpleGUI as sg


class BotView(BaseView):
    def __init__(self, controlador, windowName):
        super().__init__(controlador, windowName)

    def tela_bot(self, bot):
        comandos = bot.mostra_comandos()
        apresentacao = bot.apresentacao()

        linha0 = [sg.Text(f'Você está falando com o bot {bot.nome}')]
        linha1 = [sg.Text('Resposta: ')]
        linha2 = [sg.Text(
            apresentacao, key="resposta_bot", auto_size_text=True)]

        linha3 = []

        # colocar comandos na mesma linha
        for i in range(0, len(comandos)):
            linha3.append(sg.Button(comandos[i], key=i+1))

        linha4 = [sg.Button("Importar"), sg.Button(
            "Exportar"), sg.Button("Novo")]

        # colocar em um container e gerar a UI
        self.container = [linha0, linha1, linha2, linha3, linha4]
        self.window = sg.Window(
            self.windowName, self.container, font=("Helvetica", 14))

    def update_layout(self, resposta):
        height = len(resposta.split('\n')) - 1
        self.window.Element('resposta_bot').Update(resposta)
        self.window.Element('resposta_bot').set_size((75, height))
