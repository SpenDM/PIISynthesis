# PIISynthesis
Generate synthetic Personally Identifiable Information (PII) for deidentified data as an additional layer of information security.

Deidentification is commonly performed on sensitive data, but the processes used to do so aren't perfect. 
PII can be missed during deidentification, potentially rendering someone vulnerable to identification.

In places where a deidentification process has tagged PII in a document, this prototype tool replaces that information with randomly generated, realistic data.
This way, even when some real PII is missed during deidentification, it will be extremely difficult to tell which is real and which is fake, further protecting that information.

PIISynthesis is currently set up to work with output of the tool called DeID. 


## Current Data Types Available for Replacement

* Names
* Ages
* Emails
* ID Numbers
* ...

## Data Types in Development

US Addresses

* Geographic information more specific than the state level is considered PII. The script identifies the state if present and replaces the de-id tag with a randomly selected city and real address found within that state. Using a fake address would be easy to search for and find to be made-up.  


## Run

```python3 synthesize_identifiers.py INPUT_DIR OUTPUT_DIR```

INPUT_DIR contains files tagged for PII. 
Currently the script expects the input files to have PII marked in brackets preceeded by double asterisk with a specific tag:

```
**NAME
**PLACE
**INSTITUTION
**STREET-ADDRESS
**ZIP-CODE
**DATE
**AGE
**PHONE
**EMAIL
**ID-NUM
**DEVICE-ID
**WEB-LOC
**PATH-NUMBER
```

