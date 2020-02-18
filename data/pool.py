import random
from data.question import Question


class Pool:

    def __init__(self, questions, ownid, name):
        self.questions = questions
        self.ownid = ownid
        self.name = name

    def get_all_questions(self) -> [Question]:
        return self.questions

    def get_random_questions(self, amount) -> [Question]:
        return random.sample(self.questions, amount)

    def get_id(self):
        return self.ownid

    def get_name(self):
        return self.name
