from cConsultaDAO import *

class BancoConsulta:

    def __init__(self):
        self.__coDao = ConsultaDAO()

    def Cadastrar(self, i, crm, idc, a, m, d, h, min, hf, mf):
        co = Consulta()
        co.set_id(i)
        co.set_crm_medico(crm)
        co.set_id_cliente(idc)
        co.set_ano(a)
        co.set_mes(m)
        co.set_dia(d)
        co.set_hora(h)
        co.set_minuto(min)
        co.set_hora_fim(hf)
        co.set_minuto_fim(mf)
        id = self.__coDao.cadastrar(co)
        return id

    def editar(self, crm, idc, a, m, d, h, min, hf, mf, i):
        co = Consulta()
        co.set_crm_medico(crm)
        co.set_id_cliente(idc)
        co.set_ano(a)
        co.set_mes(m)
        co.set_dia(d)
        co.set_hora(h)
        co.set_minuto(min)
        co.set_hora_fim(hf)
        co.set_minuto_fim(mf)
        co.set_id(i)
        self.__coDao.editar(co, i)

    def listar_todos(self):
        print(type(self.__coDao))
        l = self.__coDao.listar_todos()
        return l

    def listar_id(self, i):
        p = self.__coDao.listar_id(i)
        return p

    def apagar_id(self, i):
        self.__coDao.apagar(i)