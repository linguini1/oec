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

    rankings = rank(patient)[:11]
    export_rankings_to_csv(rankings)


def case_2():

    patient = Patient(
        age=64,
        sex=Sex.MALE,
        underlying=[UnderlyingCondition.CAD, UnderlyingCondition.ARTHRITIS, UnderlyingCondition.IMMUNO_COMPROMISED],
        symptoms=[Symptoms.DIARRHEA, Symptoms.VOMIT, Symptoms.STOMACH_ACHE, Symptoms.FEVER_LOW],
        latitude=0,
        longitude=0
    )

    rankings = rank(patient)[:11]
    export_rankings_to_csv(rankings)


def case_3():

    patient = Patient(
        age=33,
        sex=Sex.MALE,
        underlying=[UnderlyingCondition.LEUKEMIA],
        symptoms=[Symptoms.FEVER_HIGH, Symptoms.NOSE_BLEED, Symptoms.WEIGHT_LOSS, Symptoms.SHORTNESS_BREATH],
        latitude=0,
        longitude=0
    )

    rankings = rank(patient)[:11]
    export_rankings_to_csv(rankings)


def case_4():
    patient = Patient(
        age=15,
        sex=Sex.MALE,
        underlying=[],
        symptoms=[Symptoms.BLUNT_TRAUMA],
        latitude=0,
        longitude=0
    )

    rankings = rank(patient)[:11]
    export_rankings_to_csv(rankings)


def case_5():
    patient = Patient(
        age=20,
        sex=Sex.FEMALE,
        underlying=[UnderlyingCondition.ASTHMA],
        symptoms=[Symptoms.FEVER_LOW, Symptoms.SHORTNESS_BREATH, Symptoms.BLUNT_TRAUMA],
        latitude=0,
        longitude=0
    )

    rankings = rank(patient)[:11]
    export_rankings_to_csv(rankings)


def case_6():
    patient = Patient(
        age=3,
        sex=Sex.MALE,
        underlying=[],
        symptoms=[Symptoms.DIARRHEA, Symptoms.VOMIT, Symptoms.STOMACH_ACHE],
        latitude=0,
        longitude=0
    )

    rankings = rank(patient)[:11]
    export_rankings_to_csv(rankings)


# Main
def main():

    # Run through test cases
    load_facilities()
    case_1()
    case_2()
    case_3()
    case_4()
    case_5()
    case_6()


if __name__ == '__main__':
    main()

