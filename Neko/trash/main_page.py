import flet as ft


class MainPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
                ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
                ft.NavigationDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Explore",
                ),
            ],
        )

    def build(self):
        # self.page.add(ft.Text(value="aaaaaaaaaa"))
        return ft.Column(self.page.navigation_bar)


# class MainPage(ft.UserControl)
#     def __init__(self, page):
#         super().__init__()
#         self.page = page

#     def build(self):
#         ...
# def build(self):
#     return self.layout()
