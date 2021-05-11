import pickle
from Packages.NumericTagReplacerMethods import *
from Packages.GeographicalTagReplacerMethods import *
from Packages.NameTagReplacerMethods import *


class TagReplace(object):
    def __init__(self):
        self.stored_values = {}
        self.given_names = {}
        self.surnames = {}
        self.titles = {}
        self.addresses = {}             # {state: {city: [Address]}}
        self.addresses_valid = True
        self.states = {}

        # given names
        with open(GIVEN_NAME_FILE, "r") as file:
            self.given_names = [name.rstrip('\n') for name in file.readlines()]

        # surnames
        with open(SURNAME_FILE, "r") as file:
            self.surnames = [name.rstrip('\n') for name in file.readlines()]

        # titles
        with open(TITLE_FILE, "r") as file:
            self.titles = [name.rstrip('\n') for name in file.readlines()]

        # addresses
        # print("read pickle")
        # with open(ADDRESS_FILE, 'rb') as file:
        #     self.addresses = pickle.load(file)
        # print("done")

        # states
        with open(STATES_FILE, 'r') as file:
            for line in file.readlines():
                print(line)
                print(line.split("\t"))
                full_name, abbreviation = [gram.rstrip("\n") for gram in line.split("\t")]
                self.states[abbreviation] = full_name

        # TODO -- self.addresses_valid = check_addresses(self.addresses, self.states)

    def replace_ADDR(self, line, star_start, tag_name_end, across_tag_info):
        replaced_line = line
        offset = 0

        # generated_addr, failed = generate_street_address(self.addresses, line, tag_name_end, across_tag_info, self.states)
        # if failed:
        #     replaced_line = line
        #     offset = 0
        # else:
        #     replaced_line, offset = replace(line, generated_addr, star_start, tag_name_end)

        return replaced_line, offset

    def replace_AGE(self, line, star_start, tag_name_end, across_tag_info):
        has_brackets, bracket_contents, bracket_end = process_brackets(line, tag_name_end)
        synthetic_age = generate_age(bracket_contents)
        replaced_line, offset = replace(line, synthetic_age, star_start, bracket_end)
        return replaced_line, offset

    def replace_DATE(self, line, star_start, tag_name_end, across_tag_info):
        """Simply use date that DEID has already provided"""
        has_brackets, bracket_contents, bracket_end = process_brackets(line, tag_name_end)
        replaced_line, offset = replace(line, bracket_contents, star_start, bracket_end)
        return replaced_line, offset

    def replace_DEVICE(self, line, star_start, tag_name_end, across_tag_info):
        generated_device = generate_device()
        replaced_line, offset = replace(line, generated_device, star_start, tag_name_end)
        return replaced_line, offset

    def replace_EMAIL(self, line, star_start, tag_name_end, across_tag_info):
        generated_email = generate_email(self.given_names, self.surnames)
        replaced_line, offset = replace(line, generated_email, star_start, tag_name_end)
        return replaced_line, offset

    def replace_ID(self, line, star_start, tag_name_end, across_tag_info):
        previous_context = line[:star_start]
        offset = 0
        return line, offset

    def replace_INST(self, line, star_start, tag_name_end, across_tag_info):
        offset = 0
        return line, offset

    def replace_NAME(self, line, star_start, tag_name_end, across_tag_info):
        has_brackets, bracket_contents, bracket_end = process_brackets(line, tag_name_end)
        preceding_word = find_preceding_word(line, star_start)
        synthetic_name = generate_name(preceding_word, bracket_contents, self.stored_values, self.given_names, self.surnames)
        replaced_line, offset = replace(line, synthetic_name, star_start, bracket_end)
        return replaced_line, offset

    def replace_PATH(self, line, star_start, tag_name_end, across_tag_info):
        offset = 0
        return line, offset

    def replace_PHONE(self, line, star_start, tag_name_end, across_tag_info):
        synthetic_phone = generate_phone()
        replaced_line, offset = replace(line, synthetic_phone, star_start, tag_name_end)
        return replaced_line, offset

    def replace_PLACE(self, line, star_start, tag_name_end, across_tag_info):
        generated_place, failed = generate_place(self.addresses, line, tag_name_end, across_tag_info, self.states)
        if failed:
            replaced_line = line
            offset = 0
        else:
            replaced_line, offset = replace(line, generated_place, star_start, tag_name_end)
        return replaced_line, offset

    def replace_WEB(self, line, star_start, tag_name_end, across_tag_info):
        offset = 0
        return line, offset

    def replace_ZIP(self, line, star_start, tag_name_end, across_tag_info):
        synthetic_zip = generate_zip(across_tag_info)
        replaced_line, offset = replace(line, synthetic_zip, star_start, tag_name_end)
        return replaced_line, offset


def check_addresses(addresses, states):
    is_valid = check_address_is_dict(addresses)
    valid_addresses = {}

    # Check content
    state_abbrs = [state.lower() for state, full_name in states.items()]

    if addresses:
        for state, state_info in addresses.items():
            if state in state_abbrs:

                if type(state_info) is dict:
                    pass
                else:
                    sys.stderr.write("Bad format in " + state + " in " + ADDRESS_FILE + "\n")
                    sys.stderr.write(state + " city info: " + state_info + "\n")
    else:
        is_valid = False
    return valid_addresses, is_valid


def check_address_is_dict(addresses):
    is_valid = True
    if type(addresses) is not dict:
        sys.stderr.write("Did not find expected content in " + ADDRESS_FILE)
        addresses = {}
        is_valid = False
    return is_valid


def replace(line, value, replacement_start, replacement_end):
    replaced_line = line[:replacement_start] + value + line[replacement_end:]
    new_offset = len(replaced_line) - len(line)
    return replaced_line, new_offset


def process_brackets(line, bracket_start):
    contents = ""
    brackets_end = 0

    has_brackets = re.match("\[(.*?)\]", line[bracket_start:])
    if has_brackets:
        brackets_end = bracket_start + has_brackets.span()[1]
        contents = has_brackets.group(1)

    return has_brackets, contents, brackets_end


def find_preceding_word(line, star_start):
    preceding_word = ""
    preceding_line = line[:star_start]

    if preceding_line:
        preceding_word = line[:star_start].split()[-1]
    return preceding_word


