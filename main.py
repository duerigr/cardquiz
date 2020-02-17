import pygame
from pygame.locals import *
from data.parser import Parser
from ui.card import Card
from ui.config import Config
from ui.cardboard import Cardboard


class Main:

    @classmethod
    def init(cls):
        # set font config
        cls.fontconfig = Config.font_vars["large"]

        cls.parser = Parser()
        cls.parser.parse("questions.json")
        pygame.init()
        cls.screen = pygame.display.set_mode((Config.display_width, Config.display_height))
        cls.screen.fill(Config.niceblue)

        # display cards
        cls.font = pygame.font.Font(Config.font_setting[0], cls.fontconfig[0])
        pools = cls.parser.get_pools()
        # TODO select pool

        cls.render_object = Cardboard(pools[0], cls.fontconfig)
        cls.render_object.render_all(cls.screen)

        cls.main()

    @classmethod
    def main(cls):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    cls.render_object.handle_click(mouse_x, mouse_y, cls.screen)
        cls.quit()

    @classmethod
    def quit(cls):
        pygame.quit()
        quit()

    @classmethod
    def log(cls, msg):
        if Config.debug:
            print(msg)


if __name__ == '__main__':
    Main.init()
