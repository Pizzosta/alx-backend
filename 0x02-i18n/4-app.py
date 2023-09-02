#!/usr/bin/env python3
"""simple flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration for babel Internationalization (i18n)

    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone for Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching supporting language otherwise
    default is english

    Returns:
        str: The selected language/locale.
    """
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles Route to the index page

    Returns:
        str: The rendered HTML content for the index page.
    """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    return render_template(
        '3-index.html', home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run()
