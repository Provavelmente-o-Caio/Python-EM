from loja import *

class Menu:
    
    def __init__(self):
        self.MenuLoja=Loja()
        self.LeOpcao()
        
    def MostrarOpcoes(self):
        print("\n\n")
        print("\n Escolha uma opção:")
        print("\n 0 - Sair")
        print("\n 1 - Cadastrar Imovel")
        print("\n 2 - Mostrar Imóveis cadastrados")
        print("\n 3 - Colocar imóvel para locação")
        print("\n 4 - Colocar Imóvel a venda")
        print("\n 5 - Mostrar todos os imóveis para locação")
        print("\n 6 - Mostrar todos os imóveis para venda")
        
    def LeOpcao(self):
        op=100
        while(op>0):
            self.MostrarOpcoes()
            op = int(input())
            
            if(op==1):
                self.MenuLoja.CadastrarImovel()
            elif(op==2):
                self.MenuLoja.EscreverCadastro()
            elif(op==3):
                self.MenuLoja.ColocarLocacao()
            elif(op==4):
                self.MenuLoja.ColocarVenda()
            elif(op==5):
                self.MenuLoja.EscreverLocacao()
            elif(op==6):
                self.MenuLoja.EscreverVenda()