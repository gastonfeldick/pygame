from asyncio import events
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
    def disparar(self):
        print ("disparo")
    def dibujarnave(self,superfice):
        superfice.blit(self.imagenNave, self.rect)

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
        self.velocidadDisparo=0.01
        self.rect.top=posy
        self.rect.left=posx
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)


def main():
    enJuego=True
    pygame.init()
    screen=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Espacio inhóspito")
    fondo=pygame.image.load("imagenes/fondo.jpg")
    
    #objetos
    jugador=naveEspacial()
    DemoProyectil=proyectil(ancho/2 , alto-30)


    while True:
        screen.blit(fondo,(0,0))
        jugador.movimiento()
        DemoProyectil.trayectoria()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if event.type==pygame.KEYDOWN:
                    if event.key==K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    elif event.key==K_RIGHT:
                        jugador.rect.left += jugador.velocidad
                    elif event.key==K_x:
                        jugador.disparar()
        jugador.dibujarnave(screen)
        DemoProyectil.dibujar(screen)
        pygame.display.update()


main()