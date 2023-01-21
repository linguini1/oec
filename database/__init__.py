# Contains utilities for loading items and saving items to a database
__author__ = "Matteo Golin"

# Imports
import csv
import os
from .facility import Facility

# Constants
FACILITY_DB: str = "facilities.csv"


# Helper functions
def load_facilities(filepath: str = f"{os.getcwd()}/{FACILITY_DB}") -> list[Facility]:

    """Returns a list of facility objects from the CSV file given by the filepath."""

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Unpack headers

        for row in reader:
            facility = Facility.from_csv_row(row)

    return Facility.instances
