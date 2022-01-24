from behave import fixture, use_fixture
from behave.model import Scenario, Tag
from behave.runner import Context
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.pages.repository import PageRepository
from behave.model import Step


def browser_chrome(context: Context):
    # создаем объект класа ChromeOptions для добавления параметров при запуске хрома.
    # Каждый параметр можно погуглить :)
    options = webdriver.ChromeOptions()
    options.add_argument('no-sandbox')
    options.add_argument('isable-extensions')
    options.add_argument('start-maximized')
    # options.add_argument('headless')
    # Обявляем экземпляр класа хромдрайвера ChromeDriverManager класс для автоматического скачивания драйвера
    # В будущем соответственно вызываем браузер через контекст как показано ниже.
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.browser = browser
    # Служит для закрытия браузера в конце тестов или при их падении
    yield context.browser
    context.browser.quit()


def browser_firefox(context: Context):
    # Аналог метода для хрома browser_chrome
    # Обявляем экземпляр класа фаерфокс GeckoDriverManager класс для автоматического скачивания драйвера.
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.browser = browser
    yield context.browser
    context.browser.quit()


# Словарь который используется для подготовки фикстур before_tag,
# в значениях прописаны имена функций в которых создаются экземпляры класа браузер
fixture_registry = {
    "fixture.browser.firefox": browser_firefox,
    "fixture.browser.chrome": browser_chrome
}


def before_tag(context: Context, tag: Tag):
    """Подготовка фикстур. Для запуска сценариев в разных браузерах"""
    if tag.startswith("fixture."):
        return use_fixture(fixture_registry.get(tag), context)


def before_scenario(ctx: Context, scenario: Scenario):
    """Действия перед выполнением сценариев. Открывает главную страницу.
    Сюда можно запихнуть все что угодно что должно запускаться перед каждым сценарием.
    Я запихнул сюда создание объектов класса PageRepository для быстрого доступа к любому класу из директории pages.
    Благодаря этому не нужно создавать в каждой функции объект класса с методом которого мы собираемся работать.
    После инициализации можно добавить например авторизацию, если во всех тестах она используется
    или обыграть это доп логикой.
    """
    ctx.pages = PageRepository(ctx)


def after_step(ctx: Context, step: Step):
    """
    При падении шага создает скриншот
    """
    if step.status == 'failed':
        step_name = step.filename.replace("features/", "") + "." + str(step.line)
        ctx.pages.base.create_screenshot(step_name)
