from ui.config import Config
from ui.card import Card
from pygame.draw import rect
from pygame.rect import Rect
from pygame.display import update


class Cardboard:

    def __init__(self, pool, fontconfig):
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

    def render_all(self, screen):
        for card in self.cards.values():
            self.__render_card(card, screen)
        update()

    def __render_card(self, card: Card, screen):
        screen.fill(Config.niceblue if not card.is_flipped() else Config.nicegreen,
                    card.get_rectangle_dimensions())
        rect(screen, Config.white, card.get_rectangle_dimensions(), 1)
        fontconfig = card.get_fontconfig()
        for texttuple in fontconfig[2]:
            screen.blit(texttuple[0], texttuple[1])

    def handle_click(self, mouse_x, mouse_y, screen):
        for card in self.cards.values():
            if card.point_in_card_dimensions(mouse_x, mouse_y):
                card.flip()
                self.__render_card(card, screen)
                update(card.get_rectangle_dimensions())
