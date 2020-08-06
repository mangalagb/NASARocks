import pandas as pd
import matplotlib.pyplot as plt
import math
import geopandas

meteors = pd.read_csv("/home/gowri/Documents/workspace/NASARocks/data/Meteors_Landings_with_country_count.csv")
meteors = meteors[:10]

world_geojson = geopandas.read_file('/home/gowri/Documents/workspace/NASARocks/data/countries.geojson')
#print(world_geojson.head())
world_geojson.plot()

for index, row in meteors.iterrows():
    meteor_count = row["meteor_count"]
    latitude = row["latitude"]
    longitude = row["longitude"]
    ax = plt.plot(longitude,latitude,marker='o',color='Red',markersize=int(math.sqrt(meteor_count))*0.5)
