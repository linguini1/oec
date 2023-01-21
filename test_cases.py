# Runs each of the test cases from the debrief
__author__ = "Matteo Golin"

# Imports
from database import load_facilities, export_rankings_to_csv
from database.ranking import rank
from database.facility import Facility
from database.patient import Patient, Sex, UnderlyingCondition, Symptoms

# Constants

# Test cases
def case_1():

    patient = Patient(
        age=24,
        sex=Sex.FEMALE,
        underlying=[],
        symptoms=[Symptoms.BLUNT_TRAUMA],
        latitude=0,
        longitude=0
    )


# Main
def main():
    case_1()
    case_2()

if __name__ == '__main__':
    main()

