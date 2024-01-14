from flet import app, Page, FLET_APP

from application.searchPage import SearchPage


class Main:

    @staticmethod
    def main(page: Page):
        search = SearchPage(page)
        search.render()


if __name__ == '__main__':
    application = Main()
    app(target=application.main, view=FLET_APP)
