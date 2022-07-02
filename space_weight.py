d = dict()
d["mecury"] = 0.38
d["venus"] = 0.91
d["mars"] = 0.38
d["jupiter"] = 2.34
d["saturn"] = 0.93
d["uranus"] = 0.92
d["neptune"] = 1.12
d["pluto"] = 0.62

space_weight = 0

def weight(space_weight):
    weight = int(input("What is your weight? "))
    planet = input("Where are you going? ")
    planet = planet.lower()
    space_weight = d[planet] * weight
    print("Your weight will be: ", space_weight)

weight(space_weight)