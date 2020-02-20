import pygame
from pygame.locals import *

from ui.config import Config
from ui.card import Card


class Cardboard:

    def __init__(self, handler, pools, font, fontconfig, screensize):
        self.disabled = False
        self.handler = handler
        self.cards = {}
        self.pools = pools
        self.font = font
        self.__init_cards(fontconfig, screensize)

    def render_all(self, screen):
        screen.fill(Config.lightgray)
        self.__render_pool_headings(screen)
        for card in self.cards.values():
            if card.is_solved() is None:
                pygame.draw.rect(screen, card.get_color(), card.get_rectangle_dimensions())
            elif card.is_solved() is True:
                pygame.draw.rect(screen, Config.gray, card.get_rectangle_dimensions())
                pygame.draw.rect(screen, Config.green, card.get_rectangle_dimensions(), 2)
            else:
                pygame.draw.rect(screen, Config.gray, card.get_rectangle_dimensions())
                pygame.draw.rect(screen, Config.red, card.get_rectangle_dimensions(), 2)

        pygame.display.flip()

    def disable(self, screen):
        self.disabled = True
        screen.fill(Config.niceblue)

    def enable(self, screen):
        self.disabled = False
        self.render_all(screen)

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

    def __render_pool_headings(self, screen):
        screen_width = screen.get_width()
        width_step = screen_width // 21
        screen_height = screen.get_height()
        height_step = screen_height // 14
        top_x = 2 * width_step
        top_y = height_step
        for p in self.pools:
            text_surface = self.font.render(str(p.get_points()), True, Config.font_setting[1])
            text_rect = text_surface.get_rect()
            text_rect.topleft = (top_x, top_y)
            screen.blit(text_surface, text_rect)
            top_x += 4 * width_step

    def __handle_click(self, mouse_x, mouse_y, screen):
        for card in self.cards.values():
            if card.point_in_card_dimensions(mouse_x, mouse_y):
                card.flip()
                self.__render_card(card, screen)
                pygame.display.update(card.get_rectangle_dimensions())

    def __init_cards(self, fontconfig, screensize):
        screen_width = screensize[0]
        width_step = screen_width // 21
        screen_height = screensize[1]
        height_step = screen_height // 14
        pools = sorted(self.pools, key=lambda e: e.get_points())

        top_x = 2 * width_step
        for p in pools:
            top_y = height_step
            questions = p.get_random_questions(5)
            for i in range(0, len(questions)):
                top_y += 2 * height_step
                rectangle = Rect((top_x, top_y), (width_step, height_step))
                self.cards[(p.get_points(), i)] = Card(questions[i].get_question(),
                                                       questions[i].get_answer(),
                                                       rectangle,
                                                       fontconfig,
                                                       Config.font_setting,
                                                       Config.row_colors[i])
            top_x += 4 * width_step
