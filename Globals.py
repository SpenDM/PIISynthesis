import string

# General Files
DATA = "Data/"

# Tags
NAME = "NAME"
PLACE = "PLACE"
INST = "INSTITUTION"
ADDR = "STREET-ADDRESS"
ZIP = "ZIP-CODE"
DATE = "DATE"
AGE = "AGE"
PHONE = "PHONE"
EMAIL = "EMAIL"
ID = "ID-NUM"
DEVICE = "DEVICE-ID"
WEB = "WEB-LOC"
PATH = "PATH-NUMBER"
TAGS = {NAME, PLACE, INST, ADDR, ZIP, DATE, AGE, PHONE, EMAIL, ID, DEVICE, WEB, PATH}
BRACKET_TAGS = {NAME, AGE, DATE}

TAG_MARKER = "**"
REPLACE_METHOD_NAME = "replace_"

# -- Get mapping of tag text to tag variable name
# NOTE: Each tag here must have a corresponding replace_XXX method in Packages/TagReplacer.py
TAG_VARIABLES = {NAME: "NAME",
                PLACE: "PLACE",
                INST: "INST",
                ADDR: "ADDR",
                ZIP: "ZIP",
                DATE: "DATE",
                AGE: "AGE",
                PHONE: "PHONE",
                EMAIL: "EMAIL",
                ID: "ID",
                DEVICE: "DEVICE",
                WEB: "WEB",
                PATH: "PATH"}


# AGE
AGE_CHILD = "birth-12"
AGE_TEEN = "in teens"
AGE_OVER_90 = "90+"
PROB_OVER_100 = 0.03
MAX_AGE = 120


# DEVICE
DOT_ID = "DOT_ID"
SERIAL = "SERIAL"
ALPHANUM_ID = "ALPHANUM_ID"
DEVICE_TYPES = [DOT_ID, SERIAL, ALPHANUM_ID]

MIN_SERIAL_LEN = 6
MAX_SERIAL_LEN = 12
ID_DIGIT_PROB = .7
DASH_PROB = .3

ALPHA_UPPER = list(string.ascii_uppercase)
ALPHA_LOWER = list(string.ascii_lowercase)
DIGITS = list(string.digits)
ALPHANUM = list(set().union(ALPHA_UPPER, DIGITS))


# EMAIL
univ_email_file = DATA + "university_domains.txt"
with open(univ_email_file, "r") as file:
    UNIV_EMAILS = file.readlines()

COMMON_EMAIL_PROB = 0.65
MIDTIER_EMAIL_PROB = COMMON_EMAIL_PROB + 0.05
UNIV_EMAIL_PROB = MIDTIER_EMAIL_PROB + 0.3

COMMON_EMAIL_DOMAINS = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "comcast.net", "msn.com", "aol.com"]
MIDTIER_EMAIL_DOMAINS = ["roadrunner.com", "mail.com", "verizon.net",  "att.net", "live.com", "sbcglobal.net", "optimum.net"]
COMMON_NON_US_EMAILS = ["bellsouth.net", "charter.net", "cox.net", "earthlink.net", "juno.com",
  "btinternet.com", "virginmedia.com", "blueyonder.co.uk", "freeserve.co.uk", "live.co.uk",
  "ntlworld.com", "o2.co.uk", "orange.net", "sky.com", "talktalk.co.uk", "tiscali.co.uk",
  "virgin.net", "wanadoo.co.uk", "bt.com", "yahoo.co.uk", "hotmail.co.uk", "facebook.com", "mac.com",
  "sina.com", "qq.com", "naver.com", "hanmail.net", "daum.net", "yahoo.co.jp", "yahoo.co.kr", "yahoo.co.id", "yahoo.co.in", "yahoo.com.sg", "yahoo.com.ph",
  "hotmail.fr", "live.fr", "laposte.net", "yahoo.fr", "wanadoo.fr", "orange.fr", "gmx.fr", "sfr.fr", "neuf.fr", "free.fr",
  "gmx.de", "hotmail.de", "live.de", "online.de", "t-online.de", "web.de", "yahoo.de",
  "mail.ru", "rambler.ru", "yandex.ru", "ya.ru", "list.ru",
  "hotmail.be", "live.be", "skynet.be", "voo.be", "tvcablenet.be", "telenet.be",
  "hotmail.com.ar", "live.com.ar", "yahoo.com.ar", "fibertel.com.ar", "speedy.com.ar", "arnet.com.ar",
  "yahoo.com.mx", "live.com.mx", "hotmail.es", "live.com", "hotmail.com.mx", "prodigy.net.mx",
  "yahoo.com.br", "hotmail.com.br", "outlook.com.br", "uol.com.br", "bol.com.br", "terra.com.br", "ig.com.br", "itelefonica.com.br", "r7.com", "zipmail.com.br", "globo.com", "globomail.com", "oi.com.br"]

NAME_EMAIL_PROB = 1
EMAIL_NUMBER_PROB = 0.35
MIN_EMAIL_LENGTH = 3
MAX_EMAIL_LENGTH = 16

EMAIL_HAS_FIRST_NAME_PROB = 0.8
EMAIL_HAS_MIDDLE_NAME_PROB = 0.2
EMAIL_INITAL_PROB = 0.5
EMAIL_LAST_NAME_INITIAL_PROB = 0.2
EMAIL_HAS_SINGLE_LAST_NAME_PROB = 0.9
EMAIL_HAS_DOUBLE_LAST_NAME_PROB = 0.2
EMAIL_FIRST_NAME_BEFORE_LAST_PROB = 0.8
EMAIL_HAS_PUNCTUATION_PROB = 0.3
EMAIL_HAS_HYPHENS_PROB = 0.1

EMAIL_SURNAMES_JOINED_HYPHEN = 0.8
EMAIL_SURNAMES_JOINED_NO_PUNC = EMAIL_SURNAMES_JOINED_HYPHEN + 0.1


# NAMES
COMMON_FIRST_NAME_INDEX = 118
RARE_FIRST_NAME_INDEX = 118 + 984
COMMON_FIRST_NAME_PROB = .80
RARE_FIRST_NAME_PROB = COMMON_FIRST_NAME_PROB + .07

COMMON_SURNAME_INDEX = 2000
RARE_SURNAME_INDEX = 5000
COMMON_SURNAME_PROB = .8
RARE_SURNAME_PROB = COMMON_SURNAME_PROB + .15

GIVEN_NAME = "GIVEN_NAME"
MIDDLE_INITIAL = "MIDDLE_INITIAL"
SURNAME = "SURNAME"
MIDDLE_INITIAL_LIST = set(string.ascii_uppercase)

GIVEN_NAME_FILE = DATA + "first_names.txt"
SURNAME_FILE = DATA + "surnames.txt"
TITLE_FILE = DATA + "titles.txt"
ADDRESS_FILE = DATA + "state_city_addresses.pickle"
STATES_FILE = DATA + "states.txt"


# PHONE
PHONE_SECTION_1 = 3
PHONE_SECTION_2 = 3
PHONE_SECTION_3 = 4

PHONE_TYPE_1 = "PHONE_TYPE_1"
PHONE_TYPE_2 = "PHONE_TYPE_2"
PHONE_TYPE_3 = "PHONE_TYPE_3"
PHONE_TYPE_4 = "PHONE_TYPE_4"
PHONE_TYPE_5 = "PHONE_TYPE_5"
PHONE_TYPE_6 = "PHONE_TYPE_6"
PHONE_TYPE_7 = "PHONE_TYPE_7"
PHONE_TYPE_8 = "PHONE_TYPE_8"
PHONE_SEPARATOR_PATTERN_LIST = [PHONE_TYPE_1, PHONE_TYPE_3, PHONE_TYPE_4, PHONE_TYPE_5,
                                PHONE_TYPE_6, PHONE_TYPE_7, PHONE_TYPE_8]

# -- has_country_code, has_parentheses, first_separator, second_separator, third_separator
PHONE_SEPARATORS_BY_PATTERN = {PHONE_TYPE_1: [True, False, "", "", ""],
                               PHONE_TYPE_2: [True, True, "", "", "-"],
                               PHONE_TYPE_3: [False, True, "", " ", "-"],
                               PHONE_TYPE_4: [False, True, "", " ", " "],
                               PHONE_TYPE_5: [False, False, "", "-", "-"],
                               PHONE_TYPE_6: [False, False, "", "", ""],
                               PHONE_TYPE_7: [False, True, "", "", "-"],
                               PHONE_TYPE_8: [True, False, "-", "-", "-"]
                               }

PHONE_PARENS_PROB = 0.3
PHONE_COUNTRY_CODE_PROB = 0.2


# ZIP
ZIP_LENGTH = 5
