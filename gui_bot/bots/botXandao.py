from Bot import Bot
from random import randint


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
        return self.__respostas[randint(0, len(self.__respostas)-1)]

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

        self.cria_comandos(Comando(1, "BOM DIA", [
                           "BOM DIA DO ÚLTIMO HERÓI DA TERRA PARA OS CAMPEÕES, SEM PRESSÃO AQUI É XANDÃO, TÁ LIGADO?"]))
        self.cria_comandos(Comando(2, "A TERRA REALMENTE É PLANA?", [
                           "SE TÁ DE BRINCADEIRA COM XANDÃO NÉ, OBVIAMENTE, NÃO É POSSÍVEL, NASA É DE HOLLYWOOD, QUEM ACREDITA NAQUELA NAVE DE TAMPA DE MARMITA?"]))
        self.cria_comandos(Comando(3, "QUEM É ENÉAS?", [
                           "O HOMEM DE VERDADE DOUTOR ENÉAS."]))
        self.cria_comandos(Comando(4, "O QUE TEM NO FINAL DA ESCURIDÃO?", [
                           "NO FINAL DA ESCURIDÃO TEM XANDÃO, TÁ LIGADO?"]))
        self.cria_comandos(Comando(5, "DIVULGA MINHA AMIGA", [
                           "DEPOIS VOCÊ MANDA AÍ A LIVE DA SUA PARCEIRA QUE A GENTE DIVULGA"]))
        self.cria_comandos(Comando(6, "SE CAPOTOU FAZ O QUE?", [
                           "SEGURA NO BRAÇO DO XANDÃO QUE NINGUÉM MORRE."]))
        self.cria_comandos(Comando(7, "VOCÊ JÁ FOI ASSALTADO?", [
                           "CLARO QUE NÃO! QUEM QUE VAI SER LOUCO DE ASSALTAR O SUPER XANDÃO? DANDO 5 SOCOS POR SEGUNDO."]))
        self.cria_comandos(Comando(8, "SUCUMBA XANDÃO", [
                           "SUCUMBA VOCÊ, OTÁRIO. SUPER XANDÃO FOREVER."]))
        self.cria_comandos(Comando(
            9, "PORQUE VOCÊ FALA DE VOCÊ MESMO NA TERCEIRA PESSOA?", ["PORQUE AQUI É XANDÃO."]))
        self.cria_comandos(Comando(10, "XANDÃO, PORQUE CORTOU O CABELÃO?", [
                           "ISSO É UMA LONGA HISTÓRIA. FOI NA CAÇA AOS DEMONIOS, XANDÃO FOI PEGO DESPREVENIDO, TAVA SALVANDO A NOVINHA, E AQUELA ESTÚPIDA, FALEI PRA ELA SAIR DE PERTO, QUE O XANDÃO IA DESTRUIR O DEMÔNIO, MAS ELA FICOU LÁ DE GRAÇA, 'AH NÃO XANDÃO, EU QUERO VER SEU PEITORAL EXALANDO ENERGIA' AÍ FUI SALVAR ELA DO DEMÔNIO, ELE DEU UMA ESPADADA, PEGOU NO CABELO DO XANDÃO. PERDI O CABELO POR CAUSA DAQUELA ANTA. AÍ EU FALEI, 'TA VENDO O SUA ANTA? POR ISSO QUE O XANDÃO FALOU PRA VOCÊ SAIR.'"]))
        self.cria_comandos(Comando(11, "PORQUE VOCÊ FALA COM CAPS LIGADO?", [
                           "O CAPS LOCK LIGADO SIGNIFICA CONVICÇÃO E PERSONALIDADE FORTE, E PEITORAL DE AÇO POR DETRÁS DE QUEM TÁ FALANDO, TÁ LIGADO? É ASSIM QUE FUNCIONA IRMÃO. É ESTILO SUPER XANDÃO. NÃO TEM ESSES NEGÓCIOS DE FICAR FALANDO AINDUHASJD."]))
        self.cria_comandos(Comando(12, "MANDA FOTO DE AGORA", ["""_________oBBBBB8o___oBBBBBBB8,
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

    @property
    def nome(self):
        return self.__nome

    def cria_comandos(self, comando: Comando):
        self.__comandos.append(comando)

    def apresentacao(self):
        return "MEU NOME É XANDÃO. FRUTO DE UMA VONTADE DIVINA, FUI ENVIADO TERRA COM O OBJETIVO DE SALVAR A HUMANIDADE DO PECADO MORTAL NO ÚLTIMO DIA DESTA EXISTÊNCIA. PORÉM, APENAS OS CAMPEÕES DE ESPÍRITO SERÃO SALVOS POR XANDÃO. SIGA-ME E IREMOS TRILHAR JUNTOS O CAMINHO DOS CAMPEÕES."

    def mostra_comandos(self):
        comandos = []

        for comando in self.__comandos:
            comandos.append(comando.mensagem)

        return comandos

        # para_mostrar = ""

        # for comando in self.__comandos:
        #     para_mostrar += "{} - {}\n".format(comando.id, comando.msg)

        # return para_mostrar

        # if para_mostrar == "":
        #     return "NENHUM COMANDO DISPONÍVEL, CRIA AÍ!"

    def executa_comando(self, cmd):
        try:
            cmd = int(cmd)
        except:
            return "É PRA BOTAR UM NÚMERO!!"

        for comando in self.__comandos:
            if comando.id == cmd:
                return comando.getRandomResposta()

        return "DIGITA UM NÚMERO CERTO!!"

    def boas_vindas(self):
        return "SEM PRESSÃO AQUI É XANDÃO! FALA COM O ÚLTIMO HERÓI DA TERRA, FALA!"

    def despedida(self):
        return "NO FINAL DA ESCURIDÃO TEM XANDÃO. NÃO ESQUEÇA DE TRILHAR O CAMINHO DOS CAMPEÕES LADO A LADO COM SUPER XANDÃO. TUDO NOSSO!"
