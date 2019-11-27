import pygame
import sys
import pygbutton
import time

class GameWin(object):
    def __init__(self,gamedisplay, music):
        self.font = pygame.font.SysFont('helvetica', 35)
        self.music = music
        self.gamedisplay = gamedisplay

    def gamewin(self):
        self.gamedisplay.fill((0, 200, 0))
        winner_image = pygame.image.load('winner.png')
        winner_image = pygame.transform.scale(winner_image,(300,300))
        self.gamedisplay.blit(winner_image,(150,80))
        pygame.mixer.music.play()
        pygame.display.flip()

    def gameover(self):
        self.gamedisplay.fill((255,0,0))
        you_lose = self.font.render("You Lose",True,(255,255,255))
        self.gamedisplay.blit(you_lose,(150,80))
        pygame.display.flip()