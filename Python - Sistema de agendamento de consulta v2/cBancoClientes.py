from cClienteDAO import *

class BancoClientes:

    def __init__(self):
        self.__clDao = ClienteDAO()

    def cadastrar(self, idc, n, i, c, sp):
        cl = Cliente()
        cl.set_id_cliente(idc)
        cl.set_nome(n)
        cl.set_idade(i)
        cl.set_cpf(c)
        cl.set_sintoma_principal(sp)
        idc = self.__clDao.cadastrar(cl)
        return idc

    def editar(self, n, i, c, sp, idc):
        cl = Cliente()
        cl.set_nome(n)
        cl.set_idade(i)
        cl.set_cpf(c)
        cl.set_sintoma_principal(sp)
        cl.set_id_cliente(idc)
        self.__clDao.editar(cl)

    def listar_todos(self):
        l = self.__clDao.listar_todos()
        return l

    def listar_id(self, idc):
        p = self.__clDao.listar_id_cliente(idc)
        return p

    def apagar_id(self, idc):
        self.__clDao.apagar(idc)