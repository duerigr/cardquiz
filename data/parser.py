import json


class Parser:

    def __init__(self):
        self.pools = []

    def parse(self, filename):
        with open("data/"+filename) as jsonfile:
            self.pools = json.load(jsonfile)

    def print(self):
        for pool in self.pools:
            for question in pool["questions"]:
                print(question["q"]+" -> "+question["a"])
