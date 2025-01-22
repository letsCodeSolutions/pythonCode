students = {
    "male":["Manish", "Rohan","Raj","Shy","Sher"],
    "female": ["Rin","Rina","Shila","Sita"]
    }

for key in students.keys():
    for people in students[key]:
        if "a" in people:
            print("Name containing a {}".format(people))
