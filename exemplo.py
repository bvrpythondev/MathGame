import pygame
import sys


def main():

    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    fonte = pygame.font.SysFont("Helvetica", 50)
    num = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    num += 1
                    text = fonte.render(str(num), True, (255, 255, 255))
                    screen.blit(text, pygame.mouse.get_pos())
                elif event.key == pygame.K_b:
                    num -= 1
                    text = fonte.render(str(num), True, (255, 255, 255))
                    # blit é responsável por "colar" o que queremos na nossa superfície(screen)
                    # O texto não pode ser feito diretamente na nossa tela. Primeiro é feita uma
                    # nova superfície com o render e só depois colamos essa superfície na nossa
                    # superfície original
                    screen.blit(text, pygame.mouse.get_pos())
                elif event.key == pygame.K_SPACE:
                    # fill seria o que faz com que a tela faça um reset. Se fizermos isso o tempo 1todo
                    # e sempre atualizarmos nossos desenhos eles vão parecer que estão se movimentando
                    screen.fill((0, 0, 0))
                    num = 0
                elif event.key == pygame.K_p:
                    quad = pygame.Rect(10, 10, 10, 10)
                    for passo in range(10, 500):
                        pygame.draw.rect(screen, (255, 0, 0), quad) # Desenha direto na superfície
                        quad = quad.move((1, 0))

                        pygame.display.flip()
                        pygame.time.wait(10)
                        screen.fill((0, 0, 0))# Comente essa linha e verá que os quadrados antigos
                        # não serão retirados


        pygame.display.flip()
main()
