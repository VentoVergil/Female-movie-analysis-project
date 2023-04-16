import pandas as pd
import numpy as np

pd.set_option('display.width',1000)
pd.set_option('display.max_rows',600)
pd.set_option('display.max_columns',1000)

movies = pd.read_csv(filepath_or_buffer = r'C:\Users\Te.TE\Documents\Serpent\Data\CSV\Female\movies.csv',
                     usecols = ['id','title','genres','original_language','production_companies',
                                'release_date','budget','revenue','runtime','status','credits','overview'],
                     index_col = 'id',parse_dates = ['release_date'])

movies['release_year'] = movies['release_date'].dt.year.astype(pd.Int64Dtype())
movies.drop(columns = 'release_date',inplace = True)

# Selecting released movies from 2018 from the large data

use = (movies[(movies['release_year'] >= 2018) & (movies['status'] == 'Released') & (movies['runtime'] != 0)]
       .sort_values(by = 'release_year')
       .reset_index(drop = True))


use.dropna(subset = 'production_companies',inplace = True)  # dropping rows with no values in production column
use['budget'] = use['budget'].astype(pd.Int64Dtype(),copy=False)    # converting values to integer datatype
use['revenue'] = use['revenue'].astype(pd.Int64Dtype(),copy=False)

use = use[~use['genres'].isin(['Documentary'])]     # Removing documentaries


# creating a subsidiary csv file to be used in later analysis
use.to_csv(path_or_buf = r'C:\Users\Te.TE\Documents\Serpent\Data\datasets\18_to_23_NDE.csv',encoding = 'utf-8')

# Data is reduced from ~330,000 to ~ 15,000

