import pandas as pd
import json
import matplotlib.pyplot as plt
import math
import mplleaflet
import numpy as np


data = pd.read_csv('Meteorite_Landings.csv')
meteors_raw_data = data[:]

ax = []
meteors = meteors_raw_data.drop_duplicates(subset=["reclong", "reclat"])

for index, row in meteors.iterrows():
    longitude = row['reclong']
    latitude = row['reclat']
    name = row["name"]

    if longitude and latitude and longitude != 0 and latitude != 0 and not pd.isnull(longitude) and not pd.isnull(latitude):
        ax = plt.plot(longitude, latitude, marker='o', color='Red', markersize=10)
        #print(name, longitude, latitude)


print("drawing map")
mplleaflet.show(fig=ax[0].figure)
