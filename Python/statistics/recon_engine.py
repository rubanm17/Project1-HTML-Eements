import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

r_df = pd.read_csv('ratings.csv')
r_df.head()

m_df = pd.read_csv('movies.csv')
m_df.head()

m_df['year'] = m_df.title.str.extract('(\(\d\d\d\d\))' , expand=True)
m_df.head()
m_df['year'] = m_df.year.str.extract('(\d\d\d\d)' , expand=True)
m_df.head()
m_df['title'] = m_df.title.str.extract('(\(\d\d\d\d\))' ,'')
m_df.head()
m_df['title'] = m_df['title'].apply(lambda x: x.strip())
m_df.head()
m_df['genres'] = m_df.genres.str.split('|')
m_df.head()

r_df = r_df.drop(['timestamp'],axis=1)

user_inp = [
    {'title': 'Grand Slam','rating':5.6},
    {'title': 'Zero','rating':7},
    {'title': 'Jumanji','rating':8.5},
    {'title': 'toy story','rating':4.5}
]
m_inp = pd.DataFrame(user_inp)
m_inp

inp_id = m_df[m_df['title'].isin(m_inp['title'].tolist())]
m_inp = pd.merge(inp_id,m_inp)
m_inp
m_inp = m_inp.drop(['genres','year'],axis=1)
m_inp
m_user = m_cp[m_cp['movield'].isin(m_inp['movield'].tolist())]
m_user
m_user = m_user.drop(['movieId','genres',],axis=1)
m_user
usergntl = m_user.drop(['title','genres','movieID','year'],axis=1)
usergntl
userprof = usergntl.transpose().dot(m_inp['rating'])
userprof
genretl = m_cp.set_index(m_cp['movieId'])
genretl
genretl = genretl.drop(['movieId','title','genres','year'],axis=1)
genretl.head()
recon_df = ((genretl*userprof).sum(axis=1)/userprof.sum())
recon_df.head()

recon_df = recon_df.sort_values(ascending=False)
recon_df.head()

recontl = m_df.loc[m_df['movieId'].isin(recon_df.head(20).keys())]
recontl