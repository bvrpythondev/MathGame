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
    backgroundimage = pygame.image.load('mat5 - copia.jpg')
    music_win = pygame.mixer.music.load('gamewining.mp3')
    # backgroundimage = pygame.transform.scale(backgroundimage,(600, 500))
    # Define o nome da janela
    pygame.display.set_caption("Math Game")
    cena1 = scene.Scene(game_display, 15, 7,['2', '3', '4','+','x'])#Solução = 2 * 4 +4 +3
    cena2 = scene.Scene(game_display, 26, 9,['2', '5', '4','+','x','(',')'])
    cena3 = scene.Scene(game_display, 59, 9,['2', '4', '6', '7', 'x', '+','/'])
    cena4 = scene.Scene(game_display, 156, 6,['7', '8','6','3','x','/'])
    cena5 = scene.Scene(game_display, 61, 15,["(", ")", "1", "2", "4", "5", "6", "9",".","+", "x", "/"])
    cena6 = scene.Scene(game_display, 63, 12,['1', '2','5','3','x','-','/','+','x','(',')'])
    cenas = []
    cenas.append(cena1)
    # cenas.append(cena2)
    # cenas.append(cena3)
    # cenas.append(cena4)
    # cenas.append(cena5)
    # cenas.append(cena6)
    gamewin = endgame.GameWin(game_display, music_win)
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
            game_display.blit(backgroundimage, [0,0])
            cenas[fase].build_scene()
            cenas[fase].write_calculator()
        except:
            gamewin.gamewin()
            time.sleep(5)
            fase = 0
            proxima_fase = 0
            
        # Atualiza a tela
        pygame.display.flip()
main()
