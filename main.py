import pygame
from pygame.locals import *
from data.parser import Parser


class Config:
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    blue = 0, 0, 255
    display_height = 480
    display_width = 640


class Main:

    @classmethod
    def init(cls):
        p = Parser()
        p.parse("questions.json")
        pygame.init()
        screen = pygame.display.set_mode((Config.display_width, Config.display_height))
        screen.fill(Config.blue)

        # display text
        largeText = pygame.font.Font("res/MechanicalBold-oOmA.otf", 30)
        textSurface = largeText.render("Hallo Welt", True, Config.white)
        textRect = textSurface.get_rect()
        textRect.center = ((Config.display_width / 2), (Config.display_height / 2))
        screen.blit(textSurface, textRect)
        pygame.display.update()

    @classmethod
    def main(cls):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    running = False
            pygame.display.update()


Main.init()
Main.main()

pygame.quit()
quit()
