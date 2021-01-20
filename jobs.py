import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
import datetime

#open file
bis=pd.read_csv('BusinessAnalyst.csv', na_values=[-1,'-1'])
print(bis.columns)
bis=DataFrame(bis)
print(bis)


from wordcloud import WordCloud

stopWords = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

def get_wordcloud(series): #simple function to tokenize and plot a said column
    word_cloud = ''
    
    for job in series:
        tokens = tokenizer.tokenize(job)
        for token in tokens:
            if token not in stopWords:
                word_cloud += ''.join(token) + ' '

    wordcloud = WordCloud(height=500,margin=0,max_words=300,
                          colormap='Set1').generate(word_cloud) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

job_title=bis['Job_Title'].apply(lambda x: x.lower())
get_wordcloud()

