from flask import Flask, session, request, render_template
from apps.common import bp as common_bp
from apps import bp as main_bp
import config
from exts import db
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(common_bp)
    app.register_blueprint(main_bp)

    db.init_app(app)
    CSRFProtect(app)  # csrf保护
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
