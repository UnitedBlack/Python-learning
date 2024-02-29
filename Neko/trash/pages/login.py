from flet import *


class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        page.title = "Neko"
        page.vertical_alignment = MainAxisAlignment.CENTER
        page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.app_icon = Column(
            [
                Container(
                    content=Image(
                        src="/neko.jpg",
                        width=200,
                        fit=ImageFit.CONTAIN,
                        border_radius=100,
                    ),
                    alignment=alignment.top_center,
                )
            ]
        )
        self.login_button = Column(
            [
                Container(
                    content=ElevatedButton(text="Login", height=80, width=250),
                    alignment=alignment.center,
                    on_click=lambda _: self.page.go("/main_page"),
                ),
            ]
        )

    def login(self, e):
        ...

    def build(self):
        self.navigation_bar = NavigationBar(
            destinations=[
                NavigationDestination(icon=icons.EXPLORE, label="Explore"),
                NavigationDestination(icon=icons.COMMUTE, label="Cmuasdsadte"),
                NavigationDestination(
                    icon=icons.BOOKMARK_BORDER,
                    selected_icon=icons.BOOKMARK,
                    label="Explore",
                ),
            ],
        )
        return Column(
            [self.app_icon, self.login_button, self.navigation_bar],
            alignment=alignment.center,
        )
