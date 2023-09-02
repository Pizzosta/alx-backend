#!/usr/bin/env python3
"""simple flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Returns to the index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
