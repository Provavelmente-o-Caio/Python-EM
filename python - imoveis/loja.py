from imovel import *
from listaimovel import *

class Loja:
    
    def __init__(self):
        self.__Venda = ListaDosImoveis()
        self.__Locacao = ListaDosImoveis()
        self.__Cadastro = ListaDosImoveis()
        
    def CadastrarImovel(self):
        imv=Imovel()
        imv.LerDados()
        self.__Cadastro.AddImovel(imv)
        
    def EscreverCadastro(self):
        print("\n Imoveis Cadastrados:")
        self.__Cadastro.EscreveImovel()
        
    def ColocarVenda(self):
        nome=input("\n Digite o nome da cidade do Imóvel: ")
        lis=self.__Cadastro.ProcuraImovel(nome)
        if(lis.TamanhoLista()>0):
            lis.EscreveImovel()
            posi=int(input("Qual a posição na fila? "))
            if(lis.TamanhoLista()>=posi):
                imv=lis.GetImovel(posi)
                self.__Venda.AddImovel(imv)
                self.__Cadastro.ApgImovel(imv)
        else:
            print("\n Não existe nenhum imovel desta cidade")
            
    def ColocarLocacao(self):
        nome=input("\n Digite o nome da cidade do Imóvel: ")
        lis=self.__Cadastro.ProcuraImovel(nome)
        if(lis.TamanhoLista()>0):
            lis.EscreveImovel()
            posi=int(input("Qual a posição na fila? "))
            if(lis.TamanhoLista()>=posi):
                imv=lis.GetImovel(posi)
                self.__Locacao.AddImovel(imv)
                self.__Cadastro.ApgImovel(imv)
        else:
            print("\n Não existe nenhum imovel desta cidade")
            
    def EscreverVenda(self):
        print("\n Imóveis a venda: ")
        self.__Venda.EscreveImovel()
        
    def EscreverLocacao(self):
        print("\n Imóveis em locação: ")
        self.__Locacao.EscreveImovel()