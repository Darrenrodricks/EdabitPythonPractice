# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid

data = {"Darth Vader" : "Father", "Leia" : "sister", "Han" : "brother in law", "R2D2" : "droid" }

def relation_to_luke(name):
    name = data.get(name)
    print("Luke I am your {}".format(name))


relation_to_luke("Darth Vader")

relation_to_luke("Leia")

relation_to_luke("Han")
