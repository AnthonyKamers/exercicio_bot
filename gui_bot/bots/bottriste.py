from Bot import Bot
import random as r


class IdRepetidoError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ComandoNaoExisteError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


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
        return r.choice(self.__respostas)

    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    # remove resposta (opcional)
    def delResposta(self, resposta):
        self.__respostas.remove(resposta)


class NewBot(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

        self.cria_comandos(1, "Boas vindas", [
                           "'Olá...Como posso te atrapalhar? Whoops, ajudar?'"])
        self.cria_comandos(2, "Despedida", ["Já vai embora? Sniff..."])
        self.cria_comandos(3, "Conselhos", [
                           'Vai dormir!', 'Larga esse curso!', 'Quem não tenta não fracassa!', 'Tururu ♬', 'Chore!'])

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self):
        return f'Eu sou o {self.__nome}'

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
        try:
            cmd = int(cmd)
            resposta = self.__comandos[cmd].getRandomResposta()

            return resposta

        except ValueError as e:
            print('comando tem que ser um inteiro')
        except StopIteration as e:
            print('comando não está na lista de comandos!')

    def boas_vindas(self):
        pass

    def despedida(self):
        pass
