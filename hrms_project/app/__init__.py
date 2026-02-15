"""
Flask App Factory
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config


# ✅ GLOBAL EXTENSIONS (IMPORTANT)
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Create Flask App"""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "../templates"),
        static_folder=os.path.join(BASE_DIR, "../static")
    )

    app.config.from_object(Config)

    CORS(app)

    # ✅ INIT EXTENSIONS
    db.init_app(app)
    migrate.init_app(app, db)

    # ✅ IMPORT AFTER INIT (AVOIDS CIRCULAR BUGS)
    from app.routes import main_routes
    from app.api import api_routes
    app.secret_key = "hrms-super-secret-key"

    app.register_blueprint(main_routes)
    app.register_blueprint(api_routes, url_prefix="/api")

    return app
