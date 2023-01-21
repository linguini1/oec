# Contains the API endpoints and page routes
__author__ = "Matteo Golin"

# Imports
from flask import Flask, render_template, request
from flask_cors import CORS
from database.patient import UnderlyingCondition, Symptoms, Sex, Patient
from database.ranking import rank

# Constants
STATIC_FOLDER: str = ".\\frontend\\build\\static"
TEMPLATE_FOLDER: str = ".\\frontend\\build"
API_ROUTE: str = "/api"

# Flask application
app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
cors = CORS(app)
app.config['SERVER_NAME'] = 'localhost:8000'
app.config['CORS_HEADERS'] = 'Content-Type'


# Webpage route
@app.route("/", methods=["GET"])
def index():
    """The homepage of the website where HTML will be served. React Router handles URLS beyond this."""

    return render_template("index.html")


# API routes
@app.route(f"{API_ROUTE}/symptoms", methods=["GET"])
def symptoms():
    """Returns the available symptoms as JSON."""

    return list(Symptoms)


@app.route(f"{API_ROUTE}/underlying", methods=["GET"])
def underlying():
    """Returns the available underlying conditions as JSON."""

    return list(UnderlyingCondition)


@app.route(f"{API_ROUTE}/sex", methods=["GET"])
def sex():
    """Returns the sex selection options as JSON."""

    return list(Sex)


@app.route(f"{API_ROUTE}/patient", methods=["POST"])
def submit_patient():
    """Submits the patient data for the search to be performed."""

    patient = Patient.from_json(request.json())
    return rank(patient)[:11]
