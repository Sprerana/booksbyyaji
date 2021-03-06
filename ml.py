import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/INTERNSHIP/MENTORMIND/mohammad dataKitaab_MohammedSaket_data.csv")
df.head()

df.set_index(df.columns[0],inplace=True)
df.head()
data=[]
for i in range(100):
    x=df.values[i]
    x=x[~pd.isnull(x)]
    data.append(x)
data
from markovclick.models import MarkovClickstream
m = MarkovClickstream(data)
fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
sns.heatmap(m.prob_matrix, xticklabels=m.pages, yticklabels=m.pages,cmap="YlGnBu")
from markovclick.viz import visualise_markov_chain
graph = visualise_markov_chain(m)
print(graph.source)
