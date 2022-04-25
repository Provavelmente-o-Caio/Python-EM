import pygame
from pygame.locals import *
import  time

class Vizinho:
    
    def __init__(self,e,d,c,b):
        self.direita = d
        self.esquerda = e
        self.cima = c
        self.baixo = b

class Quad:    
    
    def __init__(self,xy,conteudo,viz,lis):    
        self.xy=xy             #inicia a tupla (x,y) usada para indicar as posicoes cartesianas da celula
        self.conteudo = conteudo      # 0 vazio, 1 caixa 2 boneco
        self.vizinhos=viz
        self.lista=lis
        
    def moverDireita(self):
        ivz1=self.vizinhos.direita
        ovz1=self.lista[ivz1]
        ivz2=ovz1.vizinhos.direita
        ovz2=self.lista[ivz2]
        quadBoneco= self.mover(ovz1,ovz2)
        return quadBoneco
        
    def moverEsquerda(self):
        ivz1=self.vizinhos.esquerda
        ovz1=self.lista[ivz1]
        ivz2=ovz1.vizinhos.esquerda
        ovz2=self.lista[ivz2]
        quadBoneco= self.mover(ovz1,ovz2)
        return quadBoneco
        
    def moverCima(self):
        ivz1=self.vizinhos.cima
        ovz1=self.lista[ivz1]
        ivz2=ovz1.vizinhos.cima
        ovz2=self.lista[ivz2]
        quadBoneco= self.mover(ovz1,ovz2)
        return quadBoneco
    
    
    def moverBaixo(self):
        ivz1=self.vizinhos.baixo
        ovz1=self.lista[ivz1]
        ivz2=ovz1.vizinhos.baixo
        ovz2=self.lista[ivz2]
        quadBoneco= self.mover(ovz1,ovz2)
        return quadBoneco
    
    def mover(self,ovz1,ovz2):
        if(ovz1.conteudo==0):
            ovz1.conteudo=2
            self.conteudo=0
            return ovz1
        elif(ovz1.conteudo==1 and ovz2.conteudo==0):
            ovz2.conteudo=1
            ovz1.conteudo=2    
            self.conteudo=0
            return ovz1
        return self
#--------------------------------------------------------------------------------

class Tabela:  #classe usada para construir o jogo
    
    def __init__(self):  #construtor que inicializa o pygame
        pygame.init() # inicia os modulos  Teclado, Video etc
        window = pygame.display.set_mode((1000,680))  # cria a janela passando a tupla com o tamanho da janela
        pygame.display.set_caption('Sokoban')  # titulo da janela
        self.screen = pygame.display.get_surface()   #pega referencia da tela - usado no resto do codigo (self indica que é um atributo)
        print("Inicializado")
        self.carregaImagens()
        self.criaEstruturaDados()


    def carregaImagens(self): #carrega as imagens do disco para atributos(variáveis)
        self.fundo = pygame.image.load("sok.png") #carrega imagen de fundo        
        self.boneco = pygame.image.load("boneco.png") 
        self.caixa = pygame.image.load("caixa.png") 
        
        
    def criaEstruturaDados(self): 
        self.posi={}
        
        v1  = Vizinho(0,2,0,7)  #esqueda, direita, cima e baixo
        q1  = Quad((205, 209),0,v1,self.posi)
        self.posi[1]=q1
        
        v2  = Vizinho(1,3,0,8)
        q2  = Quad((305, 209),0,v2,self.posi)   
        self.posi[2]=q2
        
        v3  = Vizinho(2,4,0,9)
        q3  = Quad((405, 209),0,v3,self.posi)   
        self.posi[3]=q3
        
        v4  = Vizinho(3,5,0,10)
        q4  = Quad((505, 209),2,v4,self.posi)   
        self.posi[4]=q4
        
        v5  = Vizinho(4,6,0,11)
        q5  = Quad((605, 209),0,v5,self.posi)   
        self.posi[5]=q5
        
        v6  = Vizinho(5,0,0,12)
        q6  = Quad((705, 209),0,v6,self.posi)   
        self.posi[6]=q6
        
        v7  = Vizinho(0,8,1,13)
        q7  = Quad((205, 309),0,v7,self.posi)   
        self.posi[7]=q7
        
        v8  = Vizinho(7,9,2,14)
        q8  = Quad((305, 309),1,v8,self.posi)   
        self.posi[8]=q8
        
        v9  = Vizinho(8,10,3,15)
        q9  = Quad((405, 309),0,v9,self.posi)   
        self.posi[9]=q9
        
        v10  = Vizinho(9,11,4,16)
        q10 = Quad((505, 309),0,v10,self.posi)   
        self.posi[10]=q10
        
        v11  = Vizinho(10,12,5,17)
        q11 = Quad((605, 309),1,v11,self.posi)   
        self.posi[11]=q11
        
        v12  = Vizinho(11,0,6,18)
        q12 = Quad((705, 309),0,v12,self.posi)   
        self.posi[12]=q12
        
        v13  = Vizinho(0,14,7,0)
        q13 = Quad((205, 409),0,v13,self.posi)   
        self.posi[13]=q13
        
        v14  = Vizinho(13,15,8,0)
        q14 = Quad((305, 409),0,v14,self.posi)   
        self.posi[14]=q14
		
        v15  = Vizinho(14,16,9,0)
        q15 = Quad((405, 409),0,v15,self.posi)
        self.posi[15]=q15
		
        v16  = Vizinho(15,17,10,0)
        q16 = Quad((505, 409),0,v16,self.posi)
        self.posi[16]=q16
		
        v17  = Vizinho(16,18,11,0)
        q17 = Quad((605, 409),0,v17,self.posi)
        self.posi[17]=q17
		
        v18  = Vizinho(17,0,12,0)
        q18 = Quad((705, 409),0,v18,self.posi)
        self.posi[18]=q18
		
        
        v0  = Vizinho(0,0,0,0)
        q0 = Quad((0,0),10,v0,self.posi)   
        self.posi[0]=q0
        
        
      
    def desenhaFundo(self):  
        self.screen.blit(self.fundo,(100,100)) 
    
    def desenhaBoneco(self,posi):  
        self.screen.blit(self.boneco,posi) 

    def desenhaCaixa(self,posi):  
        self.screen.blit(self.caixa,posi) 

    def getLista(self):
        return self.posi
    
#-----------------------------------------------------------------
    

class Jogo:  #classe usada para construir o jogo

    def __init__(self):
        self.tab=Tabela()        
        self.lista=self.tab.getLista()
        self.qBoneco=self.lista[4]
        self.fim=False   #atributo usado para indicar o termino do jogo, inicia por false
        self.clock = pygame.time.Clock()  #usado para definir a velocidade do laço
        self.laco()

    
    def laco(self):  #laço central do jogo - TODO JOGO TEM UM LAÇO
        while self.fim==False: #enquanto o jogo não terminar, fica nesse laço             
            self.clock.tick(20) #define a velocidade do laço - incluencia jogos onde componentes se movem com o passar do tempo - no jogo da velha não tem incluência 
            self.leTeclado() #chama o metodo que verifica se teve evento vindo do teclado ou se foi fechada a janela
            self.atualizaTela() 
        print("fechando...")    
        pygame.quit()    
                    
    
    def leTeclado(self):  #a leitura do teclado é assincrona, não fica bloqueado esperando usuario fazer algo     
        for event in pygame.event.get(): #verifica se tem algum evento na fila, se tiver eles devem ser tratados
            if event.type == QUIT:   #evento que indica que usuario fechou a janela no X do canto superior direito
                self.fim=True  #coloca True no self.fim, isso fara com que o laço no metodo self.laco() saia, e o programa termine
            if event.type == KEYDOWN: #uma tecla foi apertada
                pygame.event.pump() #carrega o estado atual do teclado
                key = pygame.key.get_pressed()  #pega o estado atual das teclar que foram carregados
                if (key[pygame.K_UP]): #seta para subir
                    print("Sobe")
                    self.qBoneco=self.qBoneco.moverCima()
                elif (key[pygame.K_DOWN]):#seta pata descer
                    print("Desce")
                    self.qBoneco=self.qBoneco.moverBaixo()
                elif (key[pygame.K_LEFT]): #seta para esquerda
                    print("Esquerda")
                    self.qBoneco=self.qBoneco.moverEsquerda()
                elif (key[pygame.K_RIGHT]): #seta para direita
                    print("Direita")
                    self.qBoneco=self.qBoneco.moverDireita()
    
    
    def atualizaTela(self):  #redesenha a tela com base nas estruturas de dados
        self.tab.desenhaFundo()
        for x in range(1,19):   
            qd=self.lista[x]
            if(qd.conteudo==1):  
                self.tab.desenhaCaixa(qd.xy) 
            elif(qd.conteudo==2):  
                self.tab.desenhaBoneco(qd.xy) 
                
        pygame.display.update() 
        
        

#-----------------------------------------------------------------------------------------


if __name__ == "__main__":    
    print("Iniciando o Jogo")
    jo=Jogo()   #cria o objeto jogo
