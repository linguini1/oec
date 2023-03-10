# Backend API for the hospital matcher
__author__ = "Matteo Golin"

# Imports
from database import load_facilities
from routes import app

# Constants


if __name__ == '__main__':
    facilities = load_facilities()  # Load facilities before api is available
    app.run(port=8000)
