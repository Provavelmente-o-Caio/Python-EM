from spPessoa import *


class Cliente(Pessoa):
    def __init__(self, n="", c="", sp="", i = 0):
        Pessoa.__init__(self, n, i, c)
        self.__idc = -1
        self.__sintoma_principal = sp

    def set_id_cliente(self, i):
        self.__idc = i

    def get_id_cliente(self):
        return self.__idc

    def set_sintoma_principal(self,sp):
        self.__sintoma_principal = sp

    def get_sintoma_principal(self):
        return self.__sintoma_principal