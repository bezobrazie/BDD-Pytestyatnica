from selenium.webdriver.common.by import By


class ManePageLocators:
    """Хранилище локаторов главной страницы, аналог BasePageLocators но только для главной страницы"""
    VIDGETS = (By. XPATH, 'test')
