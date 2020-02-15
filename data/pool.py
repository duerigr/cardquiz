import random
from data.question import Question


class Pool:

    def __init__(self, questions):
        self.questions = questions

    def get_all_questions(self) -> [Question]:
        return self.questions

    def get_random_questions(self, amount) -> [Question]:
        return random.sample(self.questions, amount)
