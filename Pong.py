import pygame
import random

def main():
    pygame.init()
    tela = pygame.display.set_mode([1000, 650]) #Tamanho da tela
    pygame.display.set_caption("Pong") #Nome do jogo na janela
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    taco = pygame.Rect((20, 310), (10, 60))
    bola = pygame.Rect((500,325),(10, 10))
    taco2 = pygame.Rect((970, 310), (10, 60))
    timerx = 2 #Velocidade no eixo x
    timery = 0 #Velocidade no eixo y
    velocidade = [timerx, timery]
    sair = False
    contador = 0
    scoreA = 0
    scoreB = 0

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        relogio.tick(60) #Frames por segundo
        tela.fill((0, 0, 0)) #Atualização de tela
        (taco2.top, taco2.top) = pygame.mouse.get_pos() #Controle do taco2 pelo mouse

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                taco.move_ip(0, 10)

            if event.key == pygame.K_UP:
                taco.move_ip(0, -10)

        bola = bola.move(velocidade) #Movimento da bola

        if bola.colliderect(taco2): #Colisão com taco2
            velocidade[0] = -velocidade[0]
            timery = random.randint(-8,8)
            velocidade[1] = timery

        if bola.colliderect(taco):
            timery = random.randint(-8,8)
            timerx = random.randint(3,6)
            velocidade[0] = timerx
            velocidade[1] = timery

        if bola.left < 0:
            bola = pygame.Rect((500,325),(10, 10))
            scoreB += 1
        if bola.left >= 1000:
            bola = pygame.Rect((500,325),(10, 10))
            scoreA += 1
        if bola.top < 0:
            velocidade[1] = -velocidade[1]
        if bola.top >= 640:
            velocidade[1] = -velocidade[1]

        font = pygame.font.Font(None, 120)
        text = font.render(str(scoreA), 1, cor_branca)
        tela.blit(text, (300,20))
        text = font.render(str(scoreB), 1, cor_branca)
        tela.blit(text, (690,20))

        pygame.draw.rect(tela, cor_branca, taco)
        pygame.draw.rect(tela, cor_branca, taco2)
        pygame.draw.rect(tela, cor_branca, bola)

        pygame.display.update()

    pygame.quit()

main()