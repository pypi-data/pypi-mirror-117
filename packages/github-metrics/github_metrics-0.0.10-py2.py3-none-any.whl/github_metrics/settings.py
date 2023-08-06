import os

from decouple import config

BASE_DIR = os.path.dirname(__file__)

GITHUB_LOGIN = config("GITHUB_LOGIN", default="")
GITHUB_TOKEN = config("GITHUB_TOKEN", default="")
ORG_NAME = config("ORG_NAME", default="")
REPOSITORY_NAME = config("REPOSITORY_NAME", default="")
