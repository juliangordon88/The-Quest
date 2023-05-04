import pygame
import os
pygame.font.init()
pygame.mixer.init()
from random import *

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('imagenes', 'colision.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('imagenes', 'disparo.mp3'))
GAME_SOUND = pygame.mixer.Sound(os.path.join('imagenes', '007-theme.mp3'))
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 7

METEOR_SPEED = 1

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 80

#YELLOW_HIT = pygame.USEREVENT + 1


cometa_sin_girar = pygame.image.load(os.path.join('imagenes', 'cometa.png'))
cometa = pygame.transform.rotate(cometa_sin_girar, 90)

#cargamos la imagen
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('imagenes', 'nave.png'))
#adaptamos el tamaño de la imagen y la rotamos
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
     YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0) #le pasamos lo que quremos rotar y luego el angulo que la queremos rotar


SPACE = pygame.transform.scale(pygame.image.load(os.path.join('imagenes', 'fondo-nocturna-galaxia.jpg')), (WIDTH, HEIGHT))
icono = pygame.image.load(os.path.join('imagenes', 'icono.juego.png'))
pygame.display.set_icon(icono)

#crear la pantalla del juego 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#le ponemos titulo a la pantalla
pygame.display.set_caption("The Quest")

pygame.mixer.Sound.play(GAME_SOUND, -1)

IMG_METEOR = pygame.image.load(os.path.join('imagenes', 'cometa.png'))

explosiones = [pygame.image.load(os.path.join('imagenes', 'exp1.png')),
               pygame.image.load(os.path.join('imagenes', 'exp2.png')),
               pygame.image.load(os.path.join('imagenes', 'exp3.png')),
               pygame.image.load(os.path.join('imagenes', 'exp4.png')),
               pygame.image.load(os.path.join('imagenes', 'exp5.png')),
               pygame.image.load(os.path.join('imagenes', 'exp6.png')),
               pygame.image.load(os.path.join('imagenes', 'exp7.png')),
               pygame.image.load(os.path.join('imagenes', 'exp8.png')),
               ]
siguiente_imagen = 0
imagen = explosiones[siguiente_imagen]


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.y += 5

all_sprites = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)

class Meteor(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image = IMG_METEOR
          self.rect = self.image.get_rect()
          self.rect.x = WIDTH
          self.rect.y = random.randint(0, HEIGHT - self.rect.height)

     def update(self):
          self.rect.x -= METEOR_SPEED
          


def draw_window(yellow, yellow_bullets, yellow_health): #red_health, yellow_health
        x = 0

        WIN.blit(SPACE, (x, 0))
        #WIN.fill((WHITE)) #le damos color a la pantalla, le pasamos una tupla con 3 valores RGB
        #pygame.draw.rect(WIN, BLACK)

        
        yellow_health_text = HEALTH_FONT.render("Points: " + str(yellow_health), 1, WHITE)
        
        WIN.blit(yellow_health_text,(10, 10))
        
        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #dibujar las nave en la pantalla, se le pasa la imagen y el lugar donde la queremos pintar
        
        
          
     
        for bullet in yellow_bullets:
                pygame.draw.rect(WIN, YELLOW, bullet)
            

        pygame.display.update() 

def yellow_handle_movement(keys_pressed, yellow):
        
        if keys_pressed[pygame.K_w] and yellow.y - VEL + 30 > 0:  #UP
             yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height  -25 < HEIGHT:  #DOWN
             yellow.y += VEL   



def handle_bullets(yellow_bullets, yellow):
    for bullet in yellow_bullets:
          bullet.x += BULLET_VEL
          
        

#Bucle principal del juego donde ejecutaremos todo
def main():
     #definimos un rectangulo que sera la nave, con 4 valores (donde lo creamos(ancho y alto) y el tamaño del rectangulo(ancho y alto)
    yellow = pygame.Rect(10, HEIGHT/2 - SPACESHIP_HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    
    yellow_bullets = []

    
    yellow_health = 5

    all_sprites.update()
    


    all_sprites.draw(WIN)

    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS) #le damos la velocidad que queremos que se juegue
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                
        
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
       
        
     
        handle_bullets(yellow_bullets, yellow)

        draw_window(yellow, yellow_bullets, yellow_health)
        pygame.display.update()
    
    #main()


if __name__ == "__main__":
    main()





