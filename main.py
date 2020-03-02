import pygame
from pygame.locals import *
import pygameMenu
from data.parser import Parser
from ui.card import Card
from ui.carddisplay import Carddisplay
from ui.config import Config
from ui.cardboard import Cardboard
from ui.menu import Menu


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
        cls.font = pygame.font.Font(Config.font_setting[0], cls.fontconfig[0])
        cls.pools = cls.parser.get_pools()

        cls.cardisplay = Carddisplay(cls.switch_cardboard, (cls.screen.get_width(), cls.screen.get_height()))
        cls.cardboard = Cardboard(cls.switch_menu, cls.switch_carddisplay, cls.pools, cls.font, cls.fontconfig,
                                  (cls.screen.get_width(), cls.screen.get_height()))
        cls.menu = Menu(cls.screen, Config.font_setting[0], cls.switch_cardboard_new, cls.switch_cardboard)
        pygame.display.flip()

        cls.main()

    @classmethod
    def main(cls):
        while True:
            events = pygame.event.get()
            cls.menu.mainloop(events)
            cls.cardboard.mainloop(events, cls.screen)
            cls.cardisplay.mainloop(events)
        cls.quit()

    @classmethod
    def switch_cardboard_new(cls):
        cls.menu.disable()
        cls.cardboard = Cardboard(cls.switch_menu, cls.switch_carddisplay, cls.pools, cls.font, cls.fontconfig,
                                  (cls.screen.get_width(), cls.screen.get_height()))
        cls.cardboard.enable(cls.screen)
        cls.cardisplay.disable()

    @classmethod
    def switch_cardboard(cls):
        cls.menu.disable()
        cls.cardboard.enable(cls.screen)
        cls.cardisplay.disable()

    @classmethod
    def switch_menu(cls):
        cls.cardboard.disable(cls.screen)
        cls.menu.enable()
        cls.cardisplay.disable()

    @classmethod
    def switch_carddisplay(cls, card: Card):
        cls.cardboard.disable(cls.screen)
        cls.menu.disable()
        cls.cardisplay.enable(cls.screen, card)

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
