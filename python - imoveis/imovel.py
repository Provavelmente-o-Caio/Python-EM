class Imovel:

    def __init__(self):
        self.__proprietario=""
        self.__cidade=""
        self.__rua=""
        self.__numero=0
        self.__lista=[]

    def LerDados(self):
        print("Digite o nome do proprietário: ")
        self.__proprietario=input()
        print("Difite o nome da cidade :")
        self.__cidade=input()
        print("Digite o nome da rua do imóvel:")
        self.__rua=input()
        print("Digite o número da casa: ")
        self.__numero=int(input())
        
    def EscreverDados(self):
        print("Proprietário: ",self.__proprietario)
        print("Cidade: ",self.__cidade)
        print("Rua: ",self.__rua)
        print("Número: ",self.__numero)
        
    def GetRua(self):
        return self.__rua