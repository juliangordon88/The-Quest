import pygame
import os

from pygame.sprite import Group
pygame.font.init()
pygame.mixer.init()
from random import *


ANCHO = 900
ALTO = 500
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

SONIDO_DISPARO = pygame.mixer.Sound(os.path.join('imagenes', 'disparo.mp3'))
MUSICA_FONDO = pygame.mixer.Sound(os.path.join('imagenes', '007-theme.mp3'))
FUENTE_VIDAS = pygame.font.SysFont('comicsans', 40)
FPS = 60
VEL = 5
VEL_BALAS = 7
MAX_BALAS = 7
VEL_METEORO = 1

ANCHO_NAVE = 100
ALTO_NAVE = 80

METEOR_DIAGONAL = pygame.image.load(os.path.join('imagenes', 'cometa.png'))
METEORITO = pygame.transform.rotate(METEOR_DIAGONAL, 90)

IMAGEN_NAVE = pygame.transform.scale(pygame.image.load(os.path.join('imagenes', 'nave.png')), (200,200))

IMAGEN_METEORITO = pygame.image.load(os.path.join('imagenes', 'cometa.png'))

FONDO = pygame.transform.scale(pygame.image.load(os.path.join('imagenes', 'fondo-nocturna-galaxia.jpg')), (ANCHO, ALTO))

ICONO = pygame.image.load(os.path.join('imagenes', 'icono.juego.png'))
pygame.display.set_icon(ICONO)



pygame.display.set_caption("The Quest")

pygame.mixer.Sound.play(MUSICA_FONDO, -1)

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IMAGEN_NAVE
        
        self.rect = self.image.get_rect()
        #self.rect.x = ANCHO // 2
        #self.rect.y = ALTO // 2
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y - VEL + 60 > 0:
            self.rect.y -= VEL
        elif keys[pygame.K_DOWN] and self.rect.y + VEL  < 360:
            self.rect.y += VEL



class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagen = IMAGEN_METEORITO
        self.rect = self.imagen.get_rect()
        self.rect.x = ANCHO
        self.rect.y = Random.randint(0, ALTO - self.rect.height)

    def update(self):
        self.rect.x -= VEL_METEORO


all_sprites = pygame.sprite.Group()
nave = Nave()
all_sprites.add(nave)

lista_meteoritos = pygame.sprite.Group()
#for i in range(10):
  #  meteor = Meteorito()
   # lista_meteoritos.add(meteor)
   # all_sprites.add(meteor)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    PANTALLA.blit(FONDO,[0, 0])
    all_sprites.draw(PANTALLA)
    all_sprites.update()
    

    pygame.display.flip()

    

    
    
    

    

    clock.tick(60)

pygame.quit()
