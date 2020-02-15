import uuid


class Question:

    def __init__(self, question: str, answer: str):
        self.id = uuid.uuid4()
        self.question = question
        self.answer = answer

    def get_id(self):
        return self.id

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer
