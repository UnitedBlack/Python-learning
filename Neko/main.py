import flet as ft
from flet_route import Routing, path


def main(page: ft.Page):
    page.window_height = 600
    page.window_width = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
