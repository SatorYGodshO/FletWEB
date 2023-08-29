import flet as ft


class Setting:

    def __init__(self):

        self.data = None

    def build(self_wight, self_heigth):
        print(self_wight * 4)
        Setting.mainpage = ft.Container(
            width=100,
            height=100,
            bgcolor=ft.colors.CYAN_700,
            top=0,
            left=self_wight*4,
            animate_position=ft.animation.Animation(1235, ft.AnimationCurve.DECELERATE)
        )

        return Setting.mainpage

    def __del__(self):
        self.root = None

