uncommon_names = []
midtier_names = []
common_names = []

with open("yob1980.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    name, gender, number_str = line.split(",")
    number = int(number_str)

    if number < 300:
        uncommon_names.append(name)
    elif number > 5000:
        common_names.append(name)
    else:
        midtier_names.append(name)

print(len(common_names))
print(len(uncommon_names))
print(len(midtier_names))

with open("first_names.txt", "w") as file:
    file.write("\n".join(common_names))
    file.write("\n".join(midtier_names))
    file.write("\n".join(uncommon_names))
