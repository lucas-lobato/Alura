import pygame

AMARELO = (255,255,0)
PRETO = (0,0,0)
VELOCIDADE = 1
RAIO = 10
pygame.init()

tela = pygame.display.set_mode((640,480),0)

x = 10
y = 10

vel_x = VELOCIDADE
vel_y = VELOCIDADE

while True:
    #calcula as regras
    x += vel_x
    y += vel_y

    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE
    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE

    #pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (x,y), RAIO, 0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()