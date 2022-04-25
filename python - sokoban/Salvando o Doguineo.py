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
        window = pygame.display.set_mode((800,950))  # cria a janela passando a tupla com o tamanho da janela
        pygame.display.set_caption('Sokoban')  # titulo da janela
        self.screen = pygame.display.get_surface()   #pega referencia da tela - usado no resto do codigo (self indica que é um atributo)
        print("Inicializado")
        self.carregaImagens()
        self.criaEstruturaDados()
        pygame.mixer.music.load('musica.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)



    def carregaImagens(self): #carrega as imagens do disco para atributos(variáveis)
        self.fundo = pygame.image.load("sok.png") #carrega imagen de fundo        
        self.boneco = pygame.image.load("Doguinho.png") 
        self.caixa = pygame.image.load("PotedeComida.png")
        self.gan = pygame.image.load("win.jpg")
        self.per = pygame.image.load("game-over.jpg")
        
        
    def criaEstruturaDados(self): 
        self.posi={}
        
        v1  = Vizinho(0,2,0,4)
        q1  = Quad((294, 197),0,v1,self.posi)
        self.posi[1]=q1
        
        v2  = Vizinho(1,0,0,5)
        q2  = Quad((384, 197),0,v2,self.posi)   
        self.posi[2]=q2
        
        v3  = Vizinho(0,4,0,0)
        q3  = Quad((204, 287),0,v3,self.posi)   
        self.posi[3]=q3
        
        v4  = Vizinho(3,5,1,6)
        q4  = Quad((294, 287),2,v4,self.posi)   
        self.posi[4]=q4
        
        v5  = Vizinho(4,0,2,7)
        q5  = Quad((384, 287),0,v5,self.posi)   
        self.posi[5]=q5
        
        v6  = Vizinho(0,7,4,8)
        q6  = Quad((294, 377),0,v6,self.posi)   
        self.posi[6]=q6
        
        v7  = Vizinho(6,0,5,9)
        q7  = Quad((384, 377),1,v7,self.posi)   
        self.posi[7]=q7
        
        v8  = Vizinho(0,9,6,12)
        q8  = Quad((294, 467),0,v8,self.posi)   
        self.posi[8]=q8
        
        v9  = Vizinho(8,10,7,13)
        q9  = Quad((384, 467),1,v9,self.posi)   
        self.posi[9]=q9
        
        v10  = Vizinho(9,0,0,14)
        q10 = Quad((474, 467),0,v10,self.posi)   
        self.posi[10]=q10
        
        v11  = Vizinho(0,12,0,15)
        q11 = Quad((204, 557),0,v11,self.posi)   
        self.posi[11]=q11
        
        v12  = Vizinho(11,13,8,16)
        q12 = Quad((294, 557),0,v12,self.posi)   
        self.posi[12]=q12
        
        v13  = Vizinho(12,14,9,17)
        q13 = Quad((384, 557),0,v13,self.posi)   
        self.posi[13]=q13
        
        v14  = Vizinho(13,0,10,18)
        q14 = Quad((474, 557),0,v14,self.posi)   
        self.posi[14]=q14
        
        v15  = Vizinho(0,16,11,0)
        q15 = Quad((204, 647),0,v15,self.posi)   
        self.posi[15]=q15
        
        v16  = Vizinho(15,17,12,0)
        q16 = Quad((294, 647),0,v16,self.posi)   
        self.posi[16]=q16
        
        v17  = Vizinho(16,18,13,0)
        q17 = Quad((384, 647),0,v17,self.posi)   
        self.posi[17]=q17
        
        v18  = Vizinho(17,0,14,0)
        q18 = Quad((474, 647),0,v18,self.posi)   
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
    
    def desenhaGanhou(self):
        self.screen.blit(self.gan,(50,200))
        
    def desenhaPerdeu(self):
        self.screen.blit(self.per,(200,300))
    

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
        self.status="continuar"
        self.laco()

    
    def laco(self):  #laço central do jogo - TODO JOGO TEM UM LAÇO
        while self.fim==False: #enquanto o jogo não terminar, fica nesse laço             
            self.clock.tick(20) #define a velocidade do laço - incluencia jogos onde componentes se movem com o passar do tempo - no jogo da velha não tem incluência 
            self.leTeclado() #chama o metodo que verifica se teve evento vindo do teclado ou se foi fechada a janela
            if (self.status=="continuar"):
                self.atualizaTela()
        print("fechando...")
        pygame.quit()    
                    
    
    def leTeclado(self):  #a leitura do teclado é assincrona, não fica bloqueado esperando usuario fazer algo     
        for event in pygame.event.get(): #verifica se tem algum evento na fila, se tiver eles devem ser tratados
            if event.type == QUIT:   #evento que indica que usuario fechou a janela no X do canto superior direito
                self.fim=True  #coloca True no self.fim, isso fara com que o laço no metodo self.laco() saia, e o programa termine
            if self.status=="continuar":
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
        
        self.atualizaStatus()
        
        if(self.status=="vencedor"):
            self.tab.desenhaGanhou()
            
        if(self.status=="perdeu"):
            self.tab.desenhaPerdeu()
        
        pygame.display.update()
        
    
    def atualizaStatus(self):
        if (self.lista[3].conteudo==1 and self.lista[15].conteudo==1):
            self.status="vencedor"
            
        elif (self.lista[1].conteudo==1 or self.lista[2].conteudo==1 or self.lista[10].conteudo==1 or self.lista[11].conteudo==1 or self.lista[18].conteudo==1):
            self.status="perdeu"

#-----------------------------------------------------------------------------------------


if __name__ == "__main__":    
    print("Iniciando o Jogo")
    jo=Jogo()   #cria o objeto jogo