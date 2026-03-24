# ======== CONFIG GLOBAL ========

ENV = "QA"   # poti schimba in DEV / QA / PROD

URLS = {
    "DEV": "https://the-internet.herokuapp.com/login",
    "QA":  "https://the-internet.herokuapp.com/login",
    "PROD": "https://the-internet.herokuapp.com/login"
}

BASE_URL = URLS[ENV]

BROWSER = "chrome"
HEADLESS = True   # True = fara fereastra vizibila
