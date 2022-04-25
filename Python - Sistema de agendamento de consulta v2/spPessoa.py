class Pessoa:

    def __init__(self,n="",i=0,c=""):
        self.__nome = n
        self.__idade = i
        self.__cpf = c

    def set_cpf(self, c):
        self.__cpf = c

    def get_cpf(self):
        return self.__cpf

    def set_nome(self, n):
        self.__nome = n

    def get_nome(self):
        return self.__nome

    def set_idade(self,i):
        self.__idade = i

    def get_idade(self):
        return self.__idade