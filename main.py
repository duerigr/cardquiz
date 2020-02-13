from data.parser import Parser


def main():
    p = Parser()
    p.parse("questions.json")
    p.print()


main()
