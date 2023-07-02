import pygame
from pygame import mixer
import sys

#Ventana y color de texto---------------------------------------------------------------------------------------------------------

display_a = 1000
display_b = 800
t_color   = (219,22,26)

#Escala de sprites--------------------------------------------------------------------------------------------------

scale_factor = 1
min_factor   = 1.0
max_factor   = 5.0

# Posicion Sprites--------------------------------------------------------------------------------------------------

pos_build   = [0, 90]
pos_grass   = [12, 5]
pos_clds    = [300, 20]
pos_bckgrnd = [-220, -20]
pos_floor   = [0, 220]
pos_rule    = [325, 90]
pos_frame   = [752, 250]
pos_arrow   = [400, 750]
pos_text    = [775, 300]

# Posición y velocidad inicial del objeto---------------------------------------------------------------------------

pos_ball    = [450, 750]
object_vel  = 0

# Masa objeto-------------------------------------------------------------------------------------------------------

mass_object = 1
mass_plus   = 1.5
mass_limit  = 61

# Gravedad y factor de velocidad------------------------------------------------------------------------------------

t = 0 

def gravity(mass_object, scale_factor):
    vel_base = 0.5  
    vel      = vel_base / scale_factor  
    return mass_object * vel

# Inicializar Pygame------------------------------------------------------------------------------------------------

pygame.font.init()
mixer.init()
display     = pygame.display.set_mode((display_a, display_b))
clock       = pygame.time.Clock()
font_route  = "Grand9K Pixel.ttf"
font        = pygame.font.Font(font_route, 20)
font2       = pygame.font.Font(font_route, 15)
text_mass   = font.render("Total Mass: " + str(mass_object ) + "Kg", True, t_color)
text_height = font.render("Height: 0m", True, t_color)
text_energy = font.render("Energy: 0Joules", True, t_color)
game_state  = "setting mode"
count       = 0
timer       = 0

# Pista de audio----------------------------------------------------------------------------------------------------

mixer.music.load("y2mate.com - Super Meat Boy  Digital Special Edition Soundtrack  24 Forest Funk RETRO Ch 1 Warp Zone.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Sprites-----------------------------------------------------------------------------------------------------------

img_building = pygame.image.load("building2.png")
img_object   = pygame.image.load("object.png")
img_bckgrnd  = pygame.image.load("background.png")
img_clouds   = pygame.image.load("clouds.png")
img_frame    = pygame.image.load("frame.png")
img_arrow    = pygame.image.load("arrow.png")

# Funcion de escala de imagenes-------------------------------------------------------------------------------------

def image_edit(image, factor):
    
    width   = int(image.get_width() * factor)
    height  = int(image.get_height() * factor)
    return pygame.transform.scale(image, (width, height))

# Funciones de Pantallas del programa-------------------------------------------------------------------------------

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

# Base del programa-------------------------------------------------------------------------------------------------

game = True

while game:

    count += 1

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            game = False
# Controles---------------------------------------------------------------------------------------------------------
        
        elif evento.type == pygame.KEYDOWN and game_state == "setting mode":

            if evento.key == pygame.K_ESCAPE:

                game = False

            if evento.key == pygame.K_UP:

                if evento.key == pygame.K_UP:
                    
                    pos_ball[1]  -= 28
                    pos_arrow[1] -= 28
                    height       = int((display_b - pos_arrow[1]) * 0.5 - 40)
                    height2      = int(height * 0.1)
                    text_height  = font.render("Height: " + (str(height2)) + "m", True, t_color)

            if evento.key == pygame.K_DOWN:

                pos_ball[1]      += 28
                pos_arrow[1]     += 28
                height           = int((display_b - pos_arrow[1]) * -0.5 + 40)
                height2          = int(height * -0.1)
                text_height = font.render("Height: " + (str(height2)) + "m", True, t_color)
            
            if evento.key == pygame.K_w:

                if mass_object <= 60:
                    
                    scale_factor += 0.1
                    scale_factor = min(scale_factor, max_factor)
                    mass_object  += mass_plus
                    text_mass    = font.render("Total Mass: " + str(mass_object) + "Kg", True, t_color)

            if evento.key == pygame.K_s:
                
                if mass_object >= 2:
                    
                    scale_factor -= 0.1
                    scale_factor = max(scale_factor, min_factor)
                    mass_object  -= mass_plus
                    text_mass    = font.render("Total Mass: " + str(mass_object) + "Kg", True, t_color)

            if evento.key == pygame.K_SPACE:
                
                p_energy    = int(mass_object * 9.8 * height2)
                text_energy = font2.render("Total energy: " + str(p_energy) + "JOULES", True, t_color)
                game_state  = "play mode"
                print(game_state)

# Gravedad y limite de caida----------------------------------------------------------------------------------------
    
    if game_state == "play mode":

        t += 1 / 60
        object_vel += gravity(mass_object, scale_factor)
        pos_ball[1] += object_vel

        if count % 60 == 0:

            timer += 1

        if pos_ball[1] >= display_b - 32:

            game_state = "game over"

# Color de ventana--------------------------------------------------------------------------------------------------

    display.fill((62, 146, 221))  

# Escalar sprite con factor actual----------------------------------------------------------------------------------
    
    imagen_escala = image_edit(img_object, scale_factor)
    
# Posicion de los sprites-------------------------------------------------------------------------------------------
    
    display.blit(img_clouds, pos_clds)
    display.blit(img_building, pos_build)
    display.blit(img_bckgrnd, pos_bckgrnd)
    display.blit(imagen_escala, pos_ball)
    display.blit(img_arrow, pos_arrow)
    display.blit(img_frame, pos_frame)
    display.blit(text_mass, (pos_text[0], pos_text[1]))
    display.blit(text_height, (pos_text[0], pos_text[1] + 30))
    display.blit(text_energy, (pos_text[0] - 30, pos_text[1] + 60))
    
#Actualizacion de pantalla y velocidad de fotogramas----------------------------------------------------------------

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()     
