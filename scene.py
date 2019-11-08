"""Define as fases do jogo"""
import pygame
import time
import keyboard

class Scene():
    """Classe que define e cria métodos para a tela do jogo"""

    def __init__(self, game_display, alvo, teclas=None):
        self.game_display = game_display
        if teclas is None:
            self.teclas = ['+', '/', '*', '-', '7', '4', '1', '.',
                           '8', '5', '2', '0', '9', '6', '3', '=']
        else:
            self.teclas = teclas
        self.calculator = keyboard.Keyboard(self.game_display, self.teclas)
        self.alvo = alvo
        self.font = pygame.font.SysFont('helvetica', 50)
        self.display_text = []
        self.result_text = []

    def build_scene(self):
        "Desenha a fase"
        self.calculator.draw_keyboard()


    def handle_events(self, event):
        """Cuida dos eventos da fase"""
        button_pressed = self.calculator.use_keyboard(event)
        if button_pressed is not None:
            if button_pressed == 'C':
                print(self.display_text)
                self.display_text.clear()
            elif button_pressed == '=':
                # Avalia valor
                valor = self.evaluate()
                self.display_text.clear()
                if valor == self.alvo:
                    self.write_result(True)
                    return 1
                else:
                    self.write_result(False)
                    return 0
            else:
                self.display_text.append(button_pressed)
                return 0
        return 0

    def write_calculator(self):
        """Imprime números na calculadora"""
        text = self.font.render(''.join(self.display_text), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.bottomright = self.calculator.calculator_display_rect.bottomright
        self.game_display.blit(text, text_rect)

    def evaluate(self):
        """Avalia o valor da expressão na tela da calculadora"""
        try:
            value = eval(''.join(self.display_text))
        except SyntaxError:
            return
        return value

    def write_result(self,result_text):
        return result_text

    def result(self,result):
        rectWidth = 100
        rectHeight = 100
        if result == True:
            text = self.font.render('Correto', True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (rectWidth // 2, rectHeight // 2)
            self.game_display.blit(text, text_rect)
        else:
            text = self.font.render('Incorreto', True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (rectWidth // 2, rectHeight // 2)
            self.game_display.blit(text, text_rect)
