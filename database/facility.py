# Contains the facility dataclass
__author__ = "Matteo Golin"

# Imports
from dataclasses import dataclass
from enum import StrEnum
import datetime as dt
from typing import Self, ClassVar, Any

# Constants
STR_TO_BOOL = {
    "yes": True,
    "no": False
}
TIME_FORMAT: str = "%H:%M"


# Helper classes
class FacilityType(StrEnum):

    """Contains the different types that facilities can have."""

    HOSPITAL: str = "hospital"
    CLINIC: str = "clinic"
    PHARMACY: str = "pharmacy"
    LTC: str = "ltc"
    PEDIATRICS: str = "pediatrics"
    ADULT_HOSPITAL: str = "adult hospital"
    SPECIALIZED_CARE: str = "specialized care"


class CapacityType(StrEnum):

    """Contains the different capacity types that a facility may have."""
    A: str = "a"
    B: str = "b"
    C: str = "c"
    N: str = "n"


# Helper functions
def parse_facility_type(type_string: str) -> list[FacilityType]:

    """Parses a list of string facility types into FacilityType types."""

    fac_types: list[FacilityType] = []
    fac_str_types = type_string.strip().lower().split(", ")
    for fac_type in fac_str_types:
        fac_types.append(FacilityType(fac_type))

    return fac_types


def time_from_string(time_str: str) -> dt.time:

    """Returns a time object from a 24hr string following the %H:%M."""

    return dt.datetime.strptime(time_str, TIME_FORMAT).time()


# Dataclass
@dataclass
class Facility:

    """Represents a facility available to a user. All facilities have ERs."""

    instances: ClassVar[list[Self]] = []

    id_: int
    name: str
    type_: list[FacilityType]
    latitude: float
    longitude: float
    opening: dt.time
    closing: dt.time
    icu: bool
    ccu: bool
    vascular: bool
    trauma: bool
    capacity: str
    contact: str

    def __post_init__(self) -> None:
        """Commits the instance to the running list of instances."""
        self.instances.append(self)

    @classmethod
    def from_csv_row(cls, csv_row: list[str]) -> Self:

        """Returns a Facility object from a CSV row."""

        # Note CSV indexing is currently naive and not based on headers
        return cls(
            id_=int(csv_row[0]),
            name=csv_row[1],
            type_=parse_facility_type(csv_row[2]),
            latitude=float(csv_row[3]),
            longitude=float(csv_row[4]),
            opening=time_from_string(csv_row[5]),
            closing=time_from_string(csv_row[6]),
            icu=STR_TO_BOOL[csv_row[7].lower()],
            ccu=STR_TO_BOOL[csv_row[8].lower()],
            vascular=STR_TO_BOOL[csv_row[9].lower()],
            trauma=STR_TO_BOOL[csv_row[10].lower()],
            capacity=CapacityType(csv_row[11].lower()),
            contact=csv_row[12]
        )

    def __iter__(self):
        yield "id", self.id_
        yield "name", self.name
        yield "type", self.type_
        yield "latitude", self.latitude
        yield "longitude", self.longitude
        yield "opening", self.opening
        yield "closing", self.closing
        yield "icu", self.icu
        yield "ccu", self.ccu
        yield "vascular", self.vascular
        yield "trauma", self.trauma
        yield "capacity", self.capacity
        yield "contact", self.contact

    def to_csv_row(self) -> list[Any]:

        """Returns the Facility object as a CSV row."""

        return list(dict(self).values())
