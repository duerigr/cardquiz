import pygame
from pygame.locals import *

from ui.config import Config
from ui.card import Card


class Cardboard:

    def __init__(self, handler):
        self.disabled = False
        self.handler = handler
        self.cards = {}

    def render_all(self, screen, pool, fontconfig):
        questions = pool.get_random_questions(9)

        cards = {}
        for i in range(0, len(questions)):
            rectangle = Rect(Config.top_left_points[i], (Config.card_rect_width, Config.card_rect_height))
            cards[i] = Card(questions[i].get_question(),
                            questions[i].get_answer(),
                            rectangle,
                            fontconfig,
                            Config.font_setting)
        self.cards = cards
        screen.fill(Config.niceblue)
        for card in self.cards.values():
            self.__render_card(card, screen)
        pygame.display.flip()

    def disable(self, screen):
        self.disabled = True
        screen.fill(Config.niceblue)

    def enable(self, screen, pool, fontconfig):
        self.disabled = False
        self.render_all(screen, pool, fontconfig)

    def mainloop(self, events, screen):
        if self.disabled:
            return
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.__handle_click(mouse_x, mouse_y, screen)
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.handler()

    def __render_card(self, card: Card, screen):
        screen.fill(Config.niceblue if not card.is_flipped() else Config.nicegreen,
                    card.get_rectangle_dimensions())
        pygame.draw.rect(screen, Config.white, card.get_rectangle_dimensions(), 1)
        fontconfig = card.get_fontconfig()
        for texttuple in fontconfig[2]:
            screen.blit(texttuple[0], texttuple[1])

    def __handle_click(self, mouse_x, mouse_y, screen):
        for card in self.cards.values():
            if card.point_in_card_dimensions(mouse_x, mouse_y):
                card.flip()
                self.__render_card(card, screen)
                pygame.display.update(card.get_rectangle_dimensions())
