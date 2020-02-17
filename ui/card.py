import textwrap
from pygame import Rect, Surface, font


class Card:

    def __init__(self, question: str, answer: str, rectangle_dimensions: Rect, fontconfig, fontsetting):
        self.flipped = False
        self.question = question
        self.answer = answer
        self.rectangle_dimensions = rectangle_dimensions
        self.font_config_question = self.__calculate_font_config_for_text(fontconfig, fontsetting, self.question)
        self.font_config_answer = self.__calculate_font_config_for_text(fontconfig, fontsetting, self.answer)

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_display_text(self):
        return self.answer if self.flipped else self.question

    def get_rectangle_dimensions(self) -> Rect:
        return self.rectangle_dimensions

    def set_question(self, question):
        self.question = question

    def set_answer(self, answer):
        self.question = answer

    def point_in_card_dimensions(self, x, y):
        return self.rectangle_dimensions.topleft[0] < x < self.rectangle_dimensions.topright[0] and \
                                self.rectangle_dimensions.topleft[1] < y < self.rectangle_dimensions.bottomleft[1]

    def flip(self):
        if self.flipped:
            text = self.question
        else:
            text = self.answer
        self.flipped = not self.flipped
        return text

    def is_flipped(self):
        return self.flipped

    def get_fontconfig(self):
        return self.font_config_answer if self.flipped else self.font_config_question

    def __calculate_font_config_for_text(self, fontconfig, fontsetting, text) -> [int, int, [(Surface, Rect)]]:
        cardfontconfig = [fontconfig[0], fontconfig[1], []]
        fitting = False
        while not fitting:
            cardfont = font.Font(fontsetting[0], cardfontconfig[0])
            message = textwrap.fill(text, cardfontconfig[1])
            lines = message.split("\n")
            x = self.rectangle_dimensions.midtop[0]
            y = self.rectangle_dimensions.midtop[1] + cardfontconfig[0]
            text_surfaces = []
            for part in lines:
                text_surface = cardfont.render(part, True, fontsetting[1])
                text_rect = text_surface.get_rect()
                text_rect.center = (x, y)
                y += 1.75 * cardfontconfig[0]
                text_surfaces.append(text_surface)
                cardfontconfig[2].append((text_surface, text_rect))
            fitting = True
            text_height = 0
            for surf in text_surfaces:
                text_height += surf.get_rect().height
            text_height *= 1.8
            if text_height > self.rectangle_dimensions.height:
                fitting = False
                cardfontconfig[0] = cardfontconfig[0] - 2
                cardfontconfig[1] = cardfontconfig[1] + 2
                cardfontconfig[2].clear()

        return cardfontconfig
