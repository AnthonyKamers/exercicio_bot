import random

from bot import Bot
from soneca import BotSoneca
# from xandao import XANDAO
from bot_ina import BotIna

from botXandao import BotXandao
from comando import Comando
from bottriste import BotTriste
from xandao2 import XANDAO as xandao2


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa

        # verifica se só tem da classe Bot
        for b in lista_bots:
            if isinstance(b, Bot):
                pass
            else:
                raise Exception('Todos devem ser da classe Bot')

        self.__lista_bots = lista_bots
        self.__bot = None

    @property
    def empresa(self):
        return self.__empresa

    @property
    def bot(self):
        return self.__bot

    def boas_vindas(self):
        print(f'Olá, esse é o sistema de chatbots da empresa {self.__empresa}')

    def mostra_menu(self):
        print(f'Os chatbots disponíveis no momento são: ')
        for n, bot in enumerate(self.__lista_bots):
            print(
                f'{n} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao()} ')

    def escolhe_bot(self):
        # faz a entrada de dados do usuário e atribui o objeto ao atributo __bot
        length = len(self.__lista_bots)
        try:
            index = int(input('Índice do bot: '))
            self.__bot = self.__lista_bots[index]
            self.__bot.boas_vindas()
        except Exception as e:
            print('Índice inválido!')
            self.escolhe_bot()

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())

    def le_envia_comando(self):
        self.mostra_comandos_bot()
        x = input('Digite o comando desejado(-1 para sair do programa): ')
        if x == '-1':
            return False
        else:
            resposta = self.__bot.executa_comando(x)
            try:
                assert(resposta is not None)
                print(resposta)
            except Exception as e:
                pass
            return True

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.loop()

    def loop(self):
        while True:
            x = self.le_envia_comando()
            if not x:
                break


xandao = BotXandao("SUPER XANDÃO")

xandao.cria_comandos(Comando(1, "BOM DIA", [
                     "BOM DIA DO ÚLTIMO HERÓI DA TERRA PARA OS CAMPEÕES, SEM PRESSÃO AQUI É XANDÃO, TÁ LIGADO?"]))
xandao.cria_comandos(Comando(2, "A TERRA REALMENTE É PLANA?", [
                     "SE TÁ DE BRINCADEIRA COM XANDÃO NÉ, OBVIAMENTE, NÃO É POSSÍVEL, NASA É DE HOLLYWOOD, QUEM ACREDITA NAQUELA NAVE DE TAMPA DE MARMITA?"]))
xandao.cria_comandos(Comando(3, "QUEM É ENÉAS?", [
                     "O HOMEM DE VERDADE DOUTOR ENÉAS."]))
xandao.cria_comandos(Comando(4, "O QUE TEM NO FINAL DA ESCURIDÃO?", [
                     "NO FINAL DA ESCURIDÃO TEM XANDÃO, TÁ LIGADO?"]))
xandao.cria_comandos(Comando(5, "DIVULGA MINHA AMIGA", [
                     "DEPOIS VOCÊ MANDA AÍ A LIVE DA SUA PARCEIRA QUE A GENTE DIVULGA"]))
xandao.cria_comandos(Comando(6, "SE CAPOTOU FAZ O QUE?", [
                     "SEGURA NO BRAÇO DO XANDÃO QUE NINGUÉM MORRE."]))
xandao.cria_comandos(Comando(7, "VOCÊ JÁ FOI ASSALTADO?", [
                     "CLARO QUE NÃO! QUEM QUE VAI SER LOUCO DE ASSALTAR O SUPER XANDÃO? DANDO 5 SOCOS POR SEGUNDO."]))
xandao.cria_comandos(Comando(8, "SUCUMBA XANDÃO", [
                     "SUCUMBA VOCÊ, OTÁRIO. SUPER XANDÃO FOREVER."]))
xandao.cria_comandos(Comando(
    9, "PORQUE VOCÊ FALA DE VOCÊ MESMO NA TERCEIRA PESSOA?", ["PORQUE AQUI É XANDÃO."]))
xandao.cria_comandos(Comando(10, "XANDÃO, PORQUE CORTOU O CABELÃO?", [
                     "ISSO É UMA LONGA HISTÓRIA. FOI NA CAÇA AOS DEMONIOS, XANDÃO FOI PEGO DESPREVENIDO, TAVA SALVANDO A NOVINHA, E AQUELA ESTÚPIDA, FALEI PRA ELA SAIR DE PERTO, QUE O XANDÃO IA DESTRUIR O DEMÔNIO, MAS ELA FICOU LÁ DE GRAÇA, 'AH NÃO XANDÃO, EU QUERO VER SEU PEITORAL EXALANDO ENERGIA' AÍ FUI SALVAR ELA DO DEMÔNIO, ELE DEU UMA ESPADADA, PEGOU NO CABELO DO XANDÃO. PERDI O CABELO POR CAUSA DAQUELA ANTA. AÍ EU FALEI, 'TA VENDO O SUA ANTA? POR ISSO QUE O XANDÃO FALOU PRA VOCÊ SAIR.'"]))
xandao.cria_comandos(Comando(11, "PORQUE VOCÊ FALA COM CAPS LIGADO?", [
                     "O CAPS LOCK LIGADO SIGNIFICA CONVICÇÃO E PERSONALIDADE FORTE, E PEITORAL DE AÇO POR DETRÁS DE QUEM TÁ FALANDO, TÁ LIGADO? É ASSIM QUE FUNCIONA IRMÃO. É ESTILO SUPER XANDÃO. NÃO TEM ESSES NEGÓCIOS DE FICAR FALANDO AINDUHASJD."]))
xandao.cria_comandos(Comando(12, "MANDA FOTO DE AGORA", ["""_________oBBBBB8o___oBBBBBBB8,
_____o8BBBBBBBBBBB__BBBBBBBBB8________o88o,
___o8BBBBBB**8BBBB__BBBBBBBBBB_____oBBBBBBBo,
__oBBBBBBB*___***___BBBBBBBBBB_____BBBBBBBBBBo,
_8BBBBBBBBBBooooo___*BBBBBBB8______*BB*_8BBBBBBo,
_8BBBBBBBBBBBBBBBB8ooBBBBBBB8___________8BBBBBBB8,
__*BBBBBBBBBBBBBBBBBBBBBBBBBB8_o88BB88BBBBBBBBBBBB,
____*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8,
______**8BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB*,
___________*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8*,
____________*BBBBBBBBBBBBBBBBBBBBBBBB8888**,
_____________BBBBBBBBBBBBBBBBBBBBBBB*,
_____________*BBBBBBBBBBBBBBBBBBBBB*,
______________*BBBBBBBBBBBBBBBBBB8,
_______________*BBBBBBBBBBBBBBBB*,
________________8BBBBBBBBBBBBBBB8,
_________________8BBBBBBBBBBBBBBBo,
__________________BBBBBBBBBBBBBBB8,"""]))

listaBots = [BotSoneca('gasparzinho'), xandao,
             BotTriste('teste', []), xandao2('final')]
sys = SistemaChatBot('teste', listaBots)
sys.inicio()
