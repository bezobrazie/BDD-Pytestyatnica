from behave import *
from behave.runner import Context


@Given('Открыта главная страница YouTube')
def main_page_is_open(ctx: Context):
    """Проверка по урлу, что мы находимся на главной странице"""
    ctx.pages.base.open()
    assert ctx.pages.main.url_is_main()
