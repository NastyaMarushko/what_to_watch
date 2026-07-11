# what_to_watch/opinions_app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config

# Создаем экземпляры расширений БЕЗ передачи app
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Фабричная функция создания приложения."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация расширений с приложением
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация блюпринтов и команд происходит здесь же или через импорт ниже
    from .views import main_bp
    app.register_blueprint(main_bp)

    from .cli_commands import register_cli_commands
    register_cli_commands(app)

    from .error_handlers import register_error_handlers
    register_error_handlers(app)

    return app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run()
