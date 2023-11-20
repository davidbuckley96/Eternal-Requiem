import pygame


class Button:
    def __init__(self, x, y, imagem, escala):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagem = pygame.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.midbottom = (x, y)
        self.clicked = False
        self.sound = pygame.mixer.Sound("soundtrack/button_click_2.0.mp3")

    def draw(self, surface):
        action = False
        # posição do cursor
        posicao_cursor = pygame.mouse.get_pos()

        # conferir se o mouse está em cima do botão
        if self.rect.collidepoint(posicao_cursor):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:  # o botão esquerdo do mouse é o [0], o do meio é [1] e o direito é [2]
                self.clicked = True
                self.sound.set_volume(0.04)
                self.sound.play()
                action = True

            elif pygame.mouse.get_pressed()[0] == 0:  # o botão esquerdo deixou de ser pressionado
                self.clicked = False

        # desenha o botão na tela
        surface.blit(self.imagem, (self.rect.x, self.rect.y))

        return action


class TextButton:
    def __init__(self, surface, color, text_color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.retangulo = pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)
        self.mouseover = False

    def draw(self, surface, outline=None):
        # Call this method to draw the button
        if outline:
            self.retangulo = pygame.draw.rect(surface, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        if self.text != '':
            font = pygame.font.Font("fontes/PixelifySans-VariableFont_wght.ttf", 25)
            text = font.render(self.text, True, self.text_color)
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self):
        mouse_position = pygame.mouse.get_pos()
        clicked = False
        # pos is the mouse position or a xy tuple coordinate
        if self.retangulo.collidepoint(mouse_position):
            self.mouseover = True
            self.text_color = 'green'
            if pygame.MOUSEBUTTONDOWN:
                clicked = True
        return clicked


class TextButton2:
    def __init__(self, text, width, height, pos, bg_color, text_color):
        # core attributes
        self.clicked = False
        self.sound = pygame.mixer.Sound("soundtrack/text_button.mp3")

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = bg_color

        # text
        font = pygame.font.Font("fontes/morris-roman.black.ttf", 25)
        self.text_surface = font.render(text, False, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.top_rect.center)
        self.bg_color = bg_color

    # def draw(self, surface):
    #     pygame.draw.rect(surface, self.top_color, self.top_rect, border_radius=12)
    #     surface.blit(self.text_surface, self.text_rect)

    def draw(self, surface):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(surface, self.top_color, self.top_rect, border_radius=12)
        # if self.top_rect.collidepoint(mouse_pos):
        #     if pygame.mouse.get_pressed()[0]:
        #         self.clicked = True
        #     else:
        #         if self.clicked is True:
        #             action = True
        #             self.clicked = False
        #     return action
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (154, 154, 154)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                self.sound.set_volume(0.08)
                self.sound.play()
                action = True

            elif pygame.mouse.get_pressed()[0] == 0:  # o botão esquerdo deixou de ser pressionado
                self.clicked = False
        else:
            self.top_color = self.bg_color
        surface.blit(self.text_surface, self.text_rect)
        return action




