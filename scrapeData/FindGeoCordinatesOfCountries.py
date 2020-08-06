import pandas as pd
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

def readAndCleanData():
    data = pd.read_csv("/home/gowri/Documents/workspace/NASARocks/data/Meteors_Landings_with_countries.csv")
    meteors = data[:]

    df = meteors.reset_index()
    countries = df['Country'].value_counts(sort=True)
    return countries[:]


def findGeocode(country):
    try:
        geolocator = Nominatim(user_agent="myGeocoder")
        return geolocator.geocode(country)
    except GeocoderTimedOut:
        return findGeocode(country)


def findCountryCoordinates():
    countries = readAndCleanData()
    latitude = []
    longitude = []

    for country, row in countries.items():
        result = findGeocode(country)
        print(result)
        if result:
            latitude.append(result.latitude)
            longitude.append(result.longitude)
        else:
            latitude.append(None)
            longitude.append(None)

    countries_df = pd.DataFrame({'country': countries.index, 'meteor_count': countries.values})
    countries_df["latitude"] = latitude
    countries_df["longitude"] = longitude
    write_to_file(countries_df)

def write_to_file(countries):
    print("Writing to file...")
    countries.to_csv("Meteors_Landings_with_country_count.csv", encoding='utf-8', index=False)
    print("Finished writing to file")


findCountryCoordinates()
