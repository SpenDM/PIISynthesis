import re
import random
from Globals import *


def generate_age(bracket_contents):
    """Select a random value within the age window specified by the tag"""
    if bracket_contents == AGE_CHILD:
        synthetic_age = str(random.randrange(1, 10))
    elif bracket_contents == AGE_TEEN:
        synthetic_age = str(random.randrange(11, 19))
    elif bracket_contents == AGE_OVER_90:
        if random.random() < PROB_OVER_100:
            synthetic_age = str(random.randrange(100, MAX_AGE))
        else:
            synthetic_age = "9" + str(random.randint(0, 9))
    else:
        synthetic_age = generate_age_based_on_decade(bracket_contents)

    return synthetic_age


def generate_age_based_on_decade(bracket_contents):
    """Expecting bracket_contents to contain 'in 30s', else simply output the bracket contents"""
    has_decade = re.search("([2-8])", bracket_contents)
    if has_decade:
        decade = has_decade.group(1)
        year = random.randint(0, 9)
        synthetic_age = decade + str(year)
    else:
        synthetic_age = bracket_contents

    return synthetic_age


def generate_device():
    device_type = random.choice(DEVICE_TYPES)
    if device_type == SERIAL:
        synthetic_device = generate_serial()
    elif device_type == DOT_ID:
        synthetic_device = generate_alphanum()
    else:
        synthetic_device = generate_alphanum()
    return synthetic_device


def generate_serial():
    serial = ""
    length = random.randint(MIN_SERIAL_LEN, MAX_SERIAL_LEN)
    split_index = random.randint(1, length)

    # Add random sequential numbers
    for x in range(split_index):
        serial += random.choice(DIGITS)

    # Add random sequential letters
    for x in range(length - split_index):
        serial += random.choice(ALPHA_UPPER)

    return serial


def generate_alphanum():
    serial = ""
    length = random.randint(MIN_SERIAL_LEN, MAX_SERIAL_LEN)

    # Randomly add letters and digits
    for x in range(length):
        if random.random() < ID_DIGIT_PROB:
            serial += random.choice(DIGITS)
        else:
            serial += random.choice(ALPHA_UPPER)

    # Randomly add dash
    if random.random() < DASH_PROB:
        index = random.randint(1, length - 1)
        serial = serial[:index] + "-" + serial[index:]

    return serial


def generate_phone():
    number = ""

    separator_pattern = random.choice(PHONE_SEPARATOR_PATTERN_LIST)
    has_country_code, has_parentheses, separator_1, separator_2, separator_3 = PHONE_SEPARATORS_BY_PATTERN[separator_pattern]

    # Country code
    if has_country_code:
        number += "1"
        number += separator_1

    # Area code
    number += generate_area_code(has_parentheses)
    number += separator_2

    # The main seven digits
    number += generate_main_phone_digits(separator_3)

    return number


def generate_area_code(has_parentheses):
    number = ""
    area_code = ""

    for _ in range(PHONE_SECTION_1):
        area_code += str(random.randint(0, 9))

    if has_parentheses:
        number += "(" + area_code + ")"
    else:
        number += area_code

    return number


def generate_main_phone_digits(separator):
    number = ""

    for _ in range(PHONE_SECTION_2):
        number += str(random.randint(0, 9))

    number += separator

    for _ in range(PHONE_SECTION_3):
        number += str(random.randint(0, 9))

    return number
