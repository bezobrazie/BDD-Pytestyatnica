from selenium.webdriver.common.by import By


class BasePageLocators:
    """Хранилище базовых локаторов. В нем хранятся торлкьо те локаторы, которые присутствуют на всех страницах сайта.
     (Ну или хотя-бы на большинстве :) )"""
    # Поле поиска
    SEARCH_FIELD = (By.XPATH, '//*[@name="search_query"]')

    # Кнопка поиска
    DO_SEARCH_BUTTON = (By.XPATH, '//button[@class="style-scope ytd-searchbox"]')

    # Кнопка "Войти" из шапки сайта
    SIGN_IN = (By.XPATH, '(//*[@aria-label="Войти"])[1]')

    # Все кнопки "Войти" на странице локатор для примера подсчета элементов на странице
    SIGN_IN_FOR_FUN = (By.XPATH, '//*[@aria-label="Войти"]')

    # Лямбда функция для примера создания однотипных локаторов
    SUB_MENU_BUTTON = lambda button_name: (By.XPATH, f"(//*[text()='{button_name}'])[1]")




    # ЛОКАТОР ДЛЯ ПРОВЕРКИ, ЧТО МЫ НАХОДИМСЯ АН СТРАНИЦЕ ВТОРИЗАЦИИ.
    # По хорошему для него нужнен отдельный файлик или класс, но т.к. локатор один, я сделаю исключение.
    AUTH_TEXT = (By.XPATH, "//*[text()='Перейдите на YouTube']")
