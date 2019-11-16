import pygame
import sys
import pygbutton

class Information(object):
    def __init__(self,gamedisplay,alvo,teclas=None):
        if teclas is None:
            self.teclas = ['+', '/', '*', '-', '7', '4', '1', '.',
                           '8', '5', '2', '0', '9', '6', '3', '=','(',')']
        else:
            self.teclas = teclas
        self.alvo = alvo
        self.font = pygame.font.SysFont('helvetica', 35)
        self.gamedisplay = gamedisplay
    def write_result(self,result_text):
        if result_text == True:
            correto = self.font.render(str("Correto"),True,(255,255,255))
            self.gamedisplay.blit(correto,(40,430))
        else:
            print("Result = False")
