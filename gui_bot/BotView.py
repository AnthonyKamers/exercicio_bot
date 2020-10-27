import PySimpleGUI as sg


class BotView:
    def __init__(self, controlador):
        self.controlador = controlador
        self.container = []
        self.window = sg.Window(
            'Sistema ChatBot', self.container, font=('Helvetica', 14))

    def tela_bot(self, bot):
        comandos = bot.mostra_comandos()
        apresentacao = bot.apresentacao()

        linha0 = [sg.Text(f'Você está falando com o bot {bot.nome}')]
        linha1 = [sg.Text('Resposta: ')]
        linhaResposta = [sg.Text(
            apresentacao, key="resposta_bot", auto_size_text=True)]

        linha2 = []

        # colocar comandos na mesma linha
        for i in range(0, len(comandos)):
            linha2.append(sg.Button(comandos[i], key=i+1))

        linha3 = [sg.Text('Importar: '), sg.InputText(
            '', key="importar_text"), sg.Button('Importar')]
        linha4 = [sg.Text('Exportar como: '), sg.InputText(
            '', key="exportar_text"), sg.Button('Exportar')]

        # colocar em um container e gerar a UI
        self.container = [linha0, linha1,
                          linhaResposta, linha2, linha3, linha4]
        self.window = sg.Window(
            'Sistema ChatBot', self.container, font=("Helvetica", 14))

    def update_resposta_bot(self, resposta_bot):
        height = len(resposta_bot.split('\n')) - 1
        self.window.Element('resposta_bot').Update(resposta_bot)
        self.window.Element('resposta_bot').set_size((75, height))

    def le_eventos(self):
        return self.window.read()

    def fim(self):
        self.window.close()
