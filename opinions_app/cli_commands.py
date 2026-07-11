# what_to_watch/opinions_app/cli_commands.py

import csv

import click

from . import db
from .models import Opinion


def register_cli_commands(app):
    @app.cli.command('load_opinions')
    def load_opinions_command():
        """Функция загрузки мнений в базу данных."""
        with open('opinions.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            counter = 0
            for row in reader:
                try:
                    opinion = Opinion(**row)
                    db.session.add(opinion)
                    db.session.commit()
                    counter += 1
                except Exception:
                    db.session.rollback()
        click.echo(f'Загружено мнений: {counter}')
