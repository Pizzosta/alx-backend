#!/usr/bin/env python3
"""
This Flask application serves as the welcome page for Holberton School.
It provides a simple webpage with a greeting message.

Features:
- Root URL ('/') displays a welcome message.
- Supports internationalization for English and French.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz import UnknownTimeZoneError


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get the user based on the login_as URL parameter.

    Returns:
        dict/None: A user dictionary if a valid user is found, None otherwise.
    """
    user_id = request.args.get("login_as")
    if user_id:
        user = users.get(int(user_id))
        return user
    return None


@app.before_request
def before_request():
    """
    Executed before handling any request.
    Sets the user as a global variable in flask.g.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching supporting language otherwise
    default is english

    Returns:
        str: The selected language/locale.
    """
    # Check if a user is logged in and their preferred locale is supported
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # Check if the locale is specified in URL parameters
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check the request headers for the best match with supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Select and return the best time zone based on
    URL parameters, user settings, or default to UTC.

    Returns:
        pytz.timezone: The selected time zone.
    """
    # Check if the time zone is specified in URL parameters
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            return pytz.timezone(url_timezone)
        except UnknownTimeZoneError:
            pass

    # Check if a user is logged in and their preferred time zone is set
    if g.user and g.user['timezone']:
        try:
            return pytz.timezone(g.user['timezone'])
        except UnknownTimeZoneError:
            pass

    # Default to UTC if no valid time zone is found
    return pytz.timezone('UTC')


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles Route to the index page

    Returns:
        str: The rendered HTML content for the index page.
    """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    logged_in_as = _("You are logged in as %(username)s.")
    not_logged_in = _("You are not logged in.")
    return render_template(
        '7-index.html', home_title=home_title, home_header=home_header,
        logged_in_as=logged_in_as, not_logged_in=not_logged_in)


if __name__ == "__main__":
    app.run()
