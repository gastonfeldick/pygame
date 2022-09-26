from platform import python_branch
import pygame, sys

from pygame.locals import *

#crear ventana 
size=(800,500)
pygame.init()


miImagen=pygame.image.load("imagenes/descarga.png")
screen= pygame.display.set_mode(size)
rojo=(0,0,0)
x=0
y=0
bandera=0
def controlLineal(x,band):
  if (band==0):
      
      if(x==300):
            band=1
  elif (band==1):
      x-=1
      if(x==0):
        band=0
  return x,band

def controlteclas(x):
  
  if event.type==pygame.KEYDOWN: #tecla presionada
    if event.key==pygame.K_LEFT:
      x-=30
    elif event.key==pygame.K_RIGHT:
      x+=30
  elif event.type==pygame.KEYUP: #tecla liberad
    if event.key==pygame.K_LEFT:
          x-=30
    elif event.key==pygame.K_RIGHT:
      x+=30  
  return x

while True:
  screen.fill(rojo)
  screen.blit(miImagen,(x,y))
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    x=controlteclas(x)
  
  
  pygame.display.update()  


















"""
                                                 # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                     PROYECTO - BATALLA NAVAL                /
      \                     @ GASTON N. FELDICK                   /
       \_________________________________________________________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww 



"""