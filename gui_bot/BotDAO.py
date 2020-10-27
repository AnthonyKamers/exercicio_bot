from DAO import DAO
from Bot import Bot
import pickle


class BotDAO(DAO):
    def __init__(self, datasource='bots.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, bot: Bot):
        self.__object_cache[bot.nome] = bot
        self.__dump()

    def get(self, nome: str):
        try:
            return self.__object_cache[nome]
        except KeyError:
            return False

    def remove(self, bot: Bot):
        try:
            self.__object_cache.pop(bot.nome)
            self.__dump()
        except KeyError:
            return False

    def get_all(self):
        return self.__object_cache.values()
