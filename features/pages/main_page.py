from features.pages.base_page import BasePage


class MainPage(BasePage):
    """ Класс для хранения методов работы с главной страницей"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
