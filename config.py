import os

SETTINGS = {
    "prod": {
        "baseUrl": "https://www.youtube.com/",
    }
}


STAND = os.environ.get('STAND', 'prod')
CONFIG = SETTINGS[STAND]
