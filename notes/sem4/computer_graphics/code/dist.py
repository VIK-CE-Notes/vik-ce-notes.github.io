from math import sin, cos, sqrt, atan2, radians

# Approximate radius of earth in km
R = 6000

lat1 = radians(45)
lon1 = radians(165)
lat2 = radians(45)
lon2 = radians(50)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result: ", distance)
print("Should be: ", 278.546, "km")