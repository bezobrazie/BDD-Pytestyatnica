import os


# Путь до папки с проектом
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Путь до папки со скриншотами
SCREENSHOTS_PATH = os.path.join(BASE_PATH, "temp", "screenshots")

# Вспомогательный словарь для хранения тест данных при использовании нескольких окружений.
SETTINGS = {
    "prod": {
        "baseUrl": "https://www.youtube.com/",
    }
}

# Если окружение не указано, по умолчанию откроется прод
STAND = os.environ.get('STAND', 'prod')
CONFIG = SETTINGS[STAND]
