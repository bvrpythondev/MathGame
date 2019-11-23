"""Classe principal"""
import pygame
import pygbutton
import scene
import time
import endgame

# x,y(410,0,width=500,height=190)


def main():
    """Main loop"""
    # Inicia bibliotecas necessárias para o pygame
    pygame.init()
    # Cria uma tela de tamanho 800x600
    game_display = pygame.display.set_mode((600, 500))
    # Preenche o fundo da tela com a cor branca
    game_display.fill(pygbutton.WHITE)
    backgroundimage = pygame.image.load('mat5.jpg')
    backgroundimage = pygame.transform.scale(backgroundimage,(600, 500))
    # Define o nome da janela
    pygame.display.set_caption("Math Game")
    cena1 = scene.Scene(game_display, 10, 3,['1', '9', '+','(',')'])
    cena2 = scene.Scene(game_display, 100, 4,['1', '0', '5', '2', 'x', '+'])
    cena3 = scene.Scene(game_display, 40, 4,['2', 'x', '0'])
    cenas = []
    cenas.append(cena1)
    cenas.append(cena2)
    cenas.append(cena3)
    gamewin = endgame.GameWin(game_display)
    # loop principal do game
    fase = 0
    proxima_fase = 0
    while True:
        # percorre os eventos (clique do mouse, tecla pressionada, movimentar o mouse, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                proxima_fase += cenas[fase].handle_events(event)




        if proxima_fase > fase:
            fase = proxima_fase

        # Preenche a tela de branco
        try:
            game_display.fill(pygbutton.WHITE)
            game_display.blit(backgroundimage,[0,0])
            cenas[fase].build_scene()
            cenas[fase].write_calculator()
        except:
            gamewin.gamewin()
        # Atualiza a tela
        pygame.display.flip()
main()
