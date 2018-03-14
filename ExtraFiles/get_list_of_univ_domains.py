import json
from pprint import pprint

outfile = open("university_domains.txt", "w")

with open('world_universities_and_domains.json') as data_file:
    universities = json.load(data_file)

for university in universities:
    domain = university["domain"]
    outfile.writelines(domain + "\n")
