from flet import *


class MainPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        # self.page.navigation_bar = NavigationBar(
        #     destinations=[
        #         NavigationDestination(icon=icons.EXPLORE, label="Explore"),
        #         NavigationDestination(icon=icons.COMMUTE, label="Cmuasdsadte"),
        #         NavigationDestination(
        #             icon=icons.BOOKMARK_BORDER,
        #             selected_icon=icons.BOOKMARK,
        #             label="Explore",
        #         ),
        #     ]
        # )

        self.page.drawer = NavigationDrawer(
            controls=[
                Container(height=12),
                NavigationDrawerDestination(
                    label="Item 1",
                    icon=icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon_content=Icon(icons.DOOR_BACK_DOOR),
                ),
                Divider(thickness=2),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=icons.MAIL,
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=icons.PHONE,
                ),
            ],
        )

        def show_drawer(e):
            page.drawer.open = True
            page.drawer.update()


    def initialize(self):
        self.txt = Column([Text("addd")], alignment=alignment.bottom_center)
        return self.page.drawer

    def build(self):
        # self.page.add(Text(value="aaaaaaaaaa"))
        return self.initialize()
