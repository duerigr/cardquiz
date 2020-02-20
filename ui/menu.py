import pygameMenu
from ui.config import Config


class Menu:

    def __init__(self, screen, font, handler):
        self.menu = pygameMenu.Menu(screen,
                                    Config.display_width,
                                    Config.display_height,
                                    font,
                                    "Hauptmenü",
                                    bgfun=self.menu_background,
                                    color_selected=Config.white,
                                    font_color=Config.gray,
                                    font_size=30,
                                    font_size_title=40,
                                    menu_alpha=100,
                                    menu_color=Config.niceblue,
                                    option_shadow=False,
                                    )
        self.menu.add_option("Start", handler)
        self.menu.add_option("Ende", pygameMenu.events.EXIT)

    def menu_background(self):
        pass

    def mainloop(self, events):
        self.menu.mainloop(events)

    def disable(self):
        self.menu.disable()

    def enable(self):
        self.menu.enable()
