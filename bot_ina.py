import json
from random import choice
from bot import Bot

dados = None
with open('./bot_ina.json', 'r') as f:
    dados = json.load(f)


class BotIna(Bot):
    def __init__(self):
        self.__nome = dados['nome']

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self):
        return choice(dados['apresentação'])

    def mostra_comandos(self):
        string = ""
        for i in range(0, len(dados["tipos_comandos"])):
            nome = dados['tipos_comandos'][i].replace('_', ' ')
            string += f'''
            {i + 1} - {nome}
          '''
        return string

    def executa_comando(self, cmd):
        cmd = int(cmd)
        comandos = dados['comandos']
        return choice(comandos[comandos.keys()[cmd - 1]])
