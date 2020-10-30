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

        self.__comandos.append(Comando(1, "Quantos anos você tem?", [
                               'Deixa eu ver...Eu deitei pela primeira vez em 87...']))
        self.__comandos.append(Comando(2, "Abra a minha caixa de email", [
                               '*Yaaaawn* mó preguiça, depois eu faço.']))
        self.__comandos.append(Comando(3, "Qual é o rank atual do brasileirão", [
                               'A última vez que eu vi o Sport tava em primeiro...']))
        self.__comandos.append(Comando(4, "Quais são os files em cartaz?", [
                               '*Yawn* Império do Sol. Aquele lá com aquele garotinho novo... Christian Bale? Esse ai vai ter futuro, tô dizendo...zzzz']))

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    def cria_comandos(self, id, mensagem, respostas):
        if isinstance(mensagem, str):
            self.__comandos.append(Comando(id, mensagem, respostas))
        else:
            return 'Tipo recebido inválido'

    def apresentacao(self):
        return 'zzzzzz...Oi...Meu nome é...Soneca.'

    def mostra_comandos(self):
        comandos = []
        for i in self.__comandos:
            comandos.append(i.mensagem)
        return comandos

    def executa_comando(self, cmd):
        resposta = self.__comandos[cmd].getRandomResposta()

        return resposta

    def boas_vindas(self):
        return 'Zzzzz...'

    def despedida(self):
        return 'Zzzzz...'
