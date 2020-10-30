from BaseView import BaseView
import PySimpleGUI as sg


class QuestionGeneratorView(BaseView):
    def __init__(self, controlador, windowName):
        super().__init__(controlador, windowName)
        self.i = 1

    def tela_bot(self):
        linha0 = [sg.Text('Nova pergunta:'), sg.InputText(
            '', key='pergunta_input', size=(50, 1))]
        linha1 = [sg.Text('Respostas:')]

        linha3 = [sg.Button("Adicionar respostas")]
        linha4 = [sg.Button("Salvar Pergunta e Resposta(s)")]

        self.container = [linha0, linha1]

        for i in range(0, self.i):
            self.container.append([sg.InputText('', key=i, size=(50, 1))])

        self.container.append(linha3)
        self.container.append(linha4)

        self.window = sg.Window(
            self.windowName, self.container, font=("Helvetica", 14))

    def update_layout(self):
        self.fim()
        self.i += 1
        self.tela_bot()
