from asyncio import events

import pygame,sys

from pygame.locals import *


#Variables globales
ancho=800
alto=500



pygame.init()
screen=pygame.display.set_mode((ancho,alto))
while True:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.exit()
            sys.exit()

    pygame.display.update()
