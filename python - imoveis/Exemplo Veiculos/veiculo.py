
class Veiculo:
    
    def __init__(self):
        self.__nome=""
        self.__marca=""
        self.__ano=""
        
    def lerDados(self):
        self.__nome=input("Nome do veiculo? ")
        self.__marca=input("Marca do veiculo? ")
        self.__ano=int(input("Ano do veiculo? "))
        
    def escreverDados(self):
        print("Nome  :",self.__nome)
        print("Marca :",self.__marca)
        print("Ano   :",self.__ano)
        
    def getNome(self):
        return self.__nome
    
    
              