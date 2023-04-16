import math
import pandas as pd

pd.set_option('display.max_rows',600)
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000000)
pd.set_eng_float_format(2,use_eng_prefix = True)
pd.set_option('mode.chained_assignment',None)

data = pd.read_csv('Final.csv',index_col = 0)

def watch_score(score_list):
    """

    :param score_list: list of integers
    :return: final rating
    """
    final = 0

    for score in score_list:
        if score > 10:
            score /= 10

        if 0 <= score < 6:
            final += 0
        if 6 <= score < 7:
            final += 1
        if 7 <= score < 8:
            final += 2
        if 8 <= score < 9:
            final += 3
        if score >= 9:
            final += 4

    return math.ceil(final / 12 * 10)

scores = ['rotten_score','audience_score','imdb_score']

# creating a list of all scores in dataframe
data['_list_'] = data[scores].values.tolist()

# Applying scoring function to list
data['watch_score'] = data['_list_'].apply(lambda x: watch_score(x))

# removing the redundant list column created earlier
data.drop(columns = '_list_',inplace = True)

# Creating CSV
data.to_csv('my_score.csv',encoding = 'utf-8')
