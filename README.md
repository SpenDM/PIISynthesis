# PIISynthesis
Generate synthetic Personally Identifiable Information (PII) for deidentified data as an additional layer of information security.

Deidentification is commonly performed on sensitive data, but the processes used to do so aren't perfect. 
PII can be missed during deidentification, potentially rendering someone vulnerable to identification.

In places where a deidentification process has removed information from a document, this tool replaces that information with randomly generated, realistic data.
This way, even when some real PII is missed during deidentification, it will be extremely difficult to tell which is real and which is fake, further protecting that information.

## Current Data Types Available for Replacement

* Names
* Ages
* US Addresses

Geographic information more specific than the state level is considered PII. The script identifies the state if present and replaces the de-id tag with a randomly selected city and real address found within that state. Using a fake address would be easy to search for and find to be made-up.  

* Emails
* ID Numbers
* 

## Run

```python3 synthesize_identifiers.py INPUT_DIR OUTPUT_DIR```

INPUT_DIR contains deidentified files. Currently the script expects the input files to have deidentified information to be replaced with specific tags surrounded by double asterisks:

```
**NAME**
**PLACE**
**INSTITUTION**
**STREET-ADDRESS**
**ZIP-CODE**
**DATE**
**AGE**
**PHONE**
**EMAIL**
**ID-NUM**
**DEVICE-ID**
**WEB-LOC**
**PATH-NUMBER**
```

