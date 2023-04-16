from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from rotten_tomatoes_scraper.rt_scraper import MovieScraper
import time
from PyMovieDb import IMDB
from json import loads

pd.set_option('display.max_rows',600)
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000000)
pd.set_eng_float_format(2,use_eng_prefix = True)
pd.set_option('mode.chained_assignment', None)

data = pd.read_csv(filepath_or_buffer = r'C:\xxxx\xxxx\xxxx\xxxx\xxxx\xxxx\xxxx\after_prediction.csv',index_col = 0)

# scraping rotten tomatoes for movie ratings
# this process was carried out 6 times, in batches of 500 over a 12-hour period for traffic purposes
# this resulted in 6 seperate files
# data range was changed manually each time

female = data[data['fem'] == 1][:500]

no = 0
file = 1
sc_rt = []
sc_au = []

for name in female['title']:
    movie_name = name.replace(' ','_')

    # todo: confirm movie year
    try:
        movie_url = f'https://www.rottentomatoes.com/m/{movie_name}'
        movie_scraper = MovieScraper(movie_url = movie_url)
        movie_scraper.extract_metadata()
        scra = movie_scraper.metadata
        sc_rt.append(scra['Score_Rotten'])
        sc_au.append(scra['Score_Audience'])

    except:
        sc_rt.append(np.nan)
        sc_au.append(np.nan)

    print(no)
    time.sleep(0.05)

    no += 1

female['rotten_score'] = sc_rt
female['audience_score'] = sc_au
    
female.to_csv(fr"C:\xxxx\xxxx\xxxx\xxxx\xxxx\CSV\Female\rotten scores\with_rotten{no}.csv",encoding = 'utf-8')


# merging all 6 rotten score files
files = glob(fr"C:\xxxx\xxxx\xxxx\xxxx\xxxx\CSV\Female\Data\rotten scores\*.csv")
rotten = pd.concat((pd.read_csv(file,encoding = 'UTF-8') for file in files),ignore_index = True)

rotten.to_csv('female_rotten.csv',encoding = 'utf-8')

# after merging all rotten scores
merged_rotten = pd.read_csv(filepath_or_buffer = 'female_rotten.csv',index_col = 0)

(
    merged_rotten.dropna(subset = ['audience_score','rotten_score'])
    .rename(columns = {'runtime (minutes)': 'duration'})
    .drop(columns = ['merged_rotten','synopsis'])
    .reset_index(drop = True)
)


no = 1
imdb = IMDB()

n_raters = []
rating = []

first = merged_rotten[:500]

for index in first.index:
    name = first.loc[index,'title']
    year = int(first.loc[index,'release_year'])

    try:
        movie = imdb.get_by_name(name,tv = False,year = year)
        fix = loads(movie)  # convert to dict

        n_raters.append(fix['rating']['ratingCount'])
        rating.append(fix['rating']['ratingValue'])

    except:
        n_raters.append(np.nan)
        rating.append(np.nan)

    print(no)
    time.sleep(1)

    no += 1

first['imdb_rater_count'] = n_raters
first['imdb_score'] = rating

female.to_csv(fr"C:\xxxx\xxxx\xxxx\xxxx\xxxx\CSV\Female\imdb scores\with_imdb{no}.csv",encoding = 'utf-8')

# merging all 6 imdb score files
files = glob(r'C:\Users\Te.TE\Documents\Serpent\Data\imdb scores\*.csv')
imdb = pd.concat((pd.read_csv(file,encoding = 'UTF-8') for file in files),ignore_index = True)

imdb.to_csv('Final.csv',encoding = 'utf-8')

