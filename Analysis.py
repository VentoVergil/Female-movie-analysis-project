import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,confusion_matrix,ConfusionMatrixDisplay as con_mat_plt
import my_functions

pd.set_option('display.max_rows',600)
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000000)
pd.set_eng_float_format(2,use_eng_prefix = True)

# Non-Documentary English films longer than 45 minutes
data = pd.read_csv(filepath_or_buffer = r'C:\Users\Te.TE\Documents\Serpent\Data\CSV\Female\18_to_23_NDE.csv',
                   index_col = 0)  # len=14,886

# A new column 'fem' is manually created with 466 manually classified 0 or 1
# fem Movies == 1, non fem movies == 0

data['fem'] = data['fem'].astype(int,errors = 'ignore')  # datatype for fem is set to integer

data.drop_duplicates(subset = ['title','genres','synopsis'],inplace = True)  # dupicate rows removed. new_len =11,619

trainer = data[~data['fem'].isna()]  # data with manual classification  len=466
test_set = data[data['fem'].isna()]  # data with no classification  len=11,153

features = trainer['synopsis']  # Movie synopsis used as model feature for text classification
target = trainer['fem'].astype(int)

stop_words = ['the','of','and','in','to','his','he','him','with','an','is','on','for','when','their','as','they','that'
              ,'but','by','from','who','which','at','on','it','has','up','them','this','are','be','only','all','what',
              'where','not','while','after','into','can']  # manually created stopwords list excluding feminie stopwords

vectorizer = CountVectorizer(stop_words = stop_words,ngram_range = (1,3),min_df = 50)   # initializing count vectorizer
Q1,Q2,A1,A2 = train_test_split(features,np.ravel(target),stratify = target,random_state = 1,train_size = 0.4,
                               test_size = 0.6)

my_functions.shapesy(Q1,Q2,A1,A2)  # confirming shapes of training and testing dataset

Q1_vect = vectorizer.fit_transform(Q1)  # fitting count vectorizer on first train split
model = LogisticRegression()
model.fit(Q1_vect,A1)

model_test = model.predict(vectorizer.transform(Q2))  # comparing the predicted values from model with test set
print(roc_auc_score(A2,model_test))  # 0.8410230409554392

# Plotting and saving confusion matrix
con_mat_plt(confusion_matrix(y_true = A2,y_pred = model_test),display_labels = [False,True])\
    .plot(cmap = 'binary',colorbar = False)
plt.savefig('Confusion Matrix.png')

no_synops = test_set[~test_set['synopsis'].isna()]  # ignoring rows with no synopsis

fem_pred = model.predict(vectorizer.transform(no_synops['synopsis']))  # using model to predict class using synopsis
mo = pd.DataFrame(data = {'fem': fem_pred,'title': no_synops.title},index = no_synops.index.tolist())

# Joining predicted set to origonal set
test_set_predicted = (no_synops.merge(mo,left_index = True,right_index = True,how = 'left')
                      .drop(columns = ['fem_x','title_y'])
                      .rename(columns = {'title_x': 'title','fem_y': 'fem'}))

joint = (pd.concat([test_set_predicted,trainer])
         .reset_index(drop = True))

joint['fem'] = joint['fem'].astype(int,errors = 'ignore')
joint.drop(columns = 'credits',inplace = True)

# removing movies with documentary genre
no_documentaries = joint[joint['genres'].str.lower().str.contains('documentary') == False]
no_documentaries.reset_index(drop = True,inplace = True)

# Saving dataset with predicted labels to new csv file
no_documentaries.to_csv('after_prediction.csv',encoding = 'utf-8')
