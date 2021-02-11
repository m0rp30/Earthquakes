import requests
import folium
import datetime

#response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson") # Past 7 days significant Earthquakes
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson") # Past 7 days all Earthquakes
json_response = response.json()

m = folium.Map(location=[42.6, -9.5], zoom_start=2)
features = json_response['features']

for feature in features:
    magnitude = feature['properties']['mag']
    title = feature['properties']['title']
    date_time = datetime.datetime.fromtimestamp(int(str(feature['properties']['time'])[:-3]))
    longitude = feature['geometry']['coordinates'][0]
    latitude = feature['geometry']['coordinates'][1]
    
    folium.Marker(
        location=[latitude, longitude],
        popup=title,
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

m
