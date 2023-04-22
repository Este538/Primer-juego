import pygame
import random
import sys

pygame.init()

#constantes
WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

#Jugador
jugador_size = 50
jugador_pos = [WIDTH / 2,  HEIGHT - jugador_size * 2]

#Enemigo(s)
enemigo_size = 50
enemigo_pos = [random.randint(0, WIDTH - enemigo_size), 0]
#ventana
ventana = pygame.display.set_mode((WIDTH, HEIGHT))


game_over = False
clock = pygame.time.Clock()

def detectar_colision(jugador_pos, enemigo_pos):
    jx = jugador_pos[0]
    jy = jugador_pos[1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]

    if( ex >= jx and ex < (jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)):
        if ( ey >= jy and ey < (jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        posicion = jugador_pos[0]
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posicion -= jugador_size
            if event.key == pygame.K_RIGHT:
                posicion += jugador_size
            
            jugador_pos[0] = posicion
    ventana.fill(BLACK)

    if enemigo_pos[1] >= 0 and enemigo_pos[1] < HEIGHT:
        enemigo_pos[1] += 20
    else:
        enemigo_pos[0] = random.randint(0, WIDTH - enemigo_size)
        enemigo_pos[1] = 0 
    if detectar_colision(jugador_pos, enemigo_pos):
        game_over = True
    #dibujar enemigo
    pygame.draw.rect(ventana, BLUE, (enemigo_pos[0], enemigo_pos[1],
                                     enemigo_size, enemigo_size))

    #dibujar jugador
    pygame.draw.rect(ventana, RED, 
                    (jugador_pos[0], jugador_pos[1], 
                    jugador_size, jugador_size))
    
    clock.tick(30)
    pygame.display.update()