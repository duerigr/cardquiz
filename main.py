import pygame
from pygame.locals import *
from data.parser import Parser
from ui.card import Card


class Config:
    debug = False
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    nicegreen = 4, 117, 19
    blue = 0, 0, 255
    niceblue = 5, 36, 150
    display_height = 768
    display_width = 1280
    card_rect_height = (display_height // 3) - 2
    card_rect_width = (display_width // 3) - 2
    center_a1 = (display_width // 6, display_height // 6)
    center_a2 = ((display_width // 6) * 3, display_height // 6)
    center_a3 = ((display_width // 6) * 5, display_height // 6)
    center_b1 = (display_width // 6, (display_height // 6) * 3)
    center_b2 = ((display_width // 6) * 3, (display_height // 6) * 3)
    center_b3 = ((display_width // 6) * 5, (display_height // 6) * 3)
    center_c1 = (display_width // 6, (display_height // 6) * 5)
    center_c2 = ((display_width // 6) * 3, (display_height // 6) * 5)
    center_c3 = ((display_width // 6) * 5, (display_height // 6) * 5)
    center_points = (
        center_a1, center_a2, center_a3,
        center_b1, center_b2, center_b3,
        center_c1, center_c2, center_c3
    )
    top_left_a1 = (1, 1)
    top_left_a2 = (card_rect_width + 3, 1)
    top_left_a3 = ((card_rect_width * 2) + 5, 1)
    top_left_b1 = (1, card_rect_height + 3)
    top_left_b2 = (card_rect_width + 3, card_rect_height + 3)
    top_left_b3 = ((card_rect_width * 2) + 5, card_rect_height + 3)
    top_left_c1 = (1, (card_rect_height * 2) + 5)
    top_left_c2 = (card_rect_width + 3, (card_rect_height * 2) + 5)
    top_left_c3 = ((card_rect_width * 2) + 5, (card_rect_height * 2) + 5)
    top_left_points = (
        top_left_a1, top_left_a2, top_left_a3,
        top_left_b1, top_left_b2, top_left_b3,
        top_left_c1, top_left_c2, top_left_c3
    )
    font_vars = {
        "small": (18, 37),
        "medium": (26, 25),
        "large": (32, 22)
    }
    font_setting = ("res/MechanicalBold-oOmA.otf", white)


class Main:

    @classmethod
    def init(cls):
        # set font config
        cls.fontconfig = Config.font_vars["large"]

        cls.parser = Parser()
        cls.parser.parse("questions.json")
        pygame.init()
        cls.screen = pygame.display.set_mode((Config.display_width, Config.display_height))
        cls.screen.fill(Config.niceblue)

        # display cards
        cls.font = pygame.font.Font(Config.font_setting[0], cls.fontconfig[0])
        pools = cls.parser.get_pools()
        # TODO select pool
        cls.cards = cls.__draw_cards(pools, 0)
        pygame.display.update()

    @classmethod
    def __draw_cards(cls, pools, pool_id):
        questions = pools[pool_id].get_random_questions(9)

        cards = {}
        for i in range(0, len(questions)):
            rect = Rect(Config.top_left_points[i], (Config.card_rect_width, Config.card_rect_height))
            cards[i] = Card(questions[i].get_question(),
                            questions[i].get_answer(),
                            rect,
                            cls.fontconfig,
                            Config.font_setting)

        for card in cards.values():
            cls.__render_card(card)

        return cards

    @classmethod
    def __render_card(cls, card: Card):
        cls.screen.fill(Config.niceblue if not card.is_flipped() else Config.nicegreen,
                        card.get_rectangle_dimensions())
        pygame.draw.rect(cls.screen, Config.white, card.get_rectangle_dimensions(), 1)
        fontconfig = card.get_fontconfig()
        for texttuple in fontconfig[2]:
            cls.screen.blit(texttuple[0], texttuple[1])

    @classmethod
    def main(cls):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for card in cls.cards.values():
                        if card.point_in_card_dimensions(mouse_x, mouse_y):
                            cls.log("clicked card: "+card.get_question())
                            card.flip()
                            cls.__render_card(card)
                            pygame.display.update(card.get_rectangle_dimensions())

    @classmethod
    def log(cls, msg):
        if Config.debug:
            print(msg)


Main.init()
Main.main()

pygame.quit()
quit()
