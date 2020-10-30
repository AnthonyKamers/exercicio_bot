from Bot import Bot
import random


class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas=[]):
        self.__id = id
        self.__msg = msg
        self.__respostas = respostas

    # get id
    @property
    def id(self):
        return self.__id

    # get mensagem
    @property
    def mensagem(self):
        return self.__msg

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        return self.__respostas[random.randint(0, len(self.__respostas)-1)]

    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    # remove resposta (opcional)
    def delResposta(self, resposta):
        if resposta in self.__respostas:
            self.__respostas.remove(resposta)


class NewBot(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

        self.__comandos.append(Comando(1, "Bom dia", ['TOMA ESSE DOUBLE BICEPES AQUI',
                                                      'CAPSLOCK LIGADO, SINAL DE PERSONALIDADE FORTE', 'VAMOS TRILHAR O CAMINHO DOS CAMPEOES']))
        self.__comandos.append(Comando(2, "Qual o seu nome?", [
                               "AQUI É XANDÃO, O ÚLTIMO HERÓI DA TERRA!"]))
        self.__comandos.append(Comando(3, "Conselho", ['Nao tenha medo da escuridao, pois no fim havera XANDAO', 'O apocalipse so vao acontecer para os perdedores',
                                                       'Se capotar so segura no braço do XANDAO que ninguem morre', 'Vem com o XANDAO exalando energia', 'Trilhando o caminho dos campeoes que no fim tem XANDAO']))
        self.__comandos.append(Comando(4, "Despedida", [
            'Nao se preocupe que no fim da escuridao sempre havera Xandao', 'XANDAO FOREVER']))

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        x = 'SEM PRESSÃO, AQUI É XANDÃO!'
        return x

    def cria_comandos(self, id, mensagem, respostas):
        if isinstance(mensagem, str):
            self.__comandos.append(Comando(id, mensagem, respostas))
        else:
            return 'Tipo recebido inválido'

    def mostra_comandos(self):
        comandos = []
        for i in self.__comandos:
            comandos.append(i.mensagem)

        return comandos

    def executa_comando(self, cmd):
        '''if cmd == 1:
            resposta = self.boas_vindas()
        if cmd == 2:
            resposta = self.mostrar_nome()
        if cmd == 3:
            resposta = self.mostrar_conselhos()
        if cmd == 4:
            resposta = self.despedida()'''

        resposta = self.__comandos[cmd].getRandomResposta()

        return resposta

    def boas_vindas(self):
        pass

    def despedida(self):
        pass
