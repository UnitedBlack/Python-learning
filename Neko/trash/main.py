from flet import *
from pages.login import Login
from pages.main_page import MainPage


class ManekiNeko(UserControl):
    def __init__(self, page):
        self.page = page
        self.page.update()
        self.initialize()
        self.page.window_always_on_top = True

    def initialize(self):
        self.page.on_route_change = self.on_route_change
        self.page.go("/main_page")

    def on_route_change(self, route):
        self.page.views.clear()
        new_page = {
            "/main_page": MainPage,
            "/login": Login,
        }[
            self.page.route
        ](self.page)
        self.page.views.clear()
        self.page.views.append(View(route, [new_page]))


def main(page: Page):
    # page.window_height = 600
    # page.window_width = 700
    # page.vertical_alignment = MainAxisAlignment.CENTER
    # page.horizontal_alignment = CrossAxisAlignment.CENTER

    app = ManekiNeko(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    app(target=main, assets_dir="assets")
