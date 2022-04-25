import math
import random

import pygame
from pygame import mixer


class Nave:  #será criado apenas um objeto nave

    def __init__(self,x,y,mx,s):
        self.iNave = pygame.image.load('player.png')
        self.naveX = x   #posicao x
        self.naveY = y   #posicao y
        self.naveX_muda = mx #valor a ser somado em x cada ver que desenhar (simula movimento)
        self.scr=s  #screen para desenhar
  
    def setMx(self,mx):  #altera o mx para ir de um lado para o outro
        self.naveX_muda = mx

    def desenha(self):  #desenha a nave nao deixando sair para fora das bordas
        self.naveX += self.naveX_muda
        if self.naveX <= 0:
            self.naveX = 0
        elif self.naveX >= 736:
            self.naveX = 736

        self.scr.blit(self.iNave, (self.naveX,self.naveY))
    
    
    def getX(self):  # pega o valor de x usado para indicar a posicao a ser desenhada a bala
        return self.naveX
    



class Fantasma:  #serão criados 6 objetos fantasma dentro de uma lista
    
    def __init__(self,x,y,mx,my,s,j):
        self.iFantasma = pygame.image.load('enemy.png')        
        self.fantasmaX = x #posicao x do fantasma 
        self.fantasmaY = y #posicao y do fantasma
        self.fantasmaX_muda = mx #valor a ser somado em x cada vez que desenha
        self.fantasmaY_muda = my  #valor a ser somado em y cada vez que desenha  
        self.scr=s  #screen para desenhar
        self.jogo=j  #ponteiro para o objeto jogo, para poder pegar a bala e ver se tem colisao

    def setY(self,y):  #permite alterar o y do fantasma
        self.fantasmaY = y

    def desenha(self):   #desenha o fantasma
        b=self.jogo.getBala()  #antes de desenhar pega a bala do jogo para ver se colidiu
        
        if(b!=None and b.getEstado()!="fim"):  #se a bala foi criada e esta ativa testa a colisao
            colidiu=self.testaColisao(b) #testa colisao
        else:
            colidiu=False
            
        if(colidiu==False):  #se a colisao for falsa 
            return self.movimenta()  #movimenta o fantasma avisando se ele chegou ate a nave
        else: #se colidiu 
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()  #barulho de esplosao
            b.setEstado("fim")  #coloca a bala como estourada (inativa)
            self.jogo.addPlacar()  #soma placar
            
            self.fantasmaX = random.randint(0, 736)  #reposiciona fantasma no topo da tela x randomico
            self.fantasmaY = random.randint(50, 150) #reposiciona fantasma no topo da tela y randomico
            
            

    def movimenta(self): #movimenta fantasma
        self.fantasmaX += self.fantasmaX_muda  #soma valor do vomimento x que pode ser para mais ou menos
        if self.fantasmaX <= 0: #verifica se na proxima deve somar valor positivo
            self.fantasmaX_muda = 4       
            self.fantasmaY += self.fantasmaY_muda
        elif self.fantasmaX >= 736: #verifica se na proxima deve somar valor negativo
            self.fantasmaX_muda = -4
            self.fantasmaY += self.fantasmaY_muda
                    
        self.scr.blit(self.iFantasma, (self.fantasmaX,self.fantasmaY)) #movimenta x que é sempre para baixo
        
        if(self.fantasmaY > 440):  #verifica se fantasma chegou ate a nave
            return True
        else:
            return False


    def testaColisao(self,b):   #testa colisao da bala com fantasma     
        distancia= math.sqrt(math.pow(self.fantasmaX - b.getX(), 2) + (math.pow(self.fantasmaY - b.getY(), 2)))
        if distancia < 27:
            return True
        else:
            return False



class Bala:  #sera criada varias balas, uma de cada vez no momento de apertar o espaco
    
    def __init__(self,x,y,my,s):   #bala é criado na ponta da nave, se move penas em y
        self.iBala = pygame.image.load('bullet.png')
        self.balaX = x+16
        self.balaY = y-10
        self.balaY_muda = my
        self.scr=s
        self.somTiro = mixer.Sound("laser.wav")  #som no momento da criação
        self.somTiro.play()
        self.estado="fogo"
   
    def desenha(self):
        if self.balaY <= 0:   #se a bala chegar ao topo é inativada          
            self.estado = "fim"
        if self.estado=="fogo":   #se esta ativa ela sobe a cada vez que é desenhada
            self.balaY=self.balaY-self.balaY_muda            
            self.scr.blit(self.iBala, (self.balaX,self.balaY))

    def getEstado(self):
        return self.estado
    
    def setEstado(self, e):
        self.estado=e
    
    def getX(self):
        return (self.balaX)
    
    def getY(self):
        return (self.balaY)
    

class Fundo: #criado apenas um objeto fundo

    def __init__(self,x,y,s):
        self.iFundo = pygame.image.load('background.png')
        self.fundoX = x
        self.fundoY = y
        self.scr=s
        
    def desenha(self):
        self.scr.blit(self.iFundo, (self.fundoX ,self.fundoY))


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





class Jogo:  # Criado o jogo no main

    def __init__(self):
        self.jogando=True
        self.placar=0
        pygame.init()
        screen = pygame.display.set_mode((800, 600))  #cria o screen que é passado para ps objetos

        pygame.display.set_caption("Space Invader")
        icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(icon)

        # Carrega som
        mixer.music.load("background.wav")
        mixer.music.play(-1)

        self.numero_fantasmas = 6
        self.vOFantasmas=[]    #lista onde estarao os 6 fantasmas
        for i in range(self.numero_fantasmas):
            x=random.randint(0, 736)
            y=random.randint(50, 150)
            fan=Fantasma(x,y,4,40,screen,self)   #cria os fantasmas em posicao aleatoria
            self.vOFantasmas.append(fan)  #adiciona fantasma na lista
            
        self.oNave=Nave(370,480,0,screen)  #cria a nave
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
                            self.oNave.setMx(-5)   #se seta esquerda muda direção da nave para esqueda
                        if event.key == pygame.K_RIGHT:
                            self.oNave.setMx(5)    #se seta direita muda direção da nave para direita
                        if event.key == pygame.K_SPACE:  #apertou o espaco
                            if(self.oBala==None or self.oBala.getEstado()=="fim"):  #se a bala nao foi criada ou se estiver inativa, cria bala nova
                                self.oBala=Bala(self.oNave.getX(),480,10,self.scr)

                    if event.type == pygame.KEYUP:  #soltou tecla
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  #se soltou esquerda ou direta, coloca movimento nave como zero
                            self.oNave.setMx(0)
                
            
            if(self.jogando==True):   #se o jogo ainda nao terminou, fantasma nao chegou na nave
                self.oNave.desenha()  #desenha nave
                
                if(self.oBala!=None and self.oBala.getEstado()!="fim"):   #se a bala foi criada e esta ativa
                                self.oBala.desenha()  #desenha bala
                
                for i in range(self.numero_fantasmas):  #percorre a lista para desenhar os 6 fantasmas
                    r=self.vOFantasmas[i].desenha()   #desenha o fantasma e pega o estatus em r indicando se chego ate a nave             
                    if r==True:  #testa se chegou ate a nave
                        self.jogando=False  #jogo terminou 
                        break #quebra o laço
            else: #se jogo acabou mostra o GameOver
                self.oTexto.mostrar_fim_jogo()


            self.oTexto.mostra_placar(self.placar)  #mostra placar
            pygame.display.update()  #atualiza tela

        pygame.quit() #se clicou no X da janela, fecha o jogo


    def addPlacar(self):
        self.placar+=1

    def getBala(self):
        return self.oBala


    
if __name__=="__main__":
    j=Jogo()  #inicia o jogo
    
        