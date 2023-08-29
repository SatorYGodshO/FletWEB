import flet as ft


class Pagelist:

    def __init__(self):

        self.root = None

    def apend(page, color, value, what, where, date, window_wight, window_height):

        conteiner = ft.Container(
            width=window_wight/
        )

        Pagelist.mainpage.controls.append(
            conteiner
        )

    @staticmethod
    def build(self_wight, self_heigth, self):

        Pagelist.mainpage = ft.Column(
            controls=[

            ]
        )



        return Pagelist.mainpage

    def __del__(self):

        self.root = None
