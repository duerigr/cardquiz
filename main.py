import pygame
from pygame.locals import *
from data.parser import Parser
from ui.card import Card


class Config:
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    blue = 0, 0, 255
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


class Main:

    @classmethod
    def init(cls):
        cls.parser = Parser()
        cls.parser.parse("questions.json")
        pygame.init()
        cls.screen = pygame.display.set_mode((Config.display_width, Config.display_height))
        cls.screen.fill(Config.blue)

        # display cards
        cls.font = pygame.font.Font("res/MechanicalBold-oOmA.otf", 12)
        # text_surface = cls.font.render("Lorem ipsum und so weiter und so fort...", True, Config.white)
        # text_rect = Rect(10, 10, 200, 200)
        # cls.screen.blit(text_surface, text_rect)
        # pygame.draw.rect(cls.screen, Config.white, text_rect, 3)
        pools = cls.parser.get_pools()
        cls.cards = cls.__draw_cards(pools, 0)
        pygame.display.update()

    @classmethod
    def __draw_cards(cls, pools, pool_id):
        questions = pools[pool_id].get_random_questions(9)

        cards = {}
        for i in range(0, len(questions)):
            cards[i] = Card(questions[i].get_question(),
                            questions[i].get_answer(),
                            Rect(Config.top_left_points[i], (Config.card_rect_width, Config.card_rect_height)),
                            cls.__render_text(questions[i].get_question(), Config.center_points[i]))

        for card in cards.values():
            pygame.draw.rect(cls.screen, Config.white, card.get_rectangle_dimensions(), 1)

        return cards

    @classmethod
    def __render_text(cls, text, center):
        text_surface = cls.font.render(text, True, Config.white)
        text_rect = text_surface.get_rect()
        text_rect.center = (center[0], center[1])
        cls.screen.blit(text_surface, text_rect)
        return text_surface

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
                            print("clicked card: "+card.get_question())
                            cls.screen.fill(Config.blue, card.get_rectangle_dimensions())
                            pygame.draw.rect(cls.screen, Config.white, card.get_rectangle_dimensions(), 1)
                            cls.__render_text(card.flip(), card.get_rectangle_dimensions().center)
                            pygame.display.update(card.get_rectangle_dimensions())

            #pygame.display.update()


Main.init()
Main.main()

pygame.quit()
quit()
