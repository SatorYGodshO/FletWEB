import flet as ft

from frontend.MainPage import MainPage
from frontend.PageList import Pagelist
from frontend.SettingsPage import Setting

class Navigation:

    def __init__(self):

        self.root = None

    def build(self_wight, self_height, page):
        print(page)

        def _change(e):
            my_index = e.control.selected_index
            if my_index == 1:
                if MainPage.mainpage.left != 0:
                    Pagelist.mainpage.left = -self_wight
                    MainPage.mainpage.left = 0

                    Setting.mainpage.left = self_wight * 4
                else:
                    pass

                page.update()
            elif my_index == 4:
                if Setting.mainpage.left != 0:
                    Pagelist.mainpage.left = -self_wight * 4
                    MainPage.mainpage.left = -self_wight * 3

                    Setting.mainpage.left = 0
                else:
                    pass
                page.update()

            elif my_index == 0:
                if Pagelist.mainpage.left != 0:
                    Pagelist.mainpage.left = 0
                    MainPage.mainpage.left += self_wight

                    Setting.mainpage.left = self_wight * 4

                else:
                    pass

                page.update()


        navigationbar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.BLENDER
                ),
                ft.NavigationDestination(
                    icon=ft.icons.HOME
                ),
                ft.NavigationDestination(
                    icon=ft.icons.WIDGETS
                ),
                ft.NavigationDestination(
                    icon=ft.icons.RADIO_BUTTON_ON
                ),
                ft.NavigationDestination(
                    icon=ft.icons.SETTINGS
                ),


            ],#Settings Navigation Bar
            on_change=lambda e: _change(e),
            selected_index=1
        )

        return navigationbar