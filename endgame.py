import pygame
import sys
import pygbutton
import time
import GIFImage

class GameWin(object):
    def __init__(self,gamedisplay, music):
        self.font = pygame.font.SysFont('helvetica', 35)
        self.music = music
        self.gamedisplay = gamedisplay
        self.winnerAnimation = GIFImage.GIFImage('win.gif')
    def gamewin(self):
        self.gamedisplay.fill((183, 232, 255))
        for i in range(15):
            self.winnerAnimation.play()
            self.winnerAnimation.render(self.gamedisplay, (0,0))
            time.sleep(0.1)
            pygame.display.flip()
        pygame.mixer.music.play()
        pygame.display.flip()

    def gameover(self):
        self.gamedisplay.fill((255,0,0))
        you_lose = self.font.render("You Lose",True,(255,255,255))
        self.gamedisplay.blit(you_lose,(150,80))
        pygame.display.flip()