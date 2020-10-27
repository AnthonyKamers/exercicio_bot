from Bot import Bot
import random


class NewBot(Bot):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def mostrar_nome(self):
        x = 'AQUI É XANDÃO, O ÚLTIMO HERÓI DA TERRA!'
        return x

    def apresentacao(self):
        x = ('SEM PRESSÃO, AQUI É XANDÃO!')
        return x

    def boas_vindas(self):
        boas_vindas = ['TOMA ESSE DOUBLE BICEPES AQUI',
                       'CAPSLOCK LIGADO, SINAL DE PERSONALIDADE FORTE', 'VAMOS TRILHAR O CAMINHO DOS CAMPEOES']
        x = random.choice(boas_vindas)
        return x

    def despedida(self):
        despedida = [
            'Nao se preocupe que no fim da escuridao sempre havera Xandao', 'XANDAO FOREVER']
        x = random.choice(despedida)
        return x

    def mostrar_conselhos(self):
        conselhos = ['Nao tenha medo da escuridao, pois no fim havera XANDAO', 'O apocalipse so vao acontecer para os perdedores', 'Se capotar so segura no braço do XANDAO que ninguem morre',


                     'Vem com o XANDAO exalando energia', 'Trilhando o caminho dos campeoes que no fim tem XANDAO']
        x = random.choice(conselhos)
        return x

    def mostra_comandos(self):
        # while True:
        # print('Lista de Comandos:')
        # print('1 - Bom Dia')
        # print('2 - Qual o seu nome?')
        # print('3 - Quero um conselho')
        # print('4 - Despedida')
        comandos = ["Bom dia", "Qual o seu nome?",
                    "Quero um conselho", "Despedida"]
        return comandos

    def executa_comando(self, cmd):
        # while cmd < 1 and cmd > 3:
        #     cmd = int(input('Comando inválido: digite novamente: ' ))
        cmd = int(cmd)
        if cmd == 1:
            resposta = self.boas_vindas()
        if cmd == 2:
            resposta = self.mostrar_nome()
        if cmd == 3:
            resposta = self.mostrar_conselhos()
        if cmd == 4:
            resposta = self.despedida()

        return resposta
