import time

import flet as ft


class MainPage:

    def __init__(self):
        print(self)

    @staticmethod
    def build(window_width, window_height, page, values):

        MainPage.values = values
        MainPage.dragable = ft.Row(
            controls=[

            ]
        )

        def back(e, col):

            if col == 'green':

                conteiner_to_income.top += window_width / 1.85
                conteiner_to_income.opacity -= 1

                page.update()

            elif col == 'red':

                container_to_pay.top += window_width / 1.85
                container_to_pay.opacity -= 1

                page.update()

        MainPage.text_for_choice = ft.Text(
            value='Incomes',
            width=window_width/1.2,
            height=window_height / 10.8,
            text_align=ft.TextAlign.CENTER,
            size=window_width/26

        )

        MainPage.row_for_pay = ft.Row(
                            controls=[
                                ft.DragTarget(
                                    on_accept=lambda e:acept(e, 'red'),
                                    content=ft.Container(
                                        bgcolor='#A60000',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='Dolg',
                                            size=window_height/30
                                        )
                                    ),
                                ),
                                ft.DragTarget(
                                    on_accept=lambda e: acept(e, 'red'),
                                    content=ft.Container(
                                        bgcolor='#A60000',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='Home',
                                            size=window_height / 30
                                        )
                                    ),
                                ),
                                ft.DragTarget(
                                    on_accept=lambda e: acept(e, 'red'),
                                    content=ft.Container(
                                        bgcolor='#A60000',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='Enjoy',
                                            size=window_height / 30
                                        )
                                    ),
                                ),
                                ft.DragTarget(
                                    on_accept=lambda e: acept(e, 'red'),
                                    content=ft.Container(
                                        bgcolor='#A60000',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='Eat',
                                            size=window_height / 30
                                        )
                                    ),
                                ),

                            ],#Settings Row Dragtarget
                            top=window_height / 5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=window_width,
                            left=0,
                            scale=0,
                            animate_position=ft.animation.Animation(1200, ft.AnimationCurve.BOUNCE_IN_OUT),
                            animate_scale=ft.animation.Animation(700, ft.AnimationCurve.BOUNCE_IN_OUT),

        )

        MainPage.row_for_incomes = ft.Row(
                            controls=[
                                ft.DragTarget(
                                    on_accept=lambda e:acept(e, 'green'),
                                    content=ft.Container(
                                        bgcolor='#007730',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='SP',
                                            size=window_height / 30
                                        )
                                    ),
                                ),
                                ft.DragTarget(
                                    on_accept=lambda e: acept(e,'green'),
                                    content=ft.Container(
                                        bgcolor='#007730',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='SP 2',
                                            size=window_height / 30
                                        )
                                    ),
                                ),
                                ft.DragTarget(
                                    on_accept=lambda e: acept(e,'green'),
                                    content=ft.Container(
                                        bgcolor='#007730',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),
                                        width=window_width / 10,
                                        height=window_width / 15,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        border_radius=window_width / 38.4,
                                        content=ft.Text(
                                            value='DOLG',
                                            size=window_height/30
                                        )
                                    ),
                                ),
                                ft.DragTarget(
                                    on_accept=lambda e: acept(e,'green'),
                                    content=ft.Container(
                                        bgcolor='#007730',
                                        margin=ft.margin.only(left=window_width / 38.4,
                                                              top=window_width / 38.4),

                                        width=window_width / 10,
                                        height=window_width / 15,
                                        border_radius=window_width / 38.4,
                                        padding=ft.padding.only(top=window_height/54, left=window_height/54),
                                        content=ft.Text(
                                            value='Eneater',
                                            size=window_height/30,

                                        ),

                                    ),
                                ),

                            ],#Settings Row Dragtarget
                            top=window_height / 5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=window_width,
                            left=0,
                            scale=1,
                            animate_position=ft.animation.Animation(1200, ft.AnimationCurve.BOUNCE_OUT),
                            animate_scale=ft.animation.Animation(700, ft.AnimationCurve.BOUNCE_OUT),

                        )

        text_field_to_pay = ft.Container(
            content=ft.TextField(
                value="",
                hint_text="Сколько?",
                width=window_width / 1.2,
                height=window_height / 10.8,
                on_change=lambda e: save_text_field(e, 'red', text_field_to_pay.content.value),

            ),

        )

        container_to_pay = ft.Container(
            top=window_height,
            width=window_width/1.097142857142857,
            left=(window_width - (window_width/1.097142857142857)) / 2,
            height=700,
            border_radius=100,
            blur=ft.Blur(10, 5, ft.BlurTileMode.MIRROR),
            animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_IN),
            opacity=0,
            animate_opacity=ft.animation.Animation(800, ft.AnimationCurve.DECELERATE),
            content=ft.Column(
                controls=[
                    ft.Container(
                        width=window_width / 1.2,
                        height=window_height / 9,
                        bgcolor='#9A001E',
                        border_radius=window_width / 38.4,
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='-',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                )

                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        )
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                width=window_width / 9.6,
                                height=window_height / 19.2,

                                content=ft.Text(
                                    value='Back',
                                    size=35
                                ),
                                on_click=lambda e: back(e, 'red')
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    ),
                    text_field_to_pay,
                    ft.ElevatedButton(
                        width=window_width / 9.6,
                        height=window_height / 19.2,
                        content=ft.Text(
                            value='Append',
                            size=35,
                        ),
                        on_click=lambda e: append(e,
                                                  'red',
                                                  container_to_pay.content.controls[0].content.controls[1].value,
                                                  container_to_pay.content.controls[0].content.controls[3].value,)
                    )

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40
            )

        )



        text_field_to_incomes = ft.Container(
            content=ft.TextField(
                        value="",
                        hint_text="Сколько?",
                        width=window_width / 1.2,
                        height=window_height / 10.8,
                        on_change=lambda e: save_text_field(e, 'green', text_field_to_incomes.content.value)
                   ),
        )


        conteiner_to_income = ft.Container(
            top=window_height,
            width=window_width / 1.097142857142857,
            left=(window_width - (window_width / 1.097142857142857)) / 2,
            height=700,
            border_radius=100,
            blur=ft.Blur(10, 5, ft.BlurTileMode.MIRROR),
            animate_position=ft.animation.Animation(500, ft.AnimationCurve.DECELERATE),
            opacity=0,
            animate_opacity=ft.animation.Animation(800, ft.AnimationCurve.DECELERATE),
            content=ft.Column(

                controls=[
                    ft.Container(
                        width=window_width / 1.2,
                        height=window_height / 9,
                        bgcolor='#4E9600',
                        border_radius=window_width / 38.4,
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='+',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                ),
                                ft.Text(
                                    value='',
                                    size=window_width / 38.4,
                                )

                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        )
                    ),
                    ft.Row(
                        controls=[

                            ft.ElevatedButton(
                                width=window_width/9.6,
                                height=window_height/19.2,

                                content=ft.Text(
                                    value='Back',
                                    size=35
                                ),
                            on_click=lambda e: back(e, 'green')
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,


                    ),
                    text_field_to_incomes,
                    ft.ElevatedButton(
                        width=window_width / 9.6,
                        height=window_height / 19.2,
                        content=ft.Text(
                            value='Append',
                            size=35,
                        ),
                        on_click=lambda e: append(e,
                                                  'green',
                                                  conteiner_to_income.content.controls[0].content.controls[1].value,
                                                  conteiner_to_income.content.controls[0].content.controls[3].value

                                                  )
                    )

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40
            )

        )

        MainPage.text_to_cash = ft.Text(
            value=MainPage.values["Cash"],
            size=window_width / 38.4
        )

        MainPage.text_to_card = ft.Text(
            value=MainPage.values["Card"],
            size=window_width / 38.4
        )

        def choice(e):

            if MainPage.text_for_choice.value == "Incomes":
                MainPage.text_for_choice.value = 'Expenses'
                MainPage.row_for_incomes.scale -= 1
                MainPage.row_for_pay.scale += 1
                time.sleep(0.5)

            else:
                MainPage.text_for_choice.value = 'Incomes'
                MainPage.row_for_incomes.scale += 1
                MainPage.row_for_pay.scale -= 1
                time.sleep(0.5)

            if container_to_pay.opacity != 0:
                container_to_pay.top += window_width / 1.85
                container_to_pay.opacity -= 1

            if conteiner_to_income.opacity != 0:
                conteiner_to_income.top += window_width / 1.85
                conteiner_to_income.opacity -= 1
            page.update()

        def acept(e, color):

            src = page.get_control(e.src_id)

            if color == "red":

                if container_to_pay.opacity == 0:
                    container_to_pay.top -= window_width/1.85
                    container_to_pay.opacity += 1
                    container_to_pay.content.controls[0].content.controls[1].value = src.content.content.controls[-1].value
                    container_to_pay.content.controls[0].content.controls[0].value = MainPage.text_to_card.value
                    container_to_pay.content.controls[0].content.controls[3].value = e.control.content.content.value
                else:
                    container_to_pay.top += window_width / 1.85
                    container_to_pay.opacity -= 1

            elif color == "green":

                if conteiner_to_income.opacity == 0:
                    conteiner_to_income.content.controls[0].content.controls[3].value = src.content.content.controls[-1].value
                    conteiner_to_income.content.controls[0].content.controls[4].value = MainPage.text_to_card.value
                    conteiner_to_income.content.controls[0].content.controls[1].value = e.control.content.content.value

                    conteiner_to_income.top -= window_width/1.85
                    conteiner_to_income.opacity += 1
                else:
                    conteiner_to_income.top += window_width / 1.85
                    conteiner_to_income.opacity -= 1

            page.update()

        def save_text_field(e, color, value):
            MainPage.save = []
            MainPage.save.append(value)
            MainPage.save.append(color)

        def append(e, col, where, what):

            if col == 'green':
                MainPage.values[f'{what}'] += int(MainPage.save[0])
                if what == 'Cash':
                    MainPage.text_to_cash.value = MainPage.values[f"{what}"]

                elif what == 'Card':
                    MainPage.text_to_card.value = MainPage.values[f"{what}"]

                back(e, 'green')
                text_field_to_incomes.content.value = ''
                page.update()

            elif col == 'red':

                MainPage.values[f'{where}'] -= int(MainPage.save[0])
                if where == 'Cash':
                    MainPage.text_to_cash.value = MainPage.values[f"{where}"]

                elif where == 'Card':
                    MainPage.text_to_card.value = MainPage.values[f"{where}"]

                back(e, 'red')
                text_field_to_pay.content.value = ''
                page.update()

        MainPage.mainpage = ft.Column(

            controls=[
                ft.Container(
                    width=window_width/1.2,
                    height=window_height/10.8,
                    bgcolor='#67237F',
                    border_radius=(window_width/1.2) / (window_height/10.8),
                    margin=ft.margin.only(top=window_height / 54),
                    content=MainPage.text_for_choice,
                    ink=True,
                    on_click=lambda e:choice(e),

                ),
                ft.Stack(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Draggable(

                                    content=ft.Container(
                                        margin=ft.margin.only(left=window_width/38.4, top=window_width/38.4),
                                        width=window_width / 12.8,
                                        height=window_width / 12.8,
                                        border_radius=window_width/38.4,
                                        content=ft.Column(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.MONEY_SHARP,
                                                    size=window_width/38.4
                                                ),
                                                MainPage.text_to_card,
                                                ft.Text(
                                                    value='Card',
                                                    size=window_width / 96
                                                )

                                            ],#Settings Column
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        bgcolor='#67237F'
                                    )
                                ),
                                ft.Draggable(

                                    content=ft.Container(
                                        margin=ft.margin.only(left=window_width / 38.4, top=window_width / 38.4),
                                        width=window_width / 12.8,
                                        height=window_width / 12.8,
                                        border_radius=window_width/38.4,
                                        content=ft.Column(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.HOT_TUB,
                                                    size=window_width/38.4
                                                ),
                                                MainPage.text_to_cash,
                                                ft.Text(
                                                    value='Cash',
                                                    size=window_width / 96
                                                )
                                            ],  # Settings Column
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        bgcolor='#67237F'
                                    )
                                ),

                            ],# Setting Row Dragable
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=window_width

                        ),

                        MainPage.row_for_incomes,
                        MainPage.row_for_pay,
                        conteiner_to_income,
                        container_to_pay,

                    ],#Setting Stack For Dragable
                    width=window_width,
                    height=window_height

                )

            ],#Setting Collumn
            left=window_width - window_width,
            animate_position=ft.animation.Animation(1235, ft.AnimationCurve.DECELERATE),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=window_width,
            height=window_height,

        )

        return MainPage.mainpage