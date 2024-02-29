# import flet as ft


# class FirstWindow(ft.Window):
#     def build(self, page: ft.Page):
#         page.title = "First Window"
#         # ... остальной код для построения первого окна ...


# class SecondWindow(ft.Window):
#     def build(self, page: ft.Page):
#         page.title = "Second Window"
#         # ... остальной код для построения второго окна ...


# if __name__ == "__main__":
#     first_window = FirstWindow()
#     second_window = SecondWindow()

#     ft.app(target=first_window)
#     ft.app(target=second_window)
# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 20)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 20)
#         page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )
import flet as ft



def main(page: ft.Page):
    page.title = "Headspace clone"

    def change_content(e):
        print(e)
        page.controls.clear()

        if e == "default":
            nav_dest = 0
        else:
            nav_dest = e.control.selected_index

        if nav_dest == 0:
            nav_content = ft.Container(content=ft.Text(value="Today"))
            page.add(nav_content)

        if nav_dest == 1:
            nav_content = ft.Container(content=ft.Text(value="Explore"))
            page.add(nav_content)

        if nav_dest == 2:
            page.controls.clear()
            new_page = create_today_page()
            page.add(new_page)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.LANDSCAPE_OUTLINED,
                selected_icon=ft.icons.LANDSCAPE,
                label="Today",
            ),
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Explore"),
            ft.NavigationDestination(
                icon=ft.icons.PERSON_OUTLINED,
                selected_icon=ft.icons.PERSON,
                label="You",
            ),
        ],
        on_change=change_content,
        selected_index=0,
    )

    page.navigation_bar.did_mount = page.navigation_bar.on_change("default")

    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")


# def navigate_to_today_page():
#     # Очистите текущую страницу
#     page.controls.clear()

#     # Создайте новую страницу
#     new_page = create_today_page()

#     # Добавьте новую страницу на экран
#     page.add(new_page)
