planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
print("After step 1:", planet_list)

more_planets = ["Uranus", "Neptune"]

planet_list.extend(more_planets)
print("After step 2:", planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print("After step 3:", planet_list)

planet_list.append("Pluto")
print("After step 4:", planet_list)

rocky_planets = planet_list[0:4]
print("After step 5 - Rocky Planets:", rocky_planets)

del planet_list[-1]
print("After step 6:", planet_list)