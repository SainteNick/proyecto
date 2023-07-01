import pygame
from pygame import mixer
import sys

#Constantes----------------------------------------------------------------------------------------------------------

display_a = 1000
display_b = 800

#Escala de sprites---------------------------------------------------------------------------------------------------

scale_factor = 1
min_factor   = 1.0
max_factor   = 5.0

#Transformacion a kilos----------------------------------------------------------------------------------------------

mass       = min_factor =+ 1.1
total_mass = mass // 1

# Posicion Sprites---------------------------------------------------------------------------------------------------

pos_build   = [0, 90]
pos_grass   = [12, 5]
pos_clds    = [300, 20]
pos_bckgrnd = [-220, -20]
pos_floor   = [0,220]
pos_rule    = [325,90]
pos_frame   = [752, 250]
pos_arrow   = [500, 110]

# Posición y velocidad inicial del objeto----------------------------------------------------------------------------

pos_ball  = [550, 100]
object_vel = 0
mass_object = 1

# Gravedad y factor de velocidad-------------------------------------------------------------------------------------

t = 0 

def gravity(mass_object, scale_factor):
    vel_base = 0.5  
    vel      = vel_base / scale_factor  
    return mass_object * vel

# Inicializar Pygame-------------------------------------------------------------------------------------------------

mixer.init()
display    = pygame.display.set_mode((display_a, display_b))
clock      = pygame.time.Clock()
game_state = "setting mode"
count      = 0
timer      = 0

#Pista de audio------------------------------------------------------------------------------------------------------

mixer.music.load("y2mate.com - Super Meat Boy  Digital Special Edition Soundtrack  24 Forest Funk RETRO Ch 1 Warp Zone.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#Sprites-------------------------------------------------------------------------------------------------------------

img_building = pygame.image.load("building2.png")
img_object   = pygame.image.load("object.png")
img_bckgrnd  = pygame.image.load("background.png")
img_clouds   = pygame.image.load("clouds.png")
img_rule     = pygame.image.load("rule.png")
img_frame    = pygame.image.load("frame.png")
img_arrow    = pygame.image.load("arrow.png")

#Funcion de escala de imagenes---------------------------------------------------------------------------------------

def image_edit(image, factor):
    
    width   = int(image.get_width() * factor)
    height  = int(image.get_height() * factor)
    return pygame.transform.scale(image, (width, height))

#Funciones de Pantallas del programa---------------------------------------------------------------------------------

def first_screen():
    bckgrnd = pygame.image.load("first_screen.png").convert()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        display.blit(bckgrnd, (0, 0))
        pygame.display.flip()
first_screen()

def screen2():
    bckgrnd = pygame.image.load("second_screen.png").convert()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        display.blit(bckgrnd, (0, 0))
        pygame.display.flip()
screen2()

#Base del programa---------------------------------------------------------------------------------------------------

game = True

while game:
    
    count += 1
    
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            
            game = False
       
        elif evento.type == pygame.KEYDOWN and game_state == "setting mode":

            if evento.key == pygame.K_ESCAPE:
                
                game = False

            if evento.key == pygame.K_UP:
                
                pos_ball[1] -= 28
                pos_arrow[1] -= 28

            if evento.key == pygame.K_DOWN:
                
                pos_ball[1] += 38
                pos_arrow[1] += 38

            if evento.key == pygame.K_w:
                
                scale_factor += 0.1
                scale_factor = min(scale_factor, max_factor)

            if evento.key == pygame.K_s:
                
                scale_factor -= 0.1
                scale_factor = max(scale_factor, min_factor)

            if evento.key == pygame.K_SPACE:
                
                game_state = "play mode"
                print(game_state)
    
    if game_state == "play mode":
        
        t += 1 / 60
        object_vel += gravity(mass_object, scale_factor)
        pos_ball[1] += object_vel

        if count % 60 == 0:
            
            timer += 1 

        if pos_ball[1] >= display_b - 32:
            
            game_state = "game over"

    if game_state == "game over":
        
        pos_ball[1] = display_b - 32
        print(game_state)
    
    if game_state == "game over":
        
        pos_ball[1] = display_b - 32
        print(game_state)
    
    #Color de ventana

    display.fill((62, 146, 221))  

    #Escalar sprite con factor actual--------------------------------------------------------------------------------
    
    imagen_escala = image_edit(img_object, scale_factor)
    
    #Posicion de los sprites-----------------------------------------------------------------------------------------

    display.blit(img_clouds, pos_clds)
    display.blit(img_building, pos_build)
    display.blit(img_rule, pos_rule)
    display.blit(img_bckgrnd, pos_bckgrnd)
    display.blit(imagen_escala, pos_ball)
    display.blit(img_arrow, pos_arrow)
    display.blit(img_frame, pos_frame)
    
    #Actualizacion de pantalla y velocidad de fotogramas

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()     
