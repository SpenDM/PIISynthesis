import random
from Globals import *


def generate_name(preceding_word, bracket_contents, stored_values, given_names, surnames):
    synthetic_name = ""

    tags = bracket_contents.split()
    name_types = determine_name_types(tags, preceding_word)

    print(tags)
    print(name_types)

    for tag, type in zip(tags, name_types):

        # If tag has been seen before, use the name generated previously
        if tag in stored_values:
            name = stored_values[tag]

        # Else generate a new name based on determined name type
        else:
            if type == MIDDLE_INITIAL:
                name = random.sample(MIDDLE_INITIAL_LIST, 1)[0] + "."
            elif type == SURNAME:
                name = generate_surname(surnames)
            else:
                name = generate_first_name(given_names)

            # save the name used for the specific tag in case it occurs again
            stored_values[tag] = name

        # Add generated name to the full name to replace the tag with
        if synthetic_name:
            synthetic_name += " "

        synthetic_name += name

    return synthetic_name


def determine_name_types(tags, preceding_word):
    name_types = []
    end_position = len(tags) - 1

    for position, tag in enumerate(tags):
        if is_middle_initial(tag):
            name_types.append(MIDDLE_INITIAL)
        elif position == end_position:
            name_types.append(SURNAME)
        else:
            name_types.append(GIVEN_NAME)

    return name_types


def is_middle_initial(tag):
    is_initial = False

    if len(tag) == 2:
        if tag[-1] == ".":
            is_initial = True

    return is_initial


def generate_first_name(first_names):
    prob = random.random()
    if prob < COMMON_FIRST_NAME_PROB:
        first_name = random.sample(first_names[:COMMON_FIRST_NAME_INDEX], 1)[0]
    elif prob < RARE_FIRST_NAME_PROB:
        first_name = random.sample(first_names[RARE_FIRST_NAME_INDEX:], 1)[0]
    else:
        first_name = random.sample(first_names[COMMON_FIRST_NAME_INDEX:RARE_FIRST_NAME_INDEX], 1)[0]
    return first_name


def generate_surname(surnames):
    prob = random.random()
    if prob < COMMON_SURNAME_PROB:
        surname = random.sample(surnames[:COMMON_SURNAME_INDEX], 1)[0]
    elif prob < RARE_SURNAME_PROB:
        surname = random.sample(surnames[RARE_SURNAME_INDEX:], 1)[0]
    else:
        surname = random.sample(surnames[COMMON_SURNAME_INDEX:RARE_SURNAME_INDEX], 1)[0]
    return surname


def generate_email(given_names, surnames):
    email = generate_email_username(given_names, surnames)
    email += "@"
    email += generate_email_domain()
    email = email.rstrip("\n")
    return email


def generate_email_username(given_names, surnames):
    username = ""

    # generate word-based portion of email
    if random.random() < NAME_EMAIL_PROB:
        username += generate_email_name(given_names, surnames)
    else:
        username += generate_email_random()

    # generate number-based portion of email
    # TODO

    return username


def generate_email_name(given_names, surnames):
    name_parts = generate_email_name_parts()
    punctuation_type = generate_email_punctuation_type()
    names = []

    # generate random names for each name type
    for name_part in name_parts:

        if name_part == MIDDLE_INITIAL:
            name = random.sample(MIDDLE_INITIAL_LIST, 1)[0]
            names.append(name)
        elif name_part == SURNAME:
            name = generate_surname(surnames)
            names.append(name)
        else:
            name = generate_first_name(given_names)
            names.append(name)

    # join names with random punctuation
    username = punctuation_type.join(names)
    username = username.lower()

    return username


def generate_email_name_parts():
    name_parts = []
    last_name_parts = []
    name_part_initials = []
    last_name_initial = False

    # First name
    if random.random() < EMAIL_HAS_FIRST_NAME_PROB:
        if random.random() < EMAIL_INITAL_PROB:
            name_parts.append(MIDDLE_INITIAL)
            name_part_initials.append(True)
        else:
            name_parts.append(GIVEN_NAME)
            name_part_initials.append(False)

    # Middle name
    if random.random() < EMAIL_HAS_MIDDLE_NAME_PROB:
        if random.random() < EMAIL_INITAL_PROB:
            name_parts.append(MIDDLE_INITIAL)
            name_part_initials.append(True)
        else:
            name_parts.append(GIVEN_NAME)
            name_part_initials.append(False)

    # Last names
    if not name_parts:
        # First surname
        last_name_parts.append(SURNAME)

        # Second surname
        if random.random() < EMAIL_HAS_DOUBLE_LAST_NAME_PROB:
            last_name_parts.append(SURNAME)

    elif random.random() < EMAIL_HAS_SINGLE_LAST_NAME_PROB:
        # First surname
        # If there is a non-initial first/middle name and lands within chance of having an abbreviation
        if (False in name_part_initials) and (random.random() < EMAIL_LAST_NAME_INITIAL_PROB):
            name_parts.append(MIDDLE_INITIAL)
            last_name_initial = True
        else:
            last_name_parts.append(SURNAME)

        # Second surname
        if random.random() < EMAIL_HAS_DOUBLE_LAST_NAME_PROB:
            if last_name_initial:
                last_name_parts.append(MIDDLE_INITIAL)
            else:
                last_name_parts.append(SURNAME)

            # append with first surname
            if random.random() < EMAIL_SURNAMES_JOINED_HYPHEN:
                last_name = "-".join(last_name_parts)
                last_name_parts = [last_name]
            elif random.random() < EMAIL_SURNAMES_JOINED_NO_PUNC:
                last_name = "".join(last_name_parts)
                last_name_parts = [last_name]

    # Surnames before or after first names
    if random.random() < EMAIL_FIRST_NAME_BEFORE_LAST_PROB:
        name_parts.extend(last_name_parts)
    else:
        for name in last_name_parts:
            name_parts.insert(0, name)

    return name_parts


def generate_email_punctuation_type():
    r = random.random()
    has_punc = r < EMAIL_HAS_PUNCTUATION_PROB
    punc_type = ""
    if has_punc:
        punc_type = "."
        if random.random() < EMAIL_HAS_HYPHENS_PROB:
            punc_type = "-"
    return punc_type


def generate_email_random():
    username = ""

    length = random.randint(MIN_EMAIL_LENGTH, MAX_EMAIL_LENGTH)
    for _ in range(length):
        username += random.choice(ALPHA_LOWER)

    return username


def generate_email_domain():
    r = random.random()

    if r < COMMON_EMAIL_PROB:
        domain = random.choice(COMMON_EMAIL_DOMAINS)
    elif r < MIDTIER_EMAIL_PROB:
        domain = random.choice(MIDTIER_EMAIL_DOMAINS)
    elif r < UNIV_EMAIL_PROB:
        domain = random.choice(UNIV_EMAILS)
    else:
        domain = random.choice(COMMON_NON_US_EMAILS)

    return domain
