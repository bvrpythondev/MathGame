"""Define o teclado do jogo"""
import pygame
import pygbutton

# Define tamanhos dos botões
WIDTH_BUTTONS = 100
HEIGHT_BUTTON_NUM = 50

# Define espaçamento dos botões
GRID_WIDTH_MIN = 40
GRID_WIDTH_SPACE = 10
GRID_WIDTH_INTERVAL = WIDTH_BUTTONS + GRID_WIDTH_SPACE
GRID_HEIGHT_MIN = 160
GRID_HEIGHT_SPACE = 10
GRID_HEIGHT_INTERVAL = HEIGHT_BUTTON_NUM + GRID_HEIGHT_SPACE

GRID_WIDTH_BUTTON_C = GRID_WIDTH_MIN + 4*GRID_WIDTH_INTERVAL
HEIGHT_BUTTON_C = HEIGHT_BUTTON_NUM + GRID_HEIGHT_INTERVAL * 3


class Keyboard():
    ''' Classe responsável por desenhar e prover métodos de acesso
        ao teclado da calculadora.'''
    def __init__(self, gamedisplay, list_active_buttons=None):
        if list_active_buttons is None:
            self.list_active_buttons = ['+', '/', '*', '-', '7', '4', '1', '.',
                                        '8', '5', '2', '0', '9', '6', '3', '=']
        else:
            self.list_active_buttons = list_active_buttons
    
        self.buttons = self._create_buttons()
        self.calculator_display_rect = pygame.Rect(0, 0, 600, 150)
        self.calculator_display_color = (0, 0, 0)
        self.gamedisplay = gamedisplay
    def _create_buttons(self):
        '''Cria os botões do teclado e define se eles aparecem ou não
           de acordo com os valores passados em list_active_buttons'''

        keyboard_buttons = []
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN,
                                                     GRID_HEIGHT_MIN,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    "+"))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN,
                                                     GRID_HEIGHT_MIN + GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    "/"))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN,
                                                     GRID_HEIGHT_MIN + 2 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    "*"))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN,
                                                     GRID_HEIGHT_MIN + 3 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    "-"))

        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '7'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN+GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '4'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN + 2 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '1'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN + 3 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '.'))

        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 2 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '8'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 2 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN + GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '5'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 2 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN + 2 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '2'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 2 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN + 3 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '0'))

        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 3 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '9'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 3 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN+GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '6'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 3 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN+2 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '3'))
        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_MIN + 3 * GRID_WIDTH_INTERVAL,
                                                     GRID_HEIGHT_MIN + 3 * GRID_HEIGHT_INTERVAL,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_NUM),
                                                    '='))

        keyboard_buttons.append(pygbutton.PygButton((GRID_WIDTH_BUTTON_C,
                                                     GRID_HEIGHT_MIN,
                                                     WIDTH_BUTTONS,
                                                     HEIGHT_BUTTON_C),
                                                    'C'))

        for button in keyboard_buttons:
            if button.caption in self.list_active_buttons or button.caption in ['C', '=']:
                button.visible = True
            else:
                button.visible = False

        return keyboard_buttons

    def draw_keyboard(self):
        """Método responsável por desenhar o teclado do jogo."""
        pygame.draw.rect(self.gamedisplay,
                         self.calculator_display_color,
                         self.calculator_display_rect)
        for button in self.buttons:
            button.draw(self.gamedisplay)

    def use_keyboard(self, event):
        """Checa se algum botão foi pressionado"""
        for button in self.buttons:
            if 'click' in button.handle_event(event):
                return button.caption
        return None
