from geopy.geocoders import GeoNames
import pandas

starterdf = pandas.read_csv("./schoolguns.csv")
cities = starterdf["City Or County"].tolist()
states = starterdf["State"].tolist()
killed = starterdf["# Killed"].tolist()
injured = starterdf["# Injured"].tolist()
Latitude = []
Longitude = []
geolocator = GeoNames(username='jas741')  # Register at Geonames
for city,state in zip(cities,states):
    location = geolocator.geocode(city +"," + state, timeout=20)
    if location is not None:
        Latitude.append(location.latitude)
        Longitude.append(location.longitude)
        print(city + " " + state + " " + str(location.latitude) + " " + str(location.longitude))
    else:
        Latitude.append(" ")
        Longitude.append(" ")

df = pandas.DataFrame(data={"State": states, "City or Count": cities, "Latitude": Latitude, "Longitude": Longitude, "Killed": killed, "Injured": injured})
df.to_csv("./schoolgunslonglat.csv", sep=',',index=False)

#what i want to do is: add size for number hurt or killed, color for area population density
