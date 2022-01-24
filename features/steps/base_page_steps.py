import time

from behave import *
from behave.runner import Context
from features.locators.base_page import BasePageLocators


@When('Нажимаем на кнопку "Войти"')
def click_at_sign_in(ctx: Context):
    """Нажать на кнопку "Войти" в шапке сайта"""
    ctx.pages.base.click(BasePageLocators.SIGN_IN)


@When('Нажимаем на кнопку с текстом "{text}"')
def click_at_button(ctx: Context, text):
    """Нажать на кнопку из "подменю" с текстом который мы передаем в качестве аргумента"""
    ctx.pages.base.click(BasePageLocators.SUB_MENU_BUTTON(text))


@When('Делаем скриншот и сохраняем с именем "{screenshot_name}"')
def do_screenshot(ctx: Context, screenshot_name: str):
    ctx.pages.base.do_screenshot(screenshot_name)


@When('Вводим в поле поиска значение "{value}"')
def input_in_search(ctx: Context, value: str):
    ctx.pages.base.input_in_search(value)


@When('Нажимаем "Поиск"')
def click_do_search(ctx: Context):
    """
    Кнопка поиск не всегда нажимается без явного ожидания,
    хотя стоит условие element_to_be_clickable в чем проблема - хз, нужно дебажить, нет времени.
    """
    time.sleep(1)
    ctx.pages.base.click(BasePageLocators.DO_SEARCH_BUTTON)


@Then('Происходит редирект на страницу авторизации гугла')
def check_auth_page(ctx: Context):
    assert ctx.pages.base.check_number_of_browser_tabs(1), "открыто больше одной вкладки"
    assert ctx.pages.base.check_an_element_is_present(BasePageLocators.AUTH_TEXT),\
        "Нет локатора BasePageLocators.AUTH_TEXT на странице, а мы его хотели увидеть, дада, такие дела."
    # Можно было реализовать через код ниже, но я решил написать доп метод, чтобы было красивее и не было лишней реализации.
    # WebDriverWait(ctx.browser, 10).until(ec.visibility_of_element_located(BasePageLocators.AUTH_TEXT))


@Then('В URL есть значение "{url}"')
def check_url(ctx: Context, url):
    """
    Проверяет не полный урл, а наличие значения внутри урла страницы
    """
    assert ctx.pages.base.check_url_contains_value(url), f'В урле нет значения {url}'


@Then('Имя первого видео "{expected_name}"')
def check_quantity_sign_in_button(ctx: Context, expected_name: str):
    first_video_name = ctx.pages.base.get_text_from_element(BasePageLocators.FIRST_ITEM_IN_SEARCH)
    assert first_video_name == expected_name, f'На странице {first_video_name} кнопок "Войти", ожидалось {expected_name}'
