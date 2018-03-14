with open("us_cities_states_counties.csv", "r") as in_file:
    lines = in_file.readlines()

state_abbrs = {}
state_cities = {}
state_counts = {}
all_city_counts = {}

# Get state abbreviations, and city names and their counts
for line in lines[1:]:
    chunks = line.split("|")
    if len(chunks) > 3:
        state = chunks[2]
        abbr = chunks[1]
        city = chunks[0]

        # state-based counts
        if state not in state_abbrs:
            state_abbrs[state] = abbr
            state_cities[state] = {}
            state_cities[state][city] = 1
            state_counts[state] = 1

        elif city not in state_cities[state]:
            state_cities[state][city] = 1
            state_counts[state] += 1

        else:
            state_cities[state][city] += 1
            state_counts[state] += 1

        # all cities
        if city not in all_city_counts:
            all_city_counts[city] = 1
        else:
            all_city_counts[city] += 1

print("me")
