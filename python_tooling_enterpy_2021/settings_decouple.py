"""Settings"""
from decouple import config


PORT = config("PORT", cast=int, default=8080)
DOMAIN = config("DOMAIN", default="localhost")
ROOT_URL = config("ROOT_URL")
DEBUG = config("DEBUG", cast=bool)

print(PORT, type(PORT))
print(DOMAIN, type(DOMAIN))
print(ROOT_URL, type(ROOT_URL))
print(DEBUG, type(DEBUG))

# python python_tooling_enterpy_2021/settings-decouple.py
