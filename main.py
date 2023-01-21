# Backend API for the hospital matcher
__author__ = "Matteo Golin"

# Imports
from database import load_facilities

# Constants


# Main
def main():
    facils = load_facilities()
    print(facils[0])


if __name__ == '__main__':
    main()
