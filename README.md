# PIISynthesis
Generate synthetic Personally Identifiable Information (PII) for de-identified data as an additional layer of information security.

De-identification is commonly performed on sensitive data, but the processes used to do so aren't perfect. 
PII can be missed during de-identification, potentially rendering someone vulnerable to identification.

In places where a de-identification process has tagged PII in a document, this prototype tool replaces that information with randomly generated, realistic data.
This way, even when some real PII is missed during de-identification, it will be extremely difficult to tell which is real and which is fake, further protecting that information.

PIISynthesis is currently set up to work with output of a de-identification tool called DeID. 

## Example

Input Document
```
Patient: **NAME[Homer J. Simpson]
Age: **AGE[in 60s]
DOB: **DATE[05/26/1974]

**NAME[Homer] complains of sleepiness throughout the day, presents signs of narcolepsy.

Dr. **NAME[Hibbert]
**PHONE
**EMAIL
```

Output Document
```
Patient: Thomas A. Warren
Age: 63
DOB: 05/26/1974

Thomas complains of sleepiness throughout the day, presents signs of narcolepsy.

Dr. Chung
(577) 541-4903
icourtney@optimum.net
```

## Current Data Types Available for Replacement

* Names
* Ages
* Emails
* Phone Numbers
* Device IDs
* ZIP Codes

## Data Types in Development

US Addresses

* Geographic information more specific than the state level is considered PII. The script identifies the state if present and replaces the de-id tag with a randomly selected city and real address found within that state. Using a fake address would be easy to search for and find to be made-up.  


## Script Input

Currently the script expects the input files to have PII marked with tags preceeded by double asterisks, but different tags have different properties.


### NAME 
DeID retains real names in brackets after the tag NAME. 
This allows PIISynthesis to use the same generated name consistently for the same real name, and likely generate first names for first names and last names for last names

Example:

`**NAME[Homer Simpson]`

### AGE
DeID retains age ranges in brackets after the tag AGE.
PIISynthesis will generate a random age within the range.

The ranges are:
* "birth-12"
* "in teens
* "in 20s", "in 30s", etc.
* 90+

Example:
`**AGE[in 60s]`


### DATE
DeID already provides a random replacement for dates in brackets after the tag DATE.
PIISynthesis simply removes the tag format and uses the date provided.

Example:

`**DATE[05/25/1975]`

### PHONE
PIISynthesis generates a random series of numbers in one of several formats

`**PHONE`

### EMAIL
PIISynthesis generates a random email with one of a wide variety of real domains.

`**EMAIL`

### ZIP-CODE
PIISynthesis generates a random 5-digit code

`**ZIP-CODE`

### DEVICE-ID
PIISynthesis generates a random serial ID or alphanumeric string

`**DEVICE-ID`


## Run

```python3 synthesize_identifiers.py INPUT_DIR OUTPUT_DIR```

INPUT_DIR is a directory containing files tagged for PII. 
OUTPUT_DIR is a directory to write the files with synthesized PII.

