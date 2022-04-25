
from loja import *

class Menu:
    
    def __init__(self):
        self.mLoja=Loja()
        self.leOpcao()
        
        
        
    def mostraOpcoes(self):
        print("\n\n")
        print("0 sair")
        print("1 cadastrar veiculo")
        print("2 mostrar veiculos a venda")
        print("3 mostrar veiculos vendidos")
        print("4 vender veiculo")
        print("ESCOLHA UMA OPÇÃO ?")
        
    def leOpcao(self):
        op=100
        while(op>0):
            self.mostraOpcoes()
            op = int(input())
        
            if(op==1):
                self.mLoja.cadastrarVeiculo()
            elif(op==2):
                self.mLoja.escreverAVenda()
            elif(op==3):
                self.mLoja.escreverVendidos()
            elif(op==4):
                self.mLoja.vender()
            