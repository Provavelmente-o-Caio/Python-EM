from cMedicoDAO import *

class BancoMedicos:

    def __init__(self):
        self.__mDao = MedicoDAO()

    def cadastrar(self, cm, n, i, c, e):
        m = Medico()
        m.set_crm(cm)
        m.set_nome(n)
        m.set_idade(i)
        m.set_cpf(c)
        m.set_especializacao(e)
        crm = self.__mDao.cadastrar(m)
        return crm

    def editar(self, n, i, c, e, crm):
        m = Medico()
        m.set_nome(n)
        m.set_idade(i)
        m.set_cpf(c)
        m.set_especializacao(e)
        m.set_crm(crm)
        self.__mDao.editar(m)

    def listar_todos(self):
        l = self.__mDao.listar_todos()
        return l

    def listar_crm(self, crm):
        p = self.__mDao.listar_crm(crm)
        return p

    def apagar_crm(self, crm):
        self.__mDao.apagar(crm)