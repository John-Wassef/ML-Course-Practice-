import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import statsmodels.api as sm
import seaborn as sns
from sklearn.cluster import KMeans

sns.set()

data=pd.read_csv('3.01. Country clusters.csv')

x=data.iloc[:,1:3]

number_of_clusters=3

kmeans=KMeans(number_of_clusters)
kmeans.fit(x)

identified_clusters=kmeans.fit_predict(x)

data_with_clusters=data.copy()
data_with_clusters['Cluster']=identified_clusters
print(data_with_clusters)

plot.scatter(data['Longitude'],data['Latitude'],c=data_with_clusters['Cluster'],cmap='rainbow')
plot.xlim(-180,180)
plot.ylim(-90,90)
plot.show()