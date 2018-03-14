import csv
import os
import re
import pickle

filepath = "C:\\Users\\Morrissd\\Documents\\Data\\Practice\\States\\"
# filepath = "C:\\Users\\Morrissd\\Documents\\Data\\USA\\"
PICKLE_FILE_PATH = "C:\\Users\\Morrissd\\Documents\\Data\\State_pickles\\"
STREET_NUMBER_INDEX = 2
STREET_NAME_INDEX = 3
UNIT_INDEX = 4
CITY_INDEX = 5
POSTCODE_INDEX = 8
STREET_TYPES = ["St", "Ave", "Rd", "Blvd", "Dr", "Cir", "Ct", "Hwy", "Ln", "Loop", "Pkwy", "Aly", "Way",
                "Street", "Avenue", "Road", "Boulevard", "Drive", "Circle", "Court", "Highway", "Lane",
                "Parkway", "Alley"]
UNKNOWN = "UNKNOWN"


class Address(object):
    def __init__(self):
        self.number = ""
        self.street_name = ""
        self.unit = ""
        self.postal_code = ""


def main():
    # store all addresses found for each city/state, those without determinable city go to UNKNOWN
    unknown_addresses = dict()

    for folder, subfolders, files in os.walk(filepath):
        state = folder.split("\\")[-1]

        if state:
            city_addresses = dict()  # {city: [Addresses]
            print(state)

            for filename in files:
                if filename.endswith(".csv"):
                    city_filename = get_city_name(filename)

                    with open(os.path.join(folder, filename), 'r') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')

                        # Skip the first line containing column headers
                        next(readCSV)

                        # Grab each address in file
                        for row in readCSV:
                            address = Address()

                            # Number
                            number = handle_number(row[STREET_NUMBER_INDEX])
                            if number:
                                address.number = number
                            else:
                                continue

                            # Street name
                            street_name = handle_street_name(row[STREET_NAME_INDEX])
                            if street_name:
                                address.street_name = street_name
                            else:
                                continue

                            # Unit
                            unit = handle_unit(row[UNIT_INDEX])
                            if unit:
                                address.unit = unit

                            # Postal code
                            postal_code = row[POSTCODE_INDEX]
                            address.postal_code = postal_code

                            # City name
                            city = handle_city_name(city_filename, row[CITY_INDEX])

                            # Add address
                            add_address(city_addresses, city, address)

            # Store addresses in file
            state_pickle_file = PICKLE_FILE_PATH + state + ".pickle"
            with open(state_pickle_file, 'wb') as file:
                pickle.dump(city_addresses, file, protocol=pickle.HIGHEST_PROTOCOL)


def get_city_name(filename):
    city = ""
    name = re.sub("\.csv", "", filename)

    if name != "statewide":
        name = name.replace("city_of_", "")

        chunks = name.split("_")
        city = chunks[0].capitalize()

        if len(chunks) > 1:
            for chunk in chunks[1:]:
                city += " " + chunk.capitalize()

    return city


def handle_number(street_number_field):
    number = ""

    if street_number_field and street_number_field.isdigit() and street_number_field != "0":
        number = street_number_field

    return number


def handle_street_name(street_name_field):
    street_name = ""

    # Make sure field has contents and don't bother processing it if the whole address is included (indicated by comma)
    if street_name_field and "," not in street_name_field:
        street_name_words = [word.capitalize() for word in street_name_field.split()]

        # Check for "St., Dr., Blvd., etc."
        for w in reversed(street_name_words):
            if w in STREET_TYPES:

                # If it has, add it
                street_name = " ".join(street_name_words)

                break

    return street_name


def handle_unit(unit_field):
    unit = ""

    if unit_field:
        grams = unit_field.split()

        # Use the field value if the last part is a number
        if grams[-1].isdigit():
            for gram in grams:
                unit += " " + gram.capitalize()

    return unit


def handle_city_name(city_filename, city_field):
    city = ""

    # If city is in "City" field
    if city_field and city_field.capitalize() != "Unincorporated":
        city_words = [word.capitalize() for word in city_field.split()]
        city = " ".join(city_words)

    # else, take city from filename
    elif city_filename != "statewide":
        city_words = [word.capitalize() for word in city_filename.split("_")]
        city = " ".join(city_words)

    return city


def add_address(city_addresses, city, address):
    if city:
        if city not in city_addresses:
            city_addresses[city] = []
        city_addresses[city].append(address)


if __name__ == '__main__':
    main()