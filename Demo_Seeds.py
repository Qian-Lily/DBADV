from sklearn.datasets import fetch_openml
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from DBADV import DBADV

# Seeds: 3 classes;210 samples;7 dimensionality
data = fetch_openml('seeds', version=1)  # X, y = fetch_openml('seeds', version=1, return_X_y=True)
X = data.data
Y = data.target

# Standarize features
X = MinMaxScaler().fit_transform(X)

y_pred = DBADV(X, perplexity=14, MinPts=15, probability=0.977)
NMI = metrics.normalized_mutual_info_score(Y, y_pred, average_method='arithmetic')
print("NMI of Seeds data set:", round(NMI, 2))
