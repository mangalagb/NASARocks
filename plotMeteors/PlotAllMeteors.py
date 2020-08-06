from folium.plugins import MarkerCluster
import pandas as pd
import folium

meteors_raw_data = pd.read_csv("/home/gowri/Documents/workspace/NASARocks/data/Meteorite_Landings.csv")
meteors = meteors_raw_data.dropna(subset=["reclong", "reclat"]).drop_duplicates(subset=["reclong", "reclat"])

map = folium.Map(tiles='cartodbpositron', zoom_start=5)
marker_cluster = MarkerCluster().add_to(map)

for index, row in meteors.iterrows():
    name = row["name"]
    year = str(row["year"])
    latitude = row['reclat']
    longitude = row['reclong']

    popup_text = '<h3 style="color:green;">' + name + '</h3>'
    if year.lower() != "nan":
        popup_text = popup_text + ", " + year

    folium.Marker(location=[latitude, longitude], tooltip=popup_text).add_to(marker_cluster)

    print(index, popup_text)

