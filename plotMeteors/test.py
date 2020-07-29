import matplotlib.pyplot as plt
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

data = pd.read_csv('../data/Meteorite_Landings.csv')
meteors_raw_data = data[40000:]
#45,000

ax = []
meteors = meteors_raw_data.drop_duplicates(subset=["reclat", "reclong"])
meteors = meteors.dropna(subset=['GeoLocation'])

print("Drawing map of all points of meteors landings")
# for index, row in meteors.iterrows():
#     longitude = row['reclong']
#     latitude = row['reclat']
#     name = row["name"]
#
#     if longitude and latitude and longitude != 0 and latitude != 0 and not pd.isnull(longitude) and not pd.isnull(latitude):
#         ax = plt.plot(longitude, latitude, marker='o', color='Red', markersize=10)
#         #print(name, longitude, latitude)
#     # mplleaflet.show(fig=ax[0].figure)


print("Drawing map of countries of meteors landings")

#Perform reverse geocoding to map latitude and longitude to countries
meteors['GeoLocation'] = meteors['GeoLocation'].map(lambda x: x.lstrip('(').rstrip(')'))

locator = Nominatim(user_agent="myGeocoder", timeout=10)
rgeocode = RateLimiter(locator.reverse, min_delay_seconds=0.001)

print("Finding countries where meteors dropped...")
countries = []
for index, row in meteors.iterrows():
    longitude = row['reclong']
    latitude = row['reclat']
    coordinates = row["GeoLocation"]

    country = None
    try:
        result = locator.reverse(coordinates)
        address = result.raw["address"]
        country = address["country"]
        print(country, index)
    except:
        print(index)
    countries.append(country)


#Add country to original data frame
meteors["Country"] = countries

# Write to file
print("Writing to file...")
meteors.to_csv("Meteors_Landings_with_countries.csv", mode='a', encoding='utf-8', index=False)
print("Finished writing to file")

