place_file = open("places.csv")
all_place = []
for places in place_file:
    places = places.strip()
    places = places.split(",")
    all_place.append(places)

for each in range(len(all_place)):


all_place.sort(key = myFunc)
print(all_place)







place_file.close()