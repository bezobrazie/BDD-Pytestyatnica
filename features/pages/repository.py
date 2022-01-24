from behave.runner import Context
from features.pages.base_page import BasePage
from features.pages.main_page import MainPage


class lazy_property:
    """Декоратор для объявления "ленивых" свойств"""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value


class PageRepository:
    """Репозиторий страниц"""

    def __init__(self, context: Context):
        self.context = context

    @lazy_property
    def base(self):
        return BasePage(self.context.browser)

    @lazy_property
    def main(self):
        return MainPage(self.context.browser)
