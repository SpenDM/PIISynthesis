import sys
import random
from Globals import *


class Address(object):
    def __init__(self):
        self.number = ""
        self.street_name = ""
        self.unit = ""
        self.postal_code = ""


def generate_street_address(addresses, line, tag_name_end, across_tag_info, states):
    state = determine_state(line, tag_name_end, states, addresses)
    generated_address, failed = generate_address_from_state(state, addresses, across_tag_info)
    return generated_address, failed


def generate_place(addresses, line, tag_name_end, across_tag_info, states):
    failed = False

    # if an address has already been established, street address from it
    if PLACE in across_tag_info:
        generated_place = across_tag_info[PLACE]
        del across_tag_info[PLACE]
    else:
        generated_place, failed = determine_state_and_generate_place(line, tag_name_end, states, addresses)

    return generated_place, failed


def determine_state_and_generate_place(line, tag_name_end, states, addresses):
    city = ""
    failed = False

    state = determine_state(line, tag_name_end, states, addresses)

    try:
        cities = [city for city, addrs in addresses[state].items()]
        city = random.choice(cities)
    except:
        sys.stderr.write("(place) Failed to find cities for " + state + "in " + ADDRESS_FILE + "\n")
        failed = True

    return city, failed


def determine_state(line, tag_name_end, states, addresses):
    # Check for state abbreviations in the line after the tag
    state = ""
    found_state = False
    for word in line[tag_name_end:].split():
        if word in states:
            state = word
            found_state = True
            print("\nFound state " + state)
            break

    # Check for full state names in the line after the tag
    if not found_state:
        for state_abbr, state_full_name in states.items():
            if state_full_name in line[tag_name_end:]:
                state = state_abbr

                found_state = True
                print("\nFound state " + state_full_name)
                break

    # Verify state is in address data
    state = state.lower()
    state = verify_state_is_useable(state, addresses, found_state)
    return state


def generate_address_from_state(state, addresses, across_tag_info):
    city, failed = generate_and_add_city(addresses, state, across_tag_info)
    generated_address, failed = generate_address_from_database(city, addresses, state, across_tag_info)
    return generated_address, failed


def verify_state_is_useable(state_abbr, addresses, found_state):
    if not found_state or state_abbr not in addresses:
        state_abbrs = [state for state, state_info in addresses.items()]

        try:
            state_abbr = random.choice(state_abbrs)
            print("\nGenerated state " + state_abbr)
        except IndexError:
            sys.stderr.write("Failed to find states in " + ADDRESS_FILE + "\n")
    return state_abbr


def generate_and_add_city(addresses, state, across_tag_info):
    city = ""
    failed = False

    try:
        cities = [city for city, addrs in addresses[state].items()]
        city = random.choice(cities)
        across_tag_info[PLACE] = city
        print("Generated city from state: " + city + ", " + state)
    except:
        sys.stderr.write("(city from address) Failed to find cities in " + state + " in " + ADDRESS_FILE + "\n")
        failed = True

    return city, failed


def generate_address_from_database(city, addresses, state_abbr, across_tag_info):
    generated_address = ""
    failed = False

    try:
        # Choose random address from state/city
        address_objects = addresses[state_abbr][city]
        address_obj = random.choice(address_objects)

        generated_address = compile_street_address(address_obj)

        # add zip to across_tag_info
        across_tag_info[ZIP] = address_obj.postal_code

        print("Generated full address: " + generated_address + ", " + city + ", " + state_abbr + " " + address_obj.postal_code)

    except:
        sys.stderr.write("(street address) Failed to find full address information in " + " " + city + ", " + state_abbr + " in "+ ADDRESS_FILE + "\n")
        failed = True

    return generated_address, failed


def compile_street_address(address_obj):
    street_address = address_obj.number + " " + address_obj.street_name
    if address_obj.unit:
        street_address += ", " + address_obj.unit
    return street_address


def generate_zip(across_tag_info):
    zip_code = ""

    # if an address has already been established, use zip from it
    if ZIP in across_tag_info:
        zip_code = across_tag_info[ZIP]
        print("Used zip from generated address: " + zip_code)
    else:
        # generate random zip
        for x in range(ZIP_LENGTH):
            zip_code += str(random.randint(0, 9))
        print("Generated random zip: " + zip_code)

    return zip_code
