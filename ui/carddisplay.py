import pygame
from pygame.locals import *
from ui.config import Config
from ui.card import Card


class Carddisplay(pygame.sprite.Sprite):

    def __init__(self, cardboardhandler, screensize):
        super(Carddisplay, self).__init__()
        self.surf = pygame.Surface((screensize[0] // 2, screensize[1] // 2))
        self.rect = self.surf.get_rect()
        self.rect.center = (screensize[0] // 2, screensize[1] // 2)
        self.disabled = False
        self.cardboardhandler = cardboardhandler

    def disable(self):
        self.disabled = True
        self.kill()

    def enable(self, screen, card):
        self.disabled = False
        self.render_card(card)
        screen.blit(self.surf, self.rect)
        pygame.display.update(self.rect)

    def render_card(self, card: Card):
        self.surf.fill(Config.niceblue if not card.is_flipped() else Config.nicegreen)
        pygame.draw.rect(self.surf, Config.white, Rect(0, 0, self.rect.width, self.rect.height), 2)
        fontconfig = card.get_fontconfig()
        for texttuple in fontconfig[2]:
            self.surf.blit(texttuple[0], texttuple[1])

    def mainloop(self, events):
        if self.disabled:
            return
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.handle_inner_click()
                else:
                    self.handle_outer_click()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.cardboardhandler()

    def handle_inner_click(self):
        # TODO handle right / wrong
        pass

    def handle_outer_click(self):
        self.cardboardhandler()
