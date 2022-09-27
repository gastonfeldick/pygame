from asyncio import events
from cmath import rect
from time import time
import pygame,sys
from pygame.locals import *


#Variables globales

ancho=900
alto=480

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave=pygame.image.load("imagenes/nave.jpg")

        self.rect=self.imagenNave.get_rect() #devuelve un rectangulo de la nave
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30
        self.listadisparo=[]
        self.vida=True
        self.velocidad=20
    def disparar(self,x,y):
        miproyectil=proyectil(x,y)
        self.listadisparo.append(miproyectil)
        print ("disparo")
    def dibujarnave(self,superfice):
        superfice.blit(self.imagenNave, self.rect)

    def movimientoDerecha(self):
        self.rect.right+=self.velocidad
        self.movimiento()

    def movimientoIzquierda(self):
        self.rect.left-=self.velocidad
        self.movimiento()

    def movimiento(self):
        if self.vida==True:
            if self.rect.left <=0:
                self.rect.left=0
            elif self.rect.right >900:
                self.rect.right=900

class proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil=pygame.image.load("imagenes/disparoa.jpg")
        self.rect=self.imageProyectil.get_rect()
        self.velocidadDisparo=1
        self.rect.top=posy
        self.rect.left=posx
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidadDisparo
        """
        if(self.rect.top==5):
            self.rect.top=alto-30
        self.rect.top = self.rect.top - self.velocidadDisparo
        
        if self.rect.left <=45:
            self.rect.left=45

        elif self.rect.right >=850:
            self.rect.right=850
        """
    def dibujar(self,superficie): 
        superficie.blit(self.imageProyectil,self.rect)

class invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.imageInvasorA=pygame.image.load("imagenes/marcianoA.jpg")
        self.imageInvasorB=pygame.image.load("imagenes/MarcianoB.jpg")

        self.listaImagenes=[self.imageInvasorB,self.imageInvasorA]
        self.posimagen=0
        self.imagenInvasor=self.listaImagenes[self.posimagen]
        self.rect=self.imagenInvasor.get_rect()
        self.velocidad=1
        self.rect.top=posy
        self.rect.left=posx
        self.listaDisparo=[]

        self.tiempocambio=1

    def dibujar(self,superficie): 
        self.imagenInvasor=self.listaImagenes[self.posimagen]
        superficie.blit(self.imagenInvasor,self.rect)

    def comportamiento(self,tiempo):
        if self.tiempocambio==tiempo:
            self.posimagen+=1
            self.tiempocambio+=1
            
            if self.posimagen> len(self.listaImagenes)-1:
                self.posimagen=0



def main():
    enJuego=True
    pygame.init()
    screen=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Espacio inhóspito")
    fondo=pygame.image.load("imagenes/fondo.jpg")
    
    #objetos
    jugador=naveEspacial()
    #DemoProyectil=proyectil((ancho/2)-5 , alto-100)
    reloj=pygame.time.Clock()
    enemigo=invasor(100,100)
    
    while True:
        screen.blit(fondo,(0,0))
        tiempo=(pygame.time.get_ticks())/1000
        tiempo=int(tiempo)
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if event.type==pygame.KEYDOWN:
                    if event.key==K_LEFT:
                        jugador.movimientoIzquierda()
                        
                    elif event.key==K_RIGHT:
                        jugador.movimientoDerecha()
                        
                    elif event.key==K_x:

                        x,y=jugador.rect.center
                        jugador.disparar(x,y)
        
        
        
        jugador.dibujarnave(screen)
        enemigo.comportamiento(tiempo)
        enemigo.dibujar(screen)
        if len(jugador.listadisparo)>0:
            for x in jugador.listadisparo:
                x.dibujar(screen)
                x.trayectoria()

                if x.rect.top<100:
                    jugador.listadisparo.remove(x)
        print(tiempo)
        pygame.display.update()


main()