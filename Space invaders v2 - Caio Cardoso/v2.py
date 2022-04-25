import math
import random

import pygame
from pygame import mixer

class Personagem:  #superclasse

    def __init__(self,x,y,mx,my ,s):
        self.perX = x  
        self.perY = y  
        self.perX_muda = mx
        self.perY_muda = my 
        self.scr=s 
        self.iPer = None
    
    def setMx(self,mx):  
        self.perX_muda = mx
    
    def setMy(self,my):  
        self.perY_muda = my
        
    def inverteMx(self):
        self.perX_muda = self.perX_muda * -1        
        
    def inverteMy(self):
        self.perY_muda = self.perY_muda * -1

    def movimentaXD(self):  #esquerda
        self.perX += self.perX_muda
        
    def movimentaXE(self):  #direita
        self.perX -= self.perX_muda

    def movimentaYB(self):  #baixo
        self.perY += self.perY_muda
        
    def movimentaYC(self):  #cima
        self.perY -= self.perY_muda


    def desenha(self): 
        self.scr.blit(self.iPer, (self.perX,self.perY))
    
    def getX(self): 
        return self.perX
    
    def getY(self): 
        return self.perY
    
#---------------------------------------------------------------------------------

class Nave(Personagem):  #herda tudo do personagem

    def __init__(self,x,y,mx,s):
        super().__init__(x,y,mx,0,s)  #chama construtor da superclasse colocando 0 em my pois y nao move na nave
        self.iPer = pygame.image.load('player.png')  #adiciona a imagem
        self.direcao = "d"
    
    def movimentaXD(self):  #esquerda
        if (self.perX < 736):
            super().movimentaXD()
        
    def movimentaXE(self):  #direita
        if (self.perX > 0):
            super().movimentaXE()
        

#------------------------------------------------------------------------------------
    
class Fantasma(Personagem):  
    
    def __init__(self,x,y,mx,my,s,j):
        super().__init__(x,y,mx,my,s)
        self.iPer = pygame.image.load('enemy.png')
        self.iPer2 = pygame.image.load('enemy2.png')
        self.jogo=j   #atributo que nao existia na superclasse
        self.ponto=1
        self.direcao = "d"
        self.reposiciona()
    
    def movimenta(self): #movimenta fantasma
        if(self.direcao=="d"):
            self.movimentaXD()  #chamou o movimentaXD direita da superclasse
            if self.perX >= 736:
                self.direcao = "e"
                self.movimentaYB()
        if(self.direcao=="e"):
            self.movimentaXE()  #chamou o movimentaXE esquerda da superclasse
            if self.perX < 0:
                self.direcao = "d"
                self.movimentaYB()
                
    def reposiciona(self):
        self.perX = random.randint(0, 736)  #reposiciona fantasma no topo da tela x randomico
        self.perY = random.randint(50, 150) #reposiciona fantasma no topo da tela y randomico
        
    def desenha(self):   #desenha o fantasma
        b=self.jogo.getBala()  #antes de desenhar pega a bala do jogo para ver se colidiu
       
        if(b!=None and b.getEstado()!="fim"):  #se a bala foi criada e esta ativa testa a colisao
            colidiu=self.testaColisao(b) #testa colisao
        else:
            colidiu=False
            
        if(colidiu==False):  #se a colisao for falsa 
            self.movimenta()  #movimenta o fantasma avisando se ele chegou ate a nave
        else: #se colidiu 
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()  #barulho de esplosao
            b.setEstado("fim")  #coloca a bala como estourada (inativa)
            self.jogo.addPlacar(self.ponto)  #soma placar
            self.reposiciona()
        
        self.scr.blit(self.iPer, (self.perX,self.perY))
        
    def desenha2(self):   #desenha o fantasma
        b=self.jogo.getBala()  #antes de desenhar pega a bala do jogo para ver se colidiu
       
        if(b!=None and b.getEstado()!="fim"):  #se a bala foi criada e esta ativa testa a colisao
            colidiu=self.testaColisao(b) #testa colisao
        else:
            colidiu=False
            
        if(colidiu==False):  #se a colisao for falsa 
            self.movimenta()  #movimenta o fantasma avisando se ele chegou ate a nave
        else: #se colidiu 
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()  #barulho de esplosao
            b.setEstado("fim")  #coloca a bala como estourada (inativa)
            self.jogo.addPlacar(5)  #soma placar
            self.reposiciona()
        
        self.scr.blit(self.iPer2, (self.perX,self.perY))
        
    def testaColisao(self,b):   #testa colisao da bala com fantasma     
        distancia= math.sqrt(math.pow(self.perX - b.getX(), 2) + (math.pow(self.perY - b.getY(), 2)))
        if distancia < 27:
            return True
        else:
            return False

#-------------------------------------------------------------------------------------------------

class Bala(Personagem):  #sera criada varias balas, uma de cada vez no momento de apertar o espaco
    
    def __init__(self,x,y,my,s):   #bala é criado na ponta da nave, se move penas em y
        super().__init__(x,y,0,my,s)
        self.iPer = pygame.image.load('bullet.png')
        self.perX = self.perX+16
        self.perY = self.perY-10
        self.somTiro = mixer.Sound("laser.wav")  #som no momento da criação
        self.somTiro.play()
        self.estado="fogo"
   
   
    def desenha(self):
        if self.perY <= 0:   #se a bala chegar ao topo é inativada          
            self.estado = "fim"
        if self.estado=="fogo":   #se esta ativa ela sobe a cada vez que é desenhada
            self.movimentaYC()            
            super().desenha()

    def getEstado(self):
        return self.estado
    
    def setEstado(self, e):
        self.estado=e
    
#-------------------------------------------------------------------------------------------------    

class Fundo: #criado apenas um objeto fundo

    def __init__(self,x,y,s):
        self.iFundo = pygame.image.load('background.png')
        self.fundoX = x
        self.fundoY = y
        self.scr=s
        
    def desenha(self):
        self.scr.blit(self.iFundo, (self.fundoX ,self.fundoY))

#-----------------------------------------------------------------------------------------------

class Texto:  #criado apenas um objeto texto usado para escrever na tela
    
    def __init__(self,s):
        self.placar_fonte = pygame.font.Font('freesansbold.ttf', 32)
        self.fim_fonte = pygame.font.Font('freesansbold.ttf', 64)
        self.scr=s
    
    def mostra_placar(self,valor):  #escreve placar
        txt_placar = self.placar_fonte.render("Placar : " + str(valor), True, (255, 255, 255))
        self.scr.blit(txt_placar, (10, 10))

    def mostrar_fim_jogo(self):  #escreve fim jogo
        txt_fim = self.fim_fonte.render("GAME OVER", True, (255, 255, 255))
        self.scr.blit(txt_fim, (200, 250))


#------------------------------------------------------------------------------------------------


class Jogo:  # Criado o jogo no main

    def __init__(self):
        self.jogando=True
        self.placar=0
        pygame.init()
        screen = pygame.display.set_mode((800, 600))  #cria o screen que é passado para ps objetos

        pygame.display.set_caption("Space Invader v2")
        icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(icon)

        # Carrega som
        mixer.music.load("background.wav")
        mixer.music.play(-1)

        self.numero_fantasmas = 6
        self.vOFantasmas=[]    #lista onde estarao os 6 fantasmas
        for i in range(self.numero_fantasmas):
            fan=Fantasma(0,0,4,40,screen,self)   #cria os fantasmas em posicao aleatoria
            self.vOFantasmas.append(fan)  #adiciona fantasma na lista
            
        self.oNave=Nave(370,480,5,screen)  #cria a nave
        
        self.oBala=None   #declara um atributo onde serão criados as balas, uma de cada vez  None indica que nao tem objeto ainda
        self.oFundo=Fundo(0,0,screen)  #cria objeto o fundo
        self.oTexto=Texto(screen)  #cria objeto texto
        self.Jogar(screen)  #chama metodo jogar


    def Jogar(self,s):
        clock = pygame.time.Clock()
        self.scr=s

        running = True
        while running:   #laço do jogo
            clock.tick(60)    

            # RGB = Red, Green, Blue
            self.scr.fill((0, 0, 0))
            self.oFundo.desenha() #desenha fundo dentro do objeto fundo
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            if(self.jogando==True):
                    if event.type == pygame.KEYDOWN:  #aperta botao
                        if event.key == pygame.K_LEFT:
                            self.oNave.movimentaXE()   #se seta esquerda muda direção da nave para esqueda
                        if event.key == pygame.K_RIGHT:
                            self.oNave.movimentaXD()      #se seta direita muda direção da nave para direita
                        if event.key == pygame.K_SPACE:  #apertou o espaco
                            if(self.oBala==None or self.oBala.getEstado()=="fim"):  #se a bala nao foi criada ou se estiver inativa, cria bala nova
                                self.oBala=Bala(self.oNave.getX(),480,10,self.scr)

            if(self.jogando==True):   #se o jogo ainda nao terminou, fantasma nao chegou na nave
                self.oNave.desenha()  #desenha nave
                
                if(self.oBala!=None and self.oBala.getEstado()!="fim"):   #se a bala foi criada e esta ativa
                    self.oBala.desenha()  #desenha bala
                
                for i in range(self.numero_fantasmas):  #percorre a lista para desenhar os 6 fantasmas
                    fant=self.vOFantasmas[i]
                    if (i<4):
                        fant.desenha()   #desenha o fantasma e pega o estatus em r indicando se chego ate a nave
                    else:
                        fant.desenha2()
                    if(fant.getY()>450):  #se alguma nave chegou ate a linha da nave
                        self.jogando=False
                        
            else: #se jogo acabou mostra o GameOver
                self.oTexto.mostrar_fim_jogo()


            self.oTexto.mostra_placar(self.placar)  #mostra placar
            pygame.display.update()  #atualiza tela

        pygame.quit() #se clicou no X da janela, fecha o jogo


    def addPlacar(self, pontos):
        self.placar+=pontos

    def getBala(self):
        return self.oBala


    
if __name__=="__main__":
    j=Jogo()  #inicia o jogo
    
        