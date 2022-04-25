from imovel import *

class ListaDosImoveis:
    
    def __init__(self):
        self.__lista=[]
        
    def AddImovel(self,imv):
        self.__lista.append(imv)
        
    def ApgImovel(self,imv):
        self.__lista.remove(imv)
        
    def GetImovel(self,posi):
        return self.__lista[posi]
    
    def EscreveImovel(self):
        a=0
        for imv in self.__lista:
            print("Fila: ",a,"(╥﹏╥)")
            imv.EscreverDados()
            a=a+1
            
    def TamanhoLista(self):
        return len(self.__lista)
    
    def ProcuraImovel(self,nome):
        lis = ListaDosImoveis()
        for imv in self.__lista:
            if (imv.GetRua()==nome):
                lis.AddImovel(imv)
        return lis