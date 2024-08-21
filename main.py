import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv("spotify-2023_fixed.csv")



#Задание 1
sns.scatterplot(data=df, x="track_name", y="in_spotify_charts")
sns.relplot(data=df, kind="line", x="track_name", y="in_spotify_charts")

plt.show()



#Задание 2
# Получение уникальных значений для каждого признака
unique_counts = {}
for column in df.columns:
    unique_vals = df[column].unique()
    unique_counts[column] = len(unique_vals)

# Сортировка по количеству уникальных значений
sorted_counts = sorted(unique_counts.items(), key=lambda x: x[1], reverse=True)

# Выбор двух признаков с наибольшим количеством уникальных значений
top_features = sorted_counts[:2]

print(f"Два признака с наибольшим количеством уникальных числовых значений: {top_features}")



#Задание 3
def categorize_streams(streams):
    if streams < 1000:
        return 'Low'
    elif 1000 <= streams <= 10000:
        return 'Medium'
    else:
        return 'High'
    
df['Streams_category'] = df['streams'].apply(categorize_streams)
        
# Создание нового признака 'Track_name_category'
def categorize_track_name(track_name):
    first_letter = track_name[0].upper()
    if 'A' <= first_letter <= 'F':
        return 'A-F'
    elif 'G' <= first_letter <= 'L':
        return 'G-L'
    elif 'M' <= first_letter <= 'R':
        return 'M-R'
    else:
        return 'S-Z'

df['Track_name_category'] = df['track_name'].apply(categorize_track_name)



#Задание 4
sns.scatterplot(data=df, x="track_name", y="in_spotify_charts", hue="Streams_category", size="Track_name_category", palette='crest')
sns.relplot(data=df, kind="line", x="track_name", y="in_spotify_charts", hue="Streams_category", size="Track_name_category", palette='crest')

plt.show()



#Задание 5
rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["in_apple_charts", "in_shazam_charts", "in_deezer_charts", "in_spotify_charts"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)

plt.show()