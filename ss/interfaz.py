import pygame
import sys

#Constantes

display_a = 1290
display_b = 720
c_rojo = (255, 0, 0)
c_gris = (100, 100, 100)

d = [0,0]


# Dimensiones del edificio en metros

pos_edif = [0, 120]
edificio_metrosa = 50
edificio_metrosb = 70


#Dimensiones bola

pos_bola = [550, 100]
masa_a = 10
masa_b = 10
marcador = [550,680]

# Conversión de metros a píxeles (asumiendo una relación de 1 metro = 10 píxeles)
ancho_edificio = int(edificio_metrosa * 10)
alto_edificio = int(edificio_metrosb * 10)

# Posición y velocidad inicial del objeto
#velocidad_objeto = 0
#masa_objeto = 1

#Constante de la gravedad y factor de velocidad
t = 0
def velocidad(t):
    gravedad = 9.8 / 6 
    f_clibre = 1/2 * gravedad * t
    return(f_clibre)
# Inicializar Pygame



display = pygame.display.set_mode((display_a, display_b))
clock = pygame.time.Clock()
#font = pygame.font.Font(None, 28)
game_state = "setting mode"
count = 0
timer = 0




#Sprites

img_edificio = pygame.image.load("sdfasdf.png")
img_fondo = pygame.image.load("Sprite-0010.png")
img_objeto = pygame.image.load("Sprite-0002.png")

pygame.transform.scale(img_edificio, [edificio_metrosa, edificio_metrosb])


        
game = True
while game:
    count += 1
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
        if evento.type == pygame.KEYDOWN and game_state == "setting mode":
            if evento.key == pygame.K_UP:
                pos_edif[1] -= 10 
                alto_edificio += 10
                pos_bola[1] -= 10
            if evento.key == pygame.K_DOWN:
                pos_edif[1] += 10
                alto_edificio -= 10
                pos_bola[1] += 10
            if evento.key == pygame.K_SPACE:
                game_state = "play mode"
                print(game_state)
    if game_state == "play mode":
        t += 1 / 60
        pos_bola[1] += velocidad(t)
        if count % 60 == 0:
            timer += 1 
        if pos_bola[1] >= display_b - 32:
            game_state = "game over"
    if game_state == "game over":
        pos_bola[1] = display_b - 32
        print(game_state)

        
            


            
    display.fill((255, 255, 255))  



    #Texts

    #count_text = font.render(f"Timer: {timer} s", True, (0, 0, 0))
    #display.blit(count_text, (20, 20))

    # Dibujar el edificio y objeto

    #draw = pygame.init() ; sp = sprites_load()

    display.blit(img_fondo, d)
    display.blit(img_edificio, pos_edif)
    display.blit(img_objeto, pos_bola)
    pygame.display.flip()
    #ygame.draw.rect(display, c_gris, (pos_edif[0], pos_edif[1], ancho_edificio, alto_edificio))
    #pygame.draw.rect(display, c_rojo, (pos_bola[0], pos_bola[1], masa_a, masa_b))
   
    
    clock.tick(60)

pygame.quit()
sys.exit()     
