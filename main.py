# Backend API for the hospital matcher
__author__ = "Matteo Golin"

# Imports
from database import load_facilities
from flask import Flask

# Constants


# App creation
app = Flask(__name__)


# API routes


if __name__ == '__main__':
    facilities = load_facilities()  # Load facilities before api is available
    app.run(debug=True)  # TODO remove debug for submission
