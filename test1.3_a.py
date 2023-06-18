import pygame
import sys

# Constantes
display_a = 1290
display_b = 720
c_rojo = (255, 0, 0)
c_gris = (100, 100, 100)

# Dimensiones del edificio en metros
pos_edif = [20, 100]
edificio_metrosa = 50
edificio_metrosb = 70

# Dimensiones de la bola
pos_bola = [550, 100]
masa_bola = 10
altura_inicial = 100

# Conversión de metros a píxeles (asumiendo una relación de 1 metro = 10 píxeles)
ancho_edificio = int(edificio_metrosa * 10)
alto_edificio = int(edificio_metrosb * 10)

# Constante de la gravedad y factor de velocidad
t = 0

def calcular_energia_potencial(masa, altura):
    gravedad = 9.8
    energia_potencial = masa * gravedad * altura
    return energia_potencial

def velocidad(t):
    gravedad = 9.8 / 6
    f_clibre = 1/2 * gravedad * t
    return f_clibre

def fuerza_roce(velocidad):
    coeficiente_roce = 0.2
    fuerza_roce = coeficiente_roce * velocidad
    return fuerza_roce

# Inicializar Pygame
pygame.init()

display = pygame.display.set_mode((display_a, display_b))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
game_state = "setting mode"
count = 0
timer = 0
suelo = display_b - 10  # Posición del suelo

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
                altura_inicial -= 10
            if evento.key == pygame.K_DOWN:
                pos_edif[1] += 10
                alto_edificio -= 10
                pos_bola[1] += 10
                altura_inicial += 10
            if evento.key == pygame.K_SPACE:
                game_state = "play mode"
                print(game_state)

    if game_state == "play mode":
        t += 1 / 60
        velocidad_bola = velocidad(t)
        fuerza_roce_bola = fuerza_roce(velocidad_bola)
        gravedad = 9.8
        aceleracion_bola = gravedad - fuerza_roce_bola

        if pos_bola[1] + masa_bola < suelo:
            pos_bola[1] += velocidad_bola
        else:
            pos_bola[1] = suelo - masa_bola
            t = 0  # Detener el tiempo cuando la bola toca el suelo

        if count % 60 == 0:
            timer += 1

    display.fill((255, 255, 255))

    # Textos
    count_text = font.render(f"Tiempo: {timer} s", True, (0, 0, 0))
    energia_pot_text = font.render(f"Energía Potencial: {calcular_energia_potencial(masa_bola, altura_inicial)} J", True, (0, 0, 0))
    display.blit(count_text, (20, 20))
    display.blit(energia_pot_text, (20, 50))

    # Dibujar el edificio y la bola
    pygame.draw.rect(display, c_gris, (pos_edif[0], pos_edif[1], ancho_edificio, alto_edificio))
    pygame.draw.rect(display, c_rojo, (pos_bola[0], pos_bola[1], masa_bola, masa_bola))

    # Dibujar el suelo
    pygame.draw.line(display, (0, 0, 0), (0, suelo), (display_a, suelo))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
