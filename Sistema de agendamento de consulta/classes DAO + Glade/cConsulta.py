from cMedico import *
from cCliente import *


class Consulta:

    def __init__(self, d = 0, m = 0, a = 0, h = 0, min = 0, crmm = None, idc = None):
        self.__dia = d
        self.__mes = mFazeexw
        self.__ano = a
        self.__hora = h
        self.__minuto = min
        self.__crm_medico = crmm
        self.__id_cliente = idc
        self.__id_consulta = -1
        self.__horaf = hf
        self.__minutof = mf

    def set_dia(self, d):
        self.__dia = d

    def get_dia(self):
        return self.__dia

    def set_mes(self, m):
        self.__mes = m

    def get_mes(self):
        return self.__mes

    def set_ano(self, a):
        self.__ano = a

    def get_ano(self):
        return self.__ano

    def set_hora(self,h):
        self.__hora = h

    def get_hora(self):
        return self.__hora

    def set_minuto(self,min):
        self.__minuto = min

    def get_minuto(self):
        return self.__minuto

    def set_id(self, i):
        self.__id_consulta = i

    def get_id(self):
        return self.__id_consulta

    def set_hora_fim(self, hf):
        self.__horaf = hf

    def get_hora_fim(self):
        return self.__horaf

    def set_minuto_fim(self, mf):
        self.__minutof = mf

    def get_minuto_fim(self):
        return self.__minutof

    def set_crm_medico(self,crmm):
        self.__crm_medico = crmm

    def get_crm_medico(self):
        return self.__crm_medico

    def set_id_cliente(self, idc):
        self.__id_cliente = idc

    def get_id_cliente(self):
        return self.__id_cliente