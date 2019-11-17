"""Define as fases do jogo"""
import pygame
import time
import keyboard
import information

class Scene():
    """Classe que define e cria métodos para a tela do jogo"""

    def __init__(self, game_display, alvo, numjog, teclas=None):
        self.game_display = game_display
        if teclas is None:
            self.teclas = ['+', '/', '*', '-', '7', '4', '1', '.',
                           '8', '5', '2', '0', '9', '6', '3', '=','(',')']
        else:
            self.teclas = teclas
        self.calculator = keyboard.Keyboard(self.game_display, self.teclas)
        self.alvo = alvo
        self.font = pygame.font.SysFont('helvetica', 50)
        self.font2 = pygame.font.SysFont('helvetica', 31)
        self.numjog = numjog
        self.numjogi= numjog
        self.display_text = []
        self.result_text = False
        self.correto = self.font2.render("Correto",True,(0,0,0))
        self.incorreto = self.font2.render("Incorreto",True,(0,0,0))
        self.perdeu = self.font2.render("Perdeu",True,(0,0,0))

    def build_scene(self):
        "Desenha a fase"
        self.calculator.draw_keyboard()
        alvo =self.font2.render(str('Alvo = '+str(self.alvo)),True,(255,255,255))
        self.game_display.blit(alvo,(10,430))
        self.numjogp = self.font2.render(str(self.numjog), True, (0, 0, 0))
        self.game_display.blit(self.numjogp, self.calculator.rectangle_numjog)

    def handle_events(self, event):
        """Cuida dos eventos da fase"""
        button_pressed = self.calculator.use_keyboard(event)
        if button_pressed is not None:
            if button_pressed == 'C':
                print(self.display_text)
                self.display_text.clear()
                self.numjog = self.numjogi
            elif button_pressed == '=':
                # Avalia valor
                valor = self.evaluate()
                self.display_text.clear()
                if valor == self.alvo:
                    self.result_text = True
                    self.game_display.blit(self.correto,self.calculator.rectangle_resp)
                    pygame.display.flip()
                    time.sleep(1)
                    return 1
                else:
                    self.result_text = False
                    self.game_display.blit(self.incorreto, self.calculator.rectangle_resp)
                    pygame.display.flip()
                    time.sleep(1)
                    return 0
            else:
                self.display_text.append(button_pressed)
                self.numjog -= 1
                self.numjogp = self.font2.render(str(self.numjog), True, (0, 0, 0))
                self.game_display.blit(self.numjogp, self.calculator.rectangle_numjog)
                pygame.display.flip()
                if self.numjog <= 0:
                    print(self.numjog)
                    self.display_text.clear()
                    self.game_display.blit(self.perdeu, self.calculator.rectangle_resp)
                    pygame.display.flip()
                    time.sleep(0.55)
                    self.numjog = self.numjogi
                    return 0
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

