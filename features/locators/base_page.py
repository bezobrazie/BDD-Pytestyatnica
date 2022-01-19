from selenium.webdriver.common.by import By


class BasePageLocators:
    """Хранилище локаторов базовой страницы"""
    SEARCH_FIELD = (By.XPATH, '//*[@name="search_query"]')
    ALERT_TEXT = (By. XPATH, '//*[@class="promo-body-text style-scope ytd-background-promo-renderer"]')
