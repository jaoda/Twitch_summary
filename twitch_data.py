import pandas as pd
import matplotlib.pyplot as plt

# ["Most watched games on Twitch - SullyGnome.csv", "Most streamed games on Twitch - SullyGnome.csv"]
path_watched = "P:\\Projekty\\Python\\Twitch\\Main\\Most watched games on Twitch - SullyGnome.csv"
path_streamed = "P:\\Projekty\\Python\\Twitch\\Main\\Most streamed games on Twitch - SullyGnome.csv"

df_watched = pd.read_csv(path_watched)
df_streamed = pd.read_csv(path_streamed)

print(df_streamed) 

df_w = df_watched.head(15)

plt.figure(figsize=(10,6))

plt.bar(df_w['Game'], df_w['Average viewers'], color='gold', width = 0.4, label = "Average viewers")
plt.bar(df_w['Game'], df_w['Peak viewers'], color = 'red', width=0.4, label="Peak viewers", bottom = df_w['Average viewers'])

plt.xlabel('Game')
plt.xticks(rotation = 45)
plt.title('Average viewers with peak for Top 15')
plt.legend()

plt.show()
