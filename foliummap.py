import folium
import pandas as pd

US_COORDINATES = (48, -102)

crimedata = pd.read_csv('schoolgunslonglat.csv')
latitude = crimedata["Latitude"].tolist()
longitude = crimedata["Longitude"].tolist()
killed = crimedata["Killed"].tolist()
injured = crimedata["Injured"].tolist()
victims = [x+y for x,y in zip(killed,injured)]

# create empty map zoomed in on San Francisco

mymap = folium.Map(location=US_COORDINATES, zoom_start=6)

# add a marker for every record in the filtered data, use a clustered view

for lat,long,count in zip(latitude,longitude,victims):
    folium.Marker([float(lat), float(long)], popup=str(count)).add_to(mymap)
 
mymap.save('shootingmap.html')

