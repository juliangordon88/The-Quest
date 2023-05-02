import pygame
import os
pygame.font.init()
pygame.mixer.init()
import random

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#RED = (255, 0 , 0)
YELLOW = (255, 255, 0)

#BORDER = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('imagenes', 'colision.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('imagenes', 'disparo.mp3'))
GAME_SOUND = pygame.mixer.Sound(os.path.join('imagenes', '007-theme.mp3'))
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 7


SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 80

YELLOW_HIT = pygame.USEREVENT + 1
#RED_HIT = pygame.USEREVENT + 2

#red_health = 2
#yellow_health = 2

cometa_sin_girar = pygame.image.load(os.path.join('imagenes', 'cometa.png'))
cometa = pygame.transform.rotate(cometa_sin_girar, 90)
#cargamos la imagen
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('imagenes', 'nave.png'))
#adaptamos el tamaño de la imagen y la rotamos
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
     YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0) #le pasamos lo que quremos rotar y luego el angulo que la queremos rotar

#RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('imagenes', 'nave2.png'))
#RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('imagenes', 'fondo-nocturna-galaxia.jpg')), (WIDTH, HEIGHT))

#crear la pantalla del juego 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#le ponemos titulo a la pantalla
pygame.display.set_caption("The Quest")

pygame.mixer.Sound.play(GAME_SOUND, -1)


def draw_window(yellow, yellow_bullets, yellow_health): #red_health, yellow_health
        WIN.blit(SPACE, (0, 0))
        #WIN.fill((WHITE)) #le damos color a la pantalla, le pasamos una tupla con 3 valores RGB
        #pygame.draw.rect(WIN, BLACK)

        #red_health_text = HEALTH_FONT.render("Points: " + str(red_health), 1, WHITE)
        yellow_health_text = HEALTH_FONT.render("Points: " + str(yellow_health), 1, WHITE)
        #WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10, 10))
        WIN.blit(yellow_health_text,(10, 10))
        
        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #dibujar las nave en la pantalla, se le pasa la imagen y el lugar donde la queremos pintar
        #WIN.blit(RED_SPACESHIP, (red.x, red.y))




        #for bullet in red_bullets:
         #       pygame.draw.rect(WIN, RED, bullet)
        for bullet in yellow_bullets:
                pygame.draw.rect(WIN, YELLOW, bullet)
            

        pygame.display.update() #actualizamos el display para que aparezca el color blanco

def yellow_handle_movement(keys_pressed, yellow):
        #if keys_pressed[pygame.K_a] and yellow.x - VEL + 10 > 0:  #LEFT
        #     yellow.x -= VEL
        #if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width - 5 < BORDER.x:  #RIGHT
         #    yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL + 30 > 0:  #UP
             yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height  -25 < HEIGHT:  #DOWN
             yellow.y += VEL   

"""def red_handle_movement(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width - 15:  #LEFT
             red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width - 15 < WIDTH:  #RIGHT
             red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL  + 10> 0:  #UP
             red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height -10 < HEIGHT:  #DOWN
             red.y += VEL  """

def handle_bullets(yellow_bullets, yellow):
    for bullet in yellow_bullets:
          bullet.x += BULLET_VEL
          #if red.colliderect(bullet):
           #     pygame.event.post(pygame.event.Event(RED_HIT))
            #    yellow_bullets.remove(bullet)
          #elif bullet.x > WIDTH:
           #    yellow_bullets.remove(bullet)
        
                        
    """for bullet in red_bullets:
          bullet.x -= BULLET_VEL
          if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)
          elif bullet.x < 0:
               red_bullets.remove(bullet)"""
     


"""def draw_winner(text):
      draw_text = WINNER_FONT.render(text, 1, WHITE)
      WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT - draw_text.get_width() /2))
      pygame.display.update()
      pygame.time.delay(5000)"""

#Bucle principal del juego donde ejecutaremos todo
def main():
    #red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #definimos un rectangulo que sera la nave, con 4 valores (donde lo creamos(ancho y alto) y el tamaño del rectangulo(ancho y alto)
    yellow = pygame.Rect(10, HEIGHT/2 - SPACESHIP_HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #red_bullets = []
    yellow_bullets = []

    #red_health = 5
    yellow_health = 5

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
                
                #if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                 #   bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                  #  red_bullets.append(bullet)
                   # BULLET_FIRE_SOUND.play()

            #if event.type == RED_HIT:
             #  red_health -= 1
              # BULLET_HIT_SOUND.play()
            #if event.type == YELLOW_HIT:
             #  yellow_health -= 1
              # BULLET_HIT_SOUND.play()
          
     
          
        """winner_text = ""
        if red_health <= 0:
               winner_text = "Yellow Wins!"
        if yellow_health <= 0:
                         winner_text = "Red Wins!"
        if winner_text != "":
              draw_winner(winner_text)
              break  """                    

        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        #red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, yellow)

        draw_window(yellow, yellow_bullets, yellow_health)
    
    main()


if __name__ == "__main__":
    main()
