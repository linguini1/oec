# Implements the ranking system for matching a patient to a hospital
__author__ = "Matteo Golin"

# Imports
from math import acos, sin, cos, degrees, asin, sqrt
from database.facility import Facility
from database.patient import Patient

# Constants
EARTH_RADIUS_KM: int = 6371


# Helpers
def distance_from_lat_lon_km(lat1: float, long1: float, lat2: float, long2: float) -> float:

    """
    Returns the distance between two regions in km given their latitude and longitude.
    Solution from: https://www.omnicalculator.com/other/latitude-longitude-distance#:~:text=The%20distance%20between%20any%20two%20adjacent%20latitudes%20is%20approximately%2069,and%20meet%20at%20the%20poles.
    """

    # Convert to degrees
    lat1 = degrees(lat1)
    lat2 = degrees(lat2)
    long1 = degrees(long1)
    long2 = degrees(long2)

    sin_squared_lat = (sin(lat2 - lat1) ** 2) / 2
    sin_squared_long = (sin(long2 - long1) ** 2) / 2

    return 2 * EARTH_RADIUS_KM * asin(sqrt(sin_squared_lat)) + cos(lat1) * cos(lat2) * sin_squared_long


if __name__ == '__main__':
    dist = distance_from_lat_lon_km(
        43.747,
        -79.744,
        3.556,
        -80.252
    )
    print(dist)
