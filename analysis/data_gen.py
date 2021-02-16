## Use this file to generate data needed into a csv file in order to initiatlize
## plotting the time series plot live as the csv is updated.

# Dependecies
import csv
import time
import os
import pandas as pd

print(os.chdir('/Users/ZTC/Desktop/Penn Data Analytics Bootcamp/Projects/Project 1 - Spotify Data (Presentation 2:20)/bootcamp-project1-spotify/analysis/'))

file = '../cleaned_data/cleaned_data_by_year.csv'
year_df = pd.read_csv(file)

line_data = year_df[['year','acousticness','danceability','energy','instrumentalness','liveness','speechiness','valence']]
line_data

year = 1920

fieldnames = ['year', 'acousticness','danceability','energy','instrumentalness','liveness','speechiness','valence']

with open('../output_csv/data_gen.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

for index, row in line_data.iterrows():

    # while True:

    with open('../output_csv/data_gen.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            'year': line_data.iloc[index, 0],
            'acousticness': line_data.iloc[index, 1],
            'danceability': line_data.iloc[index, 2],
            'energy': line_data.iloc[index, 3],
            'instrumentalness': line_data.iloc[index, 4],
            'liveness': line_data.iloc[index, 5],
            'speechiness': line_data.iloc[index, 6],
            'valence': line_data.iloc[index, 7]
        }

        csv_writer.writerow(info)

        print(f'Writing data for year {year}')
        year += 1

    time.sleep(0.5)
