import flet as ft


class NavigationBar(ft.View):
    def __init__(self, link):
        sel
    def build(self, page: ft.Page):
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