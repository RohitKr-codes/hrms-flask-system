"""
Application Configuration
"""

import os


class Config:
    """Base Config"""

    SECRET_KEY = os.getenv("SECRET_KEY", "hrms-secret")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR, "hrms.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
