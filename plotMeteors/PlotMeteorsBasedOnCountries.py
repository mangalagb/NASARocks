import pandas as pd

data = pd.read_csv("/home/gowri/Documents/workspace/NASARocks/data/Meteors_Landings_with_countries.csv")
meteors_raw_data = data[:]
print(data)

