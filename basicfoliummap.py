import folium
import pandas as pd

#this is pretty crude

US_COORDINATES = (48, -102)

crimedata = pd.read_csv('schoolgunslonglat.csv')
latitude = crimedata["Latitude"].tolist()
longitude = crimedata["Longitude"].tolist()
killed = crimedata["Killed"].tolist()
injured = crimedata["Injured"].tolist()
victims = [x+y for x,y in zip(killed,injured)]

# create empty map centered on somewhere in the middle of the US

mymap = folium.Map(location=US_COORDINATES, zoom_start=4)

# add a marker for every record in the filtered data, use a clustered view

for lat,long,count in zip(latitude,longitude,victims):
    folium.Marker([float(lat), float(long)], popup=str(count)).add_to(mymap)
 
mymap.save('shootingmap.html')

