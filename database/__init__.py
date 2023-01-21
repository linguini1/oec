# Contains utilities for loading items and saving items to a database
__author__ = "Matteo Golin"

# Imports
import csv
import os
from .facility import Facility

# Constants
FACILITY_DB: str = "facilities.csv"
RANKING_LIST: str = "[The Architects]_-_OEC_2023_Programming_Submission_Output.csv"


# Helper functions
def load_facilities(filepath: str = f"{os.getcwd()}/{FACILITY_DB}") -> list[Facility]:

    """Returns a list of facility objects from the CSV file given by the filepath."""

    facilities: list[Facility] = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Unpack headers

        for row in reader:
            facilities.append(
                Facility.from_csv_row(row)
            )

    return facilities


def export_rankings_to_csv(rankings: list[Facility], filepath: str = f"{os.getcwd()}/{RANKING_LIST}") -> None:

    """Save the facility ranking list for a query to a CSV file given by the filepath."""

    headers = dict(rankings[0]).keys()  # Get headers

    with open(filepath, 'a', newline="", encoding="utf-8") as file:

        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers

        for facil in rankings:
            writer.writerow(facil.to_csv_row())

