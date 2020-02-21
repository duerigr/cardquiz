import pygame
from pygame.locals import *
from ui.config import Config


class Carddisplay(pygame.sprite.Sprite):

    def __init__(self, cardboardhandler, screensize):
        super(Carddisplay, self).__init__()
        self.surf = pygame.Surface((screensize[0] // 2, screensize[1] // 2))
        self.rect = self.surf.get_rect()
        self.rect.center = (screensize[0] // 2, screensize[1] // 2)
        self.rect_close = Rect(self.rect.x + self.rect.width - 22, self.rect.y + 2, 20, 20)
        self.rect_correct = Rect(self.rect.x + 2, self.rect.y + self.rect.height - 32, 30, 30)
        self.rect_wrong = Rect(self.rect.x + self.rect.width - 32, self.rect.y + self.rect.height - 32, 30, 30)
        self.rect_flip = Rect(self.rect.x + 2, self.rect.y + 2, 30, 30)
        self.disabled = False
        self.cardboardhandler = cardboardhandler
        self.card = None
        self.screen = None

    def disable(self):
        self.disabled = True
        self.card = None
        self.screen = None
        self.kill()

    def enable(self, screen, card):
        self.disabled = False
        self.card = card
        self.screen = screen
        self.render_card()

    def render_card(self):
        if not (self.card is not None and self.screen is not None):
            return
        self.surf.fill(Config.niceblue if not self.card.is_flipped() else Config.nicegreen)
        pygame.draw.rect(self.surf, Config.white, Rect(0, 0, self.rect.width, self.rect.height), 2)
        pygame.draw.rect(self.surf, Config.red, Rect(self.rect.width - 22, 2, 20, 20))
        pygame.draw.rect(self.surf, Config.green, Rect(2, self.rect.height - 32, 30, 30))
        pygame.draw.rect(self.surf, Config.yellow, Rect(self.rect.width - 32, self.rect.height - 32, 30, 30))
        pygame.draw.rect(self.surf, Config.pink, Rect(2, 2, 30, 30))
        fontconfig = self.card.get_fontconfig()
        for texttuple in fontconfig[2]:
            self.surf.blit(texttuple[0], texttuple[1])
        self.screen.blit(self.surf, self.rect)
        pygame.display.update(self.rect)

    def mainloop(self, events):
        if self.disabled:
            return
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.rect_close.collidepoint(mouse_x, mouse_y):
                    self.handle_close_click()
                elif self.rect_correct.collidepoint(mouse_x, mouse_y):
                    self.handle_correct_click()
                elif self.rect_wrong.collidepoint(mouse_x, mouse_y):
                    self.handle_wrong_click()
                elif self.rect_flip.collidepoint(mouse_x, mouse_y):
                    self.handle_flip_click()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.cardboardhandler()

    def handle_flip_click(self):
        if self.card is not None:
            self.card.flip()
            self.render_card()

    def handle_close_click(self):
        self.cardboardhandler()

    def handle_correct_click(self):
        if self.card is not None:
            self.card.set_solved(True)
        self.cardboardhandler()

    def handle_wrong_click(self):
        if self.card is not None:
            self.card.set_solved(False)
        self.cardboardhandler()
