from pygame import Rect, Surface

class Card:

    def __init__(self, question: str, answer: str, rectangle_dimensions: Rect, surface: Surface):
        self.flipped = False
        self.question = question
        self.answer = answer
        self.rectangle_dimensions = rectangle_dimensions
        self.surface = surface

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_rectangle_dimensions(self) -> Rect:
        return self.rectangle_dimensions

    def get_surface(self) -> Surface:
        return self.surface

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

