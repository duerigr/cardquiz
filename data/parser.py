import json
from data.pool import Pool
from data.question import Question


class Parser:

    def __init__(self):
        self.pools = []

    def parse(self, filename):
        with open("data/"+filename, encoding="utf-8") as jsonfile:
            rawdata = json.load(jsonfile)
            for pool in rawdata:
                questions = []
                for question in pool["questions"]:
                    questions.append(Question(question["q"], question["a"]))
                self.pools.append(Pool(questions, pool["id"], pool["name"], pool["points"]))

    def get_pools(self) -> [Pool]:
        return self.pools

    def get_pool(self, pool_id):
        for p in self.pools:
            if p.get_id() == pool_id:
                return p
        return self.pools[0]

    def print(self):
        for pool in self.pools:
            for question in pool.get_questions():
                print(question.get_question()+" -> "+question.get_answer())
