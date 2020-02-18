import pygameMenu
from ui.config import Config


class Menu:

    def __init__(self, screen, font, pools, handler):
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
        self.menu.add_selector("Pool: ",
                               self.__create_pools_options(pools),
                               selector_id="pool",
                               default=0,
                               onchange=self.__pool_changed)
        self.menu.add_option("Start", handler, self.__get_selected_pool)
        self.menu.add_option("Ende", pygameMenu.events.EXIT)

    def menu_background(self):
        pass

    def mainloop(self, events):
        self.menu.mainloop(events)

    def disable(self):
        self.menu.disable()

    def enable(self):
        self.menu.enable()

    def __create_pools_options(self, pools):
        options = []
        for pool in pools:
            options.append((pool.get_name(), pool.get_id()))

        self.pool = options[0]
        return options

    def __pool_changed(self, value, pool_id):
        self.pool = pool_id

    def __get_selected_pool(self):
        return self.pool
