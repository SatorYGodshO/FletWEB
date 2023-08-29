import flet as ft


from win32api import GetSystemMetrics

from backend.Load_Json import Load

from frontend.Navigation import Navigation
from frontend.MainPage import MainPage
from frontend.PageList import Pagelist
from frontend.SettingsPage import Setting


class Main(ft.Page):

    load_value = None

    @staticmethod
    def build(e):
        print(e)

        def load():
            Main.load_value = Load.load()
        load()
        wight = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        print(wight, height)

        main = ft.Stack(
            controls=[
                MainPage.build(wight, height, Main.page, Main.load_value),
                Pagelist.build(wight, height),
                Setting.build(wight, height)

            ],
            width=wight,
            height=height,

        )
        return main

    def main(self):
        Main.page = self
        self.fonts = {"3d": 'fonts/crackman2.ttf',
                      "3drus": 'fonts/a_romanussh2.ttf',
                      'one_most': 'fonts/mckloud-tempest.ttf'}
        self.window_width = 640
        self.window_height = 1136
        self.bgcolor = '#52026E'
        self.window_full_screen = True
        self.theme = ft.Theme(font_family='one_most')
        self.navigation_bar = Navigation.build(GetSystemMetrics(0), GetSystemMetrics(1), self)
        self.add(
            Main.build(12)
        )


if __name__ == '__main__':

    ft.app(target=Main.main)
