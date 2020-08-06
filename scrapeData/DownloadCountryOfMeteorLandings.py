import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

data = pd.read_csv("/home/gowri/Documents/workspace/NASARocks/data/Meteorite_Landings.csv")
meteors_raw_data = data[:]

ax = []
meteors = meteors_raw_data.drop_duplicates(subset=["reclat", "reclong"])
meteors = meteors.dropna(subset=['GeoLocation'])

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
    except GeocoderTimedOut:
        print(index)
    countries.append(country)


#Add country to original data frame
meteors["Country"] = countries

# Write to file
print("Writing to file...")
meteors.to_csv("Meteors_Landings_with_countries.csv", mode='a', encoding='utf-8', index=False)
print("Finished writing to file")
