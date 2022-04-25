
from veiculo import *
from listaVeiculos import *

class Loja:
    
    def __init__(self):
        self.__aVenda = ListaVeiculos()
        self.__vendidos = ListaVeiculos()
        
    def cadastrarVeiculo(self):
        veic=Veiculo()
        veic.lerDados()
        self.__aVenda.addVeiculo(veic)
        
    def escreverAVenda(self):
        print("\n Veiculos a venda")
        self.__aVenda.escreveVeiculos()
    
    
    def escreverVendidos(self):
        print("\n Veiculos já vendidos")
        self.__vendidos.escreveVeiculos()
    
        
    def vender(self):
        nome=input("\n Digite o nome do veiculo?")
        lis=self.__aVenda.procuraVeiculo(nome)
        if (lis.getTamanhoLista()>0):
            lis.escreveVeiculos()
            posi=int(input("Qual a posicao na fila? "))
            if(lis.getTamanhoLista()>posi):
                veic=lis.getVeiculo(posi)
                self.__vendidos.addVeiculo(veic)
                self.__aVenda.apagaVeiculo(veic)
        else:
            print("\n Nenhum veiculo com esse nome encontrado ")
        
        