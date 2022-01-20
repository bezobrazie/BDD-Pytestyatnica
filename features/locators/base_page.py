from selenium.webdriver.common.by import By


class BasePageLocators:
    """Хранилище базовых локаторов. В нем хранятся торлкьо те локаторы, которые присутствуют на всех страницах сайта.
     (Ну или хотя-бы на большинстве :) )"""
    # Поле поиска
    SEARCH_FIELD = (By.XPATH, '//*[@name="search_query"]')
    # Кнопка "Войти" из шапки сайта
    SIGN_IN = (By.XPATH, 'test')
    # Кнопка гамбургера, открывает/закрывает меню
    MENU_BUTTON = (By.XPATH, 'test')
    # Кнопка "Главная" в меню
    MENU_BUTTON_MAIN = (By.XPATH, 'test')
    # Кнопка "Навигатор" в меню
    MENU_BUTTON_NAVIGATOR = (By.XPATH, 'test')
    # Кнопка "Библиотека" в меню
    MENU_BUTTON_LIBRARY = (By.XPATH, 'test')
    # Кнопка "История" в меню
    MENU_BUTTON_HISTORY = (By.XPATH, 'test')
    # Перенести дял каждой страницы свой алерт.
    # Ниже локатор общий для 2х страниц. Из которого можно вытащить месагу о том, что пользователь не авторизован, для всех страниц не подходит.
    ALERT_TEXT = (By. XPATH, '//*[@class="promo-body-text style-scope ytd-background-promo-renderer"]')
