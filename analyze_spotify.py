
import ast
import csv
with open('top_50_2023.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)


GENRE = header.index('genres')
for row in rows:
    row[GENRE] = ast.literal_eval(row[GENRE])


def is_valid(num:str):
    try:
        num = float(num)
        if 0 < num < 1:
            return True
        return False
    except ValueError:
        return False

# average dancebility
DANCEABILITY = header.index('danceability')
sum_dance = 0
counter = 0
for row in rows:
    if is_valid(row[DANCEABILITY]):
        counter += 1
        sum_dance += float(row[DANCEABILITY])
print('average' , sum_dance/counter)

#is explicit
EXPLICIT = header.index('is_explicit')
exp_songs = 0
for row in rows:
    if row[EXPLICIT] == 'True':
        exp_songs +=1
print('explicit', exp_songs)

# top 3 genres
genres_count = {}
for row in rows:
    for genre in row[GENRE]:
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1

top_3_genres = sorted(genres_count.items(),key=lambda x: x[1], reverse=True)[:3]
print(top_3_genres)

# top 3 artists
ARTIST = header.index('artist_name')
artists_popularity = {}
for row in rows:
    if row[ARTIST] in artists_popularity:
        artists_popularity[row[ARTIST]] += 1
    else:
        artists_popularity[row[ARTIST]] = 1

top_3_artists = sorted(artists_popularity.items(), key=lambda  x: x[1], reverse=True)[:3]
print(top_3_artists)


#Average Liveliness with Energy Criteria
ENERGY = header.index('energy')
sum_energy = 0
for row in rows:
    if float(row[ENERGY]) > 0.5:
        sum_energy += float(row[ENERGY])
average_energy = sum_energy/len(rows)
print(average_energy)

# The most popular year
years_popularity = {}
YEAR = header.index('album_release_date')
for row in rows:
    year = row[YEAR][:4]
    if year in years_popularity:
        years_popularity[year] += 1
    else:
        years_popularity[year] = 1
top_year = sorted(years_popularity.items(),key=lambda x: x[1],reverse=True)[0]
print(top_year)
