from spPessoa import *


class Medico(Pessoa):

    def __init__(self,n="", i=0, c="", e=""):
        Pessoa.__init__(self, n, i, c)
        self.__especializacao=e
        self.__crm = -1

    def set_especializacao(self, e):
        self.__especializacao = e

    def get_especializacao(self):
        return self.__especializacao

    def set_crm(self, crm):
        self.__crm = crm

    def get_crm(self):
        return self.__crm