from abc import ABC, abstractmethod
import PySimpleGUI as sg


class BaseView(ABC):
    def __init__(self, controlador, windowName):
        self.controlador = controlador
        self.container = []
        self.windowName = windowName
        self.window = sg.Window(
            self.windowName, self.container, font=('Helvetica', 14))

    @abstractmethod
    def tela_bot(self):
        pass

    def update_layout(self):
        pass

    def le_eventos(self):
        return self.window.read()

    def fim(self):
        self.window.close()
