import os
from dotenv import load_dotenv

from sqlalchemy import NullPool

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


if os.environ.get("TEST_DATABASE_URL") is not None:
    DATABASE_URL = os.environ.get("TEST_DATABASE_URL")
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    DATABASE_PARAMS = {}
