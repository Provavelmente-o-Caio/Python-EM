from veiculo import *

class ListaVeiculos:
    
    def __init__(self):
        self.__lista=[]
        
        
    def addVeiculo(self,veic):
        self.__lista.append(veic)
                    
    def apagaVeiculo(self,veic):
        self.__lista.remove(veic)
       
       
    def getVeiculo(self,posi):
        return self.__lista[posi]
        
        
    def escreveVeiculos(self):
        a=0
        for veic in self.__lista:
            print(">>>>>>>> Fila:",a,"<<<<<<<<")
            veic.escreverDados()
            a+=1
        
    def getTamanhoLista(self):
        return len(self.__lista)
    
    
    def procuraVeiculo(self,nome):
        lis = ListaVeiculos()
        for veic in self.__lista:
            if (veic.getNome()==nome):
                lis.addVeiculo(veic)
        return lis
   