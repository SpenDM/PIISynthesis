import re

with open("state_info.txt", "r") as in_file:
    lines = in_file.readlines()

states = {}     # state name : abbrev

found_abbr = False
abbr = ""

for line in lines:

    if not found_abbr:
        has_abbr = re.search(r"<b>(\S+)</b>", line)
        if has_abbr:
            abbr = has_abbr.groups()[0]
            found_abbr = True

    else:
        has_state = re.search(r"\">(.+?)</a>", line)
        if has_state:
            state = has_state.groups()[0]
            states[state] = abbr

        found_abbr = False

out_file = open("states.txt", "w")
for state, abbr in states.items():
    out_file.write(state + "\t" + abbr + "\n")

out_file.close()
