# Contains the facility dataclass
__author__ = "Matteo Golin"

# Imports
from dataclasses import dataclass
from enum import StrEnum
import time
from typing import Self

# Constants
STR_TO_BOOL = {
    "yes": True,
    "no": False
}


# Helper class
class FacilityType(StrEnum):

    """Contains the different types that facilities can have."""

    HOSPITAL: str = "hospital"
    CLINIC: str = "clinic"
    PHARMACY: str = "pharmacy"
    LTC: str = "ltc"
    PEDIATRICS: str = "pediatrics"
    ADULT_HOSPITAL: str = "adult hospital"
    SPECIALIZED_CARE: str = "specialized care"


# Dataclass
@dataclass
class Facility:

    """Represents a facility available to a user."""

    id: int
    name: str
    type: list[FacilityType]
    latitude: float
    longitude: float
    opening: time.time
    closing: time.time
    icu: bool
    ccu: bool
    vascular: bool
    trauma: bool
    capacity: str
    contact: str

    def from_csv_row(self, csv_row: list[str]) -> Self:

        """Returns a Facility object from a CSV row."""


