"""Settings"""
import os

from dotenv import load_dotenv


load_dotenv()
PORT = int(os.environ["PORT"] if "PORT" in os.environ else "8080")
DOMAIN = os.environ["DOMAIN"] if "DOMAIN" in os.environ else "localhost"
ROOT_URL = os.environ["ROOT_URL"]
DEBUG = bool(os.environ["DEBUG"])

print(PORT, type(PORT))
print(DOMAIN, type(DOMAIN))
print(ROOT_URL, type(ROOT_URL))
print(DEBUG, type(DEBUG))

# python python_tooling_enterpy_2021/settings-dotenv.py
