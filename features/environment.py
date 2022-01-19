from behave import fixture, use_fixture
from behave.model import Scenario, Tag
from behave.runner import Context
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.pages.repository import PageRepository


def browser_chrome(context: Context):
    # создаем объект класа ChromeOptions для добавления параметров при запуске хрома.
    options = webdriver.ChromeOptions()
    options.add_argument('no-sandbox')
    options.add_argument('isable-extensions')
    options.add_argument('start-maximized')
    # options.add_argument('headless')
    # Обявляем экземпляр класа хромдрайвера ChromeDriverManager класс для автоматического скачивания драйвера
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.browser = browser
    yield context.browser
    context.browser.quit()


def browser_firefox(context: Context):
    # Обявляем экземпляр класа фаерфокс GeckoDriverManager класс для автоматического скачивания драйвера
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.browser = browser
    yield context.browser
    context.browser.quit()


# Словарь который используется для подготовки фикстур before_tag
fixture_registry = {
    "fixture.browser.firefox": browser_firefox,
    "fixture.browser.chrome": browser_chrome
}


def before_tag(context: Context, tag: Tag):
    """Подготовка фикстур."""
    if tag.startswith("fixture."):
        return use_fixture(fixture_registry.get(tag), context)


def before_scenario(ctx: Context, scenario: Scenario):
    """Действия перед выполнением сценариев. Открывает главную страницу. """
    ctx.pages = PageRepository(ctx)
    ctx.pages.base.open()
