# The dataclass representing the patient
__author__ = "Matteo Golin"

# Imports
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Self

# Constants


# Helper classes
class UnderlyingCondition(StrEnum):

    """Represents some underlying conditions a patient may have."""

    CAD: str = "cad"
    ARTHRITIS: str = "arthritis"
    IMMUNO_COMPROMISED: str = "immuno-compromised"
    LEUKEMIA: str = "leukemia"
    CANCER: str = "cancer"
    ALZHEIMERS: str = "alzheimers"
    DIABETES: str = "diabetes"
    HEART_ATTACK: str = "heart attack"
    TRAUMA: str = "trauma"
    ASTHMA: str = "asthma"


class Symptoms(StrEnum):

    """Represents some symptoms a patient may have."""

    DIARRHEA: str = "diarrhea"
    VOMIT: str = "vomit"
    FEVER_HIGH: str = "high fever"
    FEVER_LOW: str = "low fever"
    STOMACH_ACHE: str = "stomach ache"
    FATIGUE: str = "fatigue"
    NOSE_BLEED: str = "nose bleed"
    SHORTNESS_BREATH: str = "shortness of breath"
    WEIGHT_LOSS: str = "weight loss"


class Sex(StrEnum):

    """Contains the sex options available to a patient."""

    MALE: str = "male"
    FEMALE: str = "female"
    INTERSEX: str = "intersex"
    NO_ANSWER: str = "prefer not to answer"


# Class
@dataclass
class Patient:

    """Represents a patient using the matching system."""

    latitude: float
    longitude: float
    age: int
    underlying: list[UnderlyingCondition] = field(default_factory=list)
    symptoms: list[Symptoms] = field(default_factory=list)

    @classmethod
    def from_json(cls, json_packet: dict[str, Any]) -> Self:

        """Returns a Patient object instance populated using the provided JSON."""

        return cls(
            latitude=json_packet.get("latitude"),
            longitude=json_packet.get("longitude"),
            age=json_packet.get("age"),
            underlying=json_packet.get("underlying"),
            symptoms=json_packet.get("symptoms")
        )
