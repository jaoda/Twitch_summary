import pandas as pd

# ["Most watched games on Twitch - SullyGnome.csv", "Most streamed games on Twitch - SullyGnome.csv"]
path_watched = "P:\\Projekty\\Python\\Twitch\\Main\\Most watched games on Twitch - SullyGnome.csv"
path_streamed = "P:\\Projekty\\Python\\Twitch\\Main\\Most streamed games on Twitch - SullyGnome.csv"

df_watched = pd.read_csv(path_watched)
df_streamed = pd.read_csv(path_streamed)

print(df_streamed)