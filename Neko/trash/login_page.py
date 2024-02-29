import flet as ft


# class LoginPage(ft.UserControl):
#     def __init__(self, page):
#         self.page = page

#     def build(self):
#         return self.page.add(ft.Text(value="asdasddsa"))


class LoginPage(ft.UserControl):
    def __init__(self, page, main_page):
        super().__init__()
        self.page = page
        self.main_page = main_page
        self.app_icon = ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src="/neko.jpg",
                        width=200,
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=100,
                    ),
                    alignment=ft.alignment.top_center,
                )
            ]
        )
        self.login_button = ft.Column(
            [
                ft.Container(
                    content=ft.ElevatedButton(text="Login", height=80, width=250),
                    alignment=ft.alignment.center,
                    on_click=self.main_page,
                ),
            ]
        )

    def build(self):
        return ft.Column([self.app_icon, self.login_button])


#         page.add(st, zalu)
#         page.update()
# class LoginPage(ft.View):
#     def build(self, page: ft.Page):
#         page.add(ft.Text("assadasdasd"))

#    st = ft.Container(
#        content=ft.Image(
#            src="/neko.jpg",
#            width=200,
#            fit=ft.ImageFit.CONTAIN,
#            border_radius=100,
#        ),
#        alignment=ft.alignment.top_center,
#    )
#    zalu = ft.Container(
#        content=ft.ElevatedButton(text="Login", height=80, width=250),
#        alignment=ft.alignment.center,
#    )
#    row = ft.Row([st, zalu])
#    page.add(row)


# class LoginPage(ft.View):
#     def build(self, page: ft.Page):
#         st = ft.Container(
#             content=ft.Image(
#                 src="/neko.jpg",
#                 width=200,
#                 fit=ft.ImageFit.CONTAIN,
#                 border_radius=100,
#             ),
#             alignment=ft.alignment.top_center,
#         )
#         zalu = ft.Container(
#             content=ft.ElevatedButton(text="Login", height=80, width=250),
#             alignment=ft.alignment.center,
#         )
#         column = ft.Row([st, zalu])
#         page.add(column)
#         page.update()
