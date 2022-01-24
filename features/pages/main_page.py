from features.pages.base_page import BasePage
from config import CONFIG
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    """ Класс для хранения методов работы с главной страницей"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def url_is_main(self) -> bool:
        """Проверить что находимся на главной странице исходя из урла, тянем его из конфиг файла."""
        try:
            WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
                ec.url_to_be(CONFIG["baseUrl"]))
            return True
        except TimeoutException:
            return False
